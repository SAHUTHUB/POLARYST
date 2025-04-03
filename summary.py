import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from common.utils import configs
from components.functions import serialize_conversation
from section import additional_guidelines_with_figures
from components.llms import invoke_llm
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.language_models.chat_models import BaseChatModel
from bs4 import BeautifulSoup
import matplotlib.font_manager as fm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import matplotlib.font_manager as fm
from common.utils import configs
from tvDatafeed import TvDatafeed, Interval # ✅ Import TvDatafeed และ Interval
from components.chart_utils import create_matplotlib_chart_html




SUMMARIZE_CONVERSATION_SYSTEM_PROMPT_TEMPLATE = (
    "ในฐานะผู้เชี่ยวชาญในการสรุปข้อมูลหุ้น หน้าที่ของคุณคือการสังเคราะห์และย่อรายละเอียดสำคัญจาก "
    "การแลกเปลี่ยนบทสนทนาที่ได้รับระหว่างผู้ใช้งานและ AI เป้าหมายของคุณคือการผสานข้อมูลจากทุกข้อความ "
    "ในบทสนทนาและสร้างสรุปที่เน้นเฉพาะประเด็นสำคัญเน้นตัวเลข โดยไม่มีการซ้ำซ้อนหรือบรรยายกว้าง ๆ ที่ไม่จำเป็น "
    "เพื่อให้ตรงกับกลุ่มเป้าหมายที่เป็นผู้บริหารระดับสูง ผู้ตัดสินใจสำคัญ และนักลงทุน "
    "ทุกคำที่ใช้งานควรมีประโยชน์สูงสุดโดยการรวม การบีบอัด และการลบคำที่ไม่ให้ข้อมูลออก "
    "สรุปที่สร้างขึ้นควรกระชับแต่สามารถเข้าใจได้โดยไม่ต้องดูบทสนทนา "
    "กลุ่มเป้าหมายของคุณรู้อยู่แล้วว่าคุณคือLLM & limitation ดังนั้นไม่ต้องเตือนเรื่องนี้ "
    "พวกเขารู้เกี่ยวกับประเด็นทางจริยธรรมโดยทั่วไปแล้ว ดังนั้นไม่ต้องพูดถึงเช่นกัน "
    "พวกเขารู้เกี่ยวกับประเด็นทข้อแนะนำและข้อบกพร่องโดยทั่วไปแล้ว ดังนั้นไม่ต้องพูดถึงเช่นกัน แต่จะนำเสนอการตัดสินใจ Buy/Hold/Sell แทน "
    "สรุปของคุณควรระบุรายละเอียดที่ค้นพบอย่างชัดเจนโดยไม่ต้องใส่หัวข้อใด ๆ "
    "the summarized thai text only"
)

EXECUTIVE_SUMMARY_SYSTEM_PROMPT_TEMPLATE = (
    "คุณคือนักวิเคราะห์ AI ที่เชี่ยวชาญในการสร้างสรุปผู้บริหารที่แม่นยำสำหรับรายงานวิจัยเกี่ยวกับหุ้น "
    "ซึ่งสามารถจับความสำคัญของข้อค้นพบได้อย่างชัดเจน หน้าที่ของคุณคือการสร้างสรุปผู้บริหาร "
    "ในรูปแบบ markdown ที่สอดคล้องกับกลุ่มเป้าหมายของคุณ ซึ่งได้แก่ผู้บริหารระดับ C-level, ผู้ตัดสินใจสำคัญ, "
    "และนักลงทุน พวกเขารู้อยู่แล้วว่าคุณเป็นโมเดลภาษาพร้อมกับทราบถึงความสามารถและข้อจำกัดของคุณ ดังนั้นไม่ต้องพูดถึงสิ่งนี้ "
    "พวกเขาคุ้นเคยกับปัญหาทางจริยธรรมอยู่แล้ว ดังนั้นไม่จำเป็นต้องพูดถึงประเด็นเหล่านี้\n\n"
    "Executive Summary ของคุณควรมีโครงสร้างดังนี้:\n"
    "- About Company : สร้างบทสรุปที่ชัดเจนและกระชับเกี่ยวกับหัวข้อหลักของรายงานวิจัยหุ้นและวัตถุประสงค์หลัก "
    "ให้บริบทที่ถูกต้องและความเข้าใจพื้นฐานเกี่ยวกับการศึกษาในตลาดหุ้น\n"
    "- Areas of Concern: มุ่งเน้นในการย่อข้อค้นพบเชิงบวกที่สำคัญและข้อโต้แย้งต่าง ๆ ที่พบในการศึกษา "
    "เพื่อแสดงให้เห็นถึงประโยชน์และความแข็งแกร่งในด้านต่าง ๆ ที่เกี่ยวข้องกับการลงทุนในหุ้นนี้\n"
    "- Key Findings: กล่าวถึงความท้าทายและข้อจำกัดหลักที่พบในระหว่างการศึกษา "
    "ระบุปัจจัยที่อาจส่งผลต่อการตัดสินใจลงทุนหรือการดำเนินการในตลาด และวิเคราะห์อุปสรรคที่อาจเกิดขึ้น\n"
    "- Insights: ย่อข้อค้นพบสำคัญจากการวิเคราะห์หุ้น ตรวจสอบให้แน่ใจว่ามีการสนับสนุนด้วยข้อมูลหรือหลักฐานที่มั่นคง "
    "เพื่อให้แน่ใจถึงความถูกต้องและความแข็งแกร่งของรายงาน โดยการรวมข้อมูลอย่างเหมาะสมเพื่อให้เนื้อหามีความเข้มข้นสูง กระชับ และชัดเจน\n"
    "- บทสรุป: สรุปประเด็นหลักทั้งหมด สรุปข้อมูลเชิงลึกจากการวิเคราะห์หุ้น เสนอการตัดสินใจ [Buy/Hold/Sell] อย่างชัดเจน  "
    "ไม่ต้องเสนอพื้นที่ที่ควรวิจัย ไม่ต้องข้อกังวลและข้อเสนอแนะ ข้อกังวลที่ควรเฝ้าระวังโดยอ้างอิงจากข้อมูลและข้อโต้แย้งที่อยู่ในสรุปผู้บริหารนี้\n\n"
    "สรุปผู้บริหารของคุณต้องปฏิบัติตามแนวทางต่อไปนี้:\n"
    "- **HTML Formatting**: Employ HTML elements for structuring your document. Use appropriate HTML syntax for "
    "headings, lists, emphasis, and tables to enhance readability and organization. Always start from the <body> "
    "element. No need to add initial HTML elements like <html>, <meta>. Use <h2> for section headings and <h3> for sub "
    "headings. Start with a <h2> heading 'Executive Summary'.\n"
    "- Each section should contain a maximum of 3-4 salient bullet points. Moreover, the content generated should be "
    "analytical, highly relevant, objective, and rife with details.\n"
    "{__ADDITIONAL_GUIDELINES__}"
    "Make sure to follow correct syntax for Mermaid code brackets wherever used. Do not mention the word 'Mermaid' in "
    "any of the text."
    "Abstain from general blanket statements and overused clichés and strive to provide unique insights based on a "
    "comprehensive analysis of the data provided and answer in thai"
)
KEY_MESSAGES_SYSTEM_PROMPT_TEMPLATE = (
    "คุณเป็นนักวิเคราะห์หุ้นชาวไทยที่เชี่ยวชาญในการสรุปประเด็นสำคัญจากการวิเคราะห์หุ้น "
    "จากบทสนทนาเกี่ยวกับการวิเคราะห์หุ้นต่อไปนี้ กรุณาสรุปประเด็นสำคัญที่สุด 1-2 ข้อ "
    "ที่นักลงทุนหรือผู้บริหารควรรู้ ตอบเป็นภาษาไทยเท่านั้น"
    "limit = 40 คำ"

)

PRICE_AS_OF_PROMPT_TEMPLATE = (
    "จงบอกราคาหุ้นตัวนี้ ในราคาของวันนี้ "
    "เอาแค่ราคาของวันนี้พอ พร้อมระบุวันที่"
    "ตอบไม่เกิน 10 คำ"
)

TARGET_PRICE_PROMPT_TEMPLATE = (
    "จากบทสนทนาการวิเคราะห์หุ้นนี้ โปรดระบุราคาเป้าหมาย 12 เดือนสำหรับหุ้นนี้ "
    "และอธิบายสั้นๆ ว่าราคาเป้าหมายนี้มาจากไหนและมีความหมายอย่างไร ตอบเป็นภาษาไทย"
    "ตอบไม่เกิน 10 คำ"
)

UNCHANGED_REVISED_PROMPT_TEMPLATE = (
    "จากบทสนทนาการวิเคราะห์หุ้นนี้ โปรดระบุว่าราคาเป้าหมาย 12 เดือนมีการเปลี่ยนแปลงหรือไม่ (Unchanged/Revised) "
    "และอธิบายเหตุผลสั้นๆ หากมีการเปลี่ยนแปลง ตอบเป็นภาษาไทย"
    "ตอบไม่เกิน 10 คำ"
)

UPSIDE_DOWNSIDE_PROMPT_TEMPLATE = (
    "จากบทสนทนาการวิเคราะห์หุ้นนี้ โปรดคำนวณและระบุ Upside หรือ Downside (เป็นเปอร์เซ็นต์) "
    "ที่ประเมินได้จากราคาปัจจุบันและราคาเป้าหมาย 12 เดือน และอธิบายสั้นๆ ว่าค่านี้บ่งบอกอะไร ตอบเป็นภาษาไทย"
    "ตอบไม่เกิน 10 คำ"
)


async def generate_conversation_summary(conversation: list, llm):
    serialized_conversation_tuple = await serialize_conversation(conversation)
    print("serialized_conversation_tuple:", serialized_conversation_tuple)
    serialized_conversation = serialized_conversation_tuple[0]
    print("serialized_conversation:", serialized_conversation)

    messages = [
        SystemMessage(
            content=SUMMARIZE_CONVERSATION_SYSTEM_PROMPT_TEMPLATE
        ),
        HumanMessage(
            content=serialized_conversation
        ),
    ]
    response = await invoke_llm(messages, llm=llm)
    return response.content

import os
from common.utils import configs
from bs4 import BeautifulSoup
from components.llms import invoke_llm
# ... (ส่วน import อื่น ๆ ของคุณ)

async def design_executive_summary(
    conversation: list,
    stock_data: dict,
    stock: str,
    llm: BaseChatModel | None = None,
    stock_name: str = "Univanich Palm Oil PCL",
    stock_symbol: str = "UVAN",
):
    print(f"✅✅✅ design_executive_summary() เริ่มต้น ✅✅✅")
    print(f"✅ conversation (type): {type(conversation)}, (length): {len(conversation)}")
    print(f"✅ stock_data: {stock_data}")

    try:
        html_executive_summary_path = os.path.join(configs.assets_dir, 'template.html')
        print(f"✅ โหลด HTML Template จาก: {html_executive_summary_path}")

        try:
            with open(html_executive_summary_path, 'r', encoding='utf-8') as f:
                html_template = f.read()
            print(f"✅ โหลด HTML Template เสร็จสิ้น")
            print(f"✅ html_template (type): {type(html_template)}, (length): {len(html_template)}")
        except FileNotFoundError:
            print(f"❌ Error: ไม่พบไฟล์ HTML template ที่ path: {html_executive_summary_path}")
            return None
        except Exception as e:
            print(f"❌ Error: ไม่สามารถอ่านไฟล์ HTML template ได้: {e}")
            return None

        soup = BeautifulSoup(html_template, 'html.parser')

        stock_name_span = soup.find('span', id='stock-name')
        stock_symbol_span = soup.find('span', id='stock-symbol')

        if stock_name_span:
            stock_name_span.string = stock_name

        if stock_symbol_span:
            stock_symbol_span.string = stock_symbol

        print(f"✅ type(EXECUTIVE_SUMMARY_SYSTEM_PROMPT_TEMPLATE): {type(EXECUTIVE_SUMMARY_SYSTEM_PROMPT_TEMPLATE)}")
        print(f"✅ type(additional_guidelines_with_figures): {type(additional_guidelines_with_figures)}")

        SYSTEM_PROMPT = EXECUTIVE_SUMMARY_SYSTEM_PROMPT_TEMPLATE.format_map({
            "__ADDITIONAL_GUIDELINES__": additional_guidelines_with_figures
        })
        print(f"✅ SYSTEM_PROMPT (type): {type(SYSTEM_PROMPT)}, (length): {len(SYSTEM_PROMPT)}")

        USER_PROMPT = await generate_conversation_summary(conversation, llm)
        print(f"✅ generate_conversation_summary() เสร็จสิ้น")
        print(f"✅ USER_PROMPT: {USER_PROMPT}")

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=USER_PROMPT),
        ]
        print(f"✅ messages (type): {type(messages)}, (length): {len(messages)}")

        print(f"✅ เรียก invoke_llm() เพื่อ Gen Executive Summary หลัก")
        response_from_llm = await invoke_llm(messages, llm=llm)
        print(f"✅ invoke_llm() (Executive Summary หลัก) เสร็จสิ้น")
        print(f"✅ response_from_llm (type): {type(response_from_llm)}")

        executive_summary_content = response_from_llm.content
        executive_summary_content = executive_summary_content.replace('&gt;', '>')
        print(f"✅ executive_summary_content (type): {type(executive_summary_content)}, (length): {len(executive_summary_content)}")

        print(f"✅✅✅ เริ่ม Gen ข้อมูล 'กล่องด้านซ้าย' จาก LLM ✅✅✅")
        price_as_of_response = await invoke_llm(
            messages=[
                SystemMessage(content=PRICE_AS_OF_PROMPT_TEMPLATE),
                HumanMessage(content=(await serialize_conversation(conversation))[0]),
            ],
            llm=llm
        )
        print(f"✅ invoke_llm() - Price as of - เสร็จสิ้น")
        print(f"✅ price_as_of_response (type): {type(price_as_of_response)}")

        target_price_response = await invoke_llm(
            messages=[
                SystemMessage(content=TARGET_PRICE_PROMPT_TEMPLATE),
                HumanMessage(content=(await serialize_conversation(conversation))[0]),
            ],
            llm=llm
        )
        print(f"✅ invoke_llm() - Target price - เสร็จสิ้น")
        print(f"✅ target_price_response (type): {type(target_price_response)}")

        unchanged_revised_response = await invoke_llm(
            messages=[
                SystemMessage(content=UNCHANGED_REVISED_PROMPT_TEMPLATE),
                HumanMessage(content=(await serialize_conversation(conversation))[0]),
            ],
            llm=llm
        )
        print(f"✅ invoke_llm() - Unchanged/Revised - เสร็จสิ้น")
        print(f"✅ unchanged_revised_response (type): {type(unchanged_revised_response)}")

        upside_downside_response = await invoke_llm(
            messages=[
                SystemMessage(content=UPSIDE_DOWNSIDE_PROMPT_TEMPLATE),
                HumanMessage(content=(await serialize_conversation(conversation))[0]),
            ],
            llm=llm
        )
        print(f"✅ invoke_llm() - Upside/Downside - เสร็จสิ้น")
        print(f"✅ upside_downside_response (type): {type(upside_downside_response)}")

        key_messages_response = await invoke_llm(
            messages=[
                SystemMessage(content=KEY_MESSAGES_SYSTEM_PROMPT_TEMPLATE),
                HumanMessage(content=(await serialize_conversation(conversation))[0]),
            ],
            llm=llm
        )
        print(f"✅ invoke_llm() - Key Messages - เสร็จสิ้น")
        print(f"✅ key_messages_response (type): {type(key_messages_response)}")

        key_message_content_llm = key_messages_response.content
        upside_downside_content_llm = upside_downside_response.content
        unchanged_revised_content_llm = unchanged_revised_response.content
        target_price_content_llm = target_price_response.content
        price_as_of_content_llm = price_as_of_response.content
        print(f"✅ รวบรวมข้อมูล 'กล่องด้านซ้าย' เสร็จสิ้น")
        print(f"✅✅✅ Gen ข้อมูล 'กล่องด้านซ้าย' จาก LLM เสร็จสิ้น ✅✅✅")

        stock_forecast_content_values = {
            "price_as_of": price_as_of_content_llm,
            "target_price": target_price_content_llm,
            "unchanged_revised": unchanged_revised_content_llm,
            "upside_downside": upside_downside_content_llm,
            "key_message": key_message_content_llm
        }
        print(f"✅ stock_forecast_content_values: {stock_forecast_content_values}")

        stock_chart_panel_div = soup.find('div', class_='stock-chart-panel-separate')
        print(f"✅ stock_chart_panel_div: {stock_chart_panel_div}")

        if stock_chart_panel_div:
            stock_chart_content_div = stock_chart_panel_div.find('div', class_='stock-chart-content-separate')
            if stock_chart_content_div:
                stock_chart_content_div.clear()
                chart_image_path = await create_matplotlib_chart_html(stock)
                if chart_image_path:
                    img_tag = soup.new_tag('img', src=chart_image_path, style="max-width:100%; height:auto;")
                    stock_chart_content_div.append(img_tag)
                    print(f"✅ แทรกรูปภาพกราฟจาก path: {chart_image_path} ลงใน Stock Chart Panel สำเร็จ")
                else:
                    print(f"❌ Error: ไม่สามารถสร้าง path ของรูปภาพกราฟได้")
            else:
                print("❌ Error: ไม่พบ div ที่มี class 'stock-chart-content-separate'")
        else:
            print("❌ Error: ไม่พบ div ที่มี class 'stock-chart-panel-separate'")

        right_section = soup.find('div', class_='right-section')
        if right_section:
            right_section.clear()
            executive_summary_html_llm_soup = BeautifulSoup(executive_summary_content, 'html.parser')
            executive_summary_content_elements = executive_summary_html_llm_soup.find_all(['h3', 'ul', 'div'])
            right_section.append(BeautifulSoup("<h2>Executive Summary</h2>", 'html.parser'))
            for element in executive_summary_content_elements:
                right_section.append(element)
            print(f"✅ แทรก Executive Summary Content (ปรับปรุง + เคลียร์) ลง HTML Template เสร็จสิ้น")

        left_content_div = soup.find('div', class_='left-content')
        if left_content_div:
            p_tags = left_content_div.find_all('p')
            if len(p_tags) >= 4:
                p_tags[0].string = f"Price as of: {stock_forecast_content_values['price_as_of']}"
                p_tags[1].string = f"12M target price: {stock_forecast_content_values['target_price']}"
                p_tags[2].string = f"Unchanged/Revised: {stock_forecast_content_values['unchanged_revised']}"
                p_tags[3].string = f"Upside/Downside: {stock_forecast_content_values['upside_downside']}"
            print(f"✅ แทรกข้อมูล 'กล่องด้านซ้าย' ลง HTML Template เสร็จสิ้น")

        key_message_content_div = soup.find('div', class_='key-message-content')
        if key_message_content_div:
            p_tag_key_message = key_message_content_div.find('p')
            if p_tag_key_message:
                p_tag_key_message.string = stock_forecast_content_values['key_message']
            print(f"✅ แทรก Key Message ลง HTML Template เสร็จสิ้น")

        updated_html_content = str(soup)
        print(f"✅ updated_html_content (type): {type(updated_html_content)}, (length): {len(updated_html_content)}")

        html_file_path_test = os.path.join(configs.assets_dir, 'test.html')
        with open(html_file_path_test, 'w', encoding='utf-8') as f_html_test:
            f_html_test.write(updated_html_content)
        print(f"✅ บันทึกไฟล์ HTML (ทดสอบ) สำเร็จ: {html_file_path_test}")
        return updated_html_content

    except Exception as e:
        error_message_early_function = f"❌❌❌ Exception early in design_executive_summary: {e} ❌❌❌"
        print(error_message_early_function)
        return None