import os
from report import run_generation
import pandas as pd
from components.llms import openai, anthropic
from components.convert import html_to_pdf
from components.deduplicate import deduplicate_section
import os
import asyncio
from tqdm import tqdm
from typing import List, Dict, Literal
from tenacity import retry, stop_after_attempt
import tempfile # ✅ Import tempfile เพื่อจัดการไฟล์ชั่วคราว
from common.utils import configs
from section import design_section
from skeleton import design_report_skeleton
from summary import design_executive_summary

from components.llms import openai, anthropic
from components.convert import html_to_pdf
from components.deduplicate import deduplicate_section
from components.functions import (
    serialize_conversation,
    sanitize_filename,
    extract_html_body_content,
    compile_full_html,
    add_title_to_html
)
from components.functions import (
    serialize_conversation,
    sanitize_filename,
    extract_html_body_content,
    compile_full_html,
    add_title_to_html
)
stock_data_real = {}
sheet0 = pd.read_csv('Delta.csv')
sheet = pd.read_csv('Delta2.csv')
sheet2 = pd.read_csv('DeltaROEROA.csv')

news= """Bangkok, Thailand, November 8, 2024 -Delta Electronics (Thailand) PCL., a global leader in power management and IoT-based smart green solutions has achieved a remarkable milestone by receiving an "Excellent" grade (5-star) on the Corporate Governance Report (CGR) from the Thai Institute of Directors Association (IOD) for the ninth consecutive year.

"This recognition is a testament to our unwavering dedication to corporate governance and responsible business practices." said Mr. Victor Cheng, Delta Thailand CEO, "We believe that governance excellence not only benefits our shareholders but also reinforces our role as a positive force for sustainable development. Our journey to consistently meet and exceed the highest governance standards reflects our commitment to transparency, stakeholder engagement, and sustainable growth."

The 2024 CGR survey, supported by the Stock Exchange of Thailand (SET), evaluated a total of 808 Thai listed companies across four key governance categories. Delta Thailand's scores across each category underline the company's commitment to transparency, equitable treatment, stakeholder engagement, and sustainable business practices:

Rights and Equitable Treatment of Shareholders:

Delta Thailand's commitment to shareholders was showcased through initiatives such as holding hybrid Annual General Meetings (AGMs) and training programs on conflict-of-interest prevention and insider information protection.

Role of Stakeholders and Business Sustainability:

Delta Thailand has actively prioritized sustainability, aligning its policies with environmental management and fair employee compensation practices while providing a platform for monitoring and addressing whistleblower concerns.

Disclosure and Transparency:

Delta Thailand's emphasis on ESG (Environmental, Social, Governance) transparency was reflected in the Management Discussion and Analysis (MD&A) reports, along with clear disclosures on business operations and competitive landscapes.

Board Responsibility:

Delta Thailand's Board demonstrates diversity and independence, with board members actively engaged in specialized training to enhance their expertise and drive corporate excellence.

The CGR study, which aligns with international best practices and Thailand's Corporate Governance Code, serves as an essential tool for Thai listed companies to benchmark and improve corporate governance practices. It also provides critical insights for regulators, investors, and other stakeholders, enhancing confidence and promoting a more transparent investment environment.

With this achievement, Delta Electronics Thailand continues to lead by example, fostering a robust culture of transparency, ethical practices, and corporate responsibility, ensuring value creation for all stakeholders and sustained contribution to Thailand's economic development.

Delta Electronics (Thailand) pcl published this content on November 08, 2024.

Jakarta Indonesia, November 7, 2024 - Delta Electronics, a global leader in power management and IoT-based smart green solutions, announced today its business expansion in Indonesia. Building on its strong partnerships with local distributors and system integrators, PT Delta Electronics Indonesia will continue collaboration with these partners while extending its engagement with government agencies and key customers. Delta aims to provide tailored solutions that address the unique needs of key Indonesian industries, including Data Centers, Manufacturing and Renewable Energy, with a focus on driving sustainable innovation.

"At PT Delta Electronics Indonesia, we are committed to being at the forefront of innovative power electronics technologies and solutions. Our ongoing investment in research and development has enabled us to consistently introduce advanced products that enhance energy efficiency and minimize our customers' carbon footprints. This evolution reflects our dedication to not only providing solutions but also being a reliable partner to foster sustainability in Indonesia." remarked Mr. Johnny Tam, Country Manager, PT Delta Electronics Indonesia.

"Delta Electronics has transformed significantly in Indonesia since its first entry into the market over twenty years ago as a Telecom supplier into a significant player in Data Center, Automation and Energy Infrastructure spaces. This transition reflects our vision of innovation and commitment to local markets, all while maintaining a strong emphasis on energy efficiency and sustainable technologies." said Mr. David Leal, Vice-President, SEA Business, Delta Electronics.

Focusing on Innovative Solutions in Power Electronics, Automation, and Energy Infrastructure to Support Sustainable Development

By establishing PT Delta Electronics Indonesia, the company strengthens its local presence and engagement with Indonesian industries, delivering faster, tailored solutions to meet the unique challenges of industrialization and urbanization.

Delta is advancing Indonesia's EV ecosystem through strategic partnerships with local players. Notably, PT Delta Electronics implemented EV chargers for the 2022 G20 Bali Summit, supporting e-mobility for world leaders at the event. At the 43rd ASEAN Summit in Jakarta, the company also deployed chargers to facilitate transportation for regional leaders. Furthermore, PT Delta Indonesia signed an MOU with an Indonesian consumer electronics factory to increase accessibility of Delta's reliable, energy-efficient solutions to Indonesian customers.

PT Delta Electronics Indonesia will drive sustainability in smart cities, data centers, automation, and energy infrastructure by collaborating closely with private and government sectors. Beyond technology solutions, the company remains committed to community engagement, environmental awareness, and Indonesia's long-term sustainable development goals, underscoring its dedication to a smarter, more sustainable future.

ALEXANDRIA, Va: United States Patent and Trademark Office has published on October 31, 2024, an application no. 20240363283 for the registration of US patent by Delta Electronics (Thailand) Public Company Limited for "POWER MODULE AND POWER CIRCUIT".Inventors: JIN; FengCAI; LeiDONG; KaiKE; Zhong-WeiApplicant: Delta Electronics (Thailand) Public Company Limited Samutprakarn THApplication filing date: 2024-07-05According to the abstract released by the U.S. Patent & Trademark Office: "Power module includes transformer unit including primary and secondary windings and magnetic core; parallely connected first and second capacitor units coupled to first terminal of primary winding of transformer unit through first node; first and second external pins respectively coupled to first terminal of first capacitor unit and second terminal of second capacitor unit; first and second switch units coupled to second terminal of primary winding of transformer unit thorough second node; third and fourth external pins respectively coupled to first terminal of first switch unit and second terminal of second switch unit; secondary-side circuit coupled to secondary winding; and fifth and sixth external pins electrically coupled to first and second output terminals of secondary-side circuit, respectively. First external pin is coupled to one of third and fourth external pins selectively."

ALEXANDRIA, Va: United States Patent and Trademark Office has published on October 31, 2024, an application no. 20240364146 for the registration of US patent by Delta Electronics (Thailand) Public Co., Ltd. for "WIRELESS POWER TRANSMISSION SYSTEM".Inventors: RICHTER; Ulrich ENDERLIN; JonasApplicant: Delta Electronics (Thailand) Public Co., Ltd. THApplication filing date: 2024-04-16According to the abstract released by the U.S. Patent & Trademark Office: "The present disclosure concerns a wireless power transmission system, comprising a primary unit including a primary pad for wireless power transmission and a primary wireless communication unit; a secondary unit including a secondary pad for wireless power reception and a secondary wireless communication unit; and a control unit; wherein the primary pad and the secondary pad are configured to wirelessly transfer power via inductive coupling, wherein the primary and secondary wireless communication units are configured to transmit and receive a communication signal, and wherein the control unit is configured to detect a relative position of the primary wireless communication unit and the secondary wireless communication unit using the communication signal."
Oct 25 (Reuters) - Delta Electronics Thailand PCL DELTA.BK:
DELTA ELECTRONICS THAILAND PCL - PURCHASE OF NEW MACHINES FOR 835.01 MILLION BAHT


"""
if __name__ == '__main__':
    stock = "DELTA.BK"
    stock_symbol_main = 'DELTA'

    conversation = [
    {
        "role": "user",
        "content": f"คุณเป็นนักวิเคราะห์ชาวไทยและคุณกำลังเขียนรายงานวิเคราะห์ในภาษาไทย อัปเดตข่าวของ {stock} พร้อมกับ {news} โดยใช้ {sheet},{sheet0} และ {sheet2} สรุป และตอบกลับเป็นภาษาไทย"
    },
    {
        "role": "assistant",
        "content": f"ภาพรวมทางการเงิน:\nรายได้: 105 ล้านดอลลาร์ (+55% YoY) ใกล้เคียงกับสถิติสูงสุดที่ 106 ล้านดอลลาร์ในไตรมาสที่ผ่านมา\nกำไรขั้นต้น:\nค่าใช้จ่ายในการดำเนินงาน: 79.9 ล้านดอลลาร์ (GAAP), 68.7 ล้านดอลลาร์ (ไม่ใช่ GAAP)\nสถานะเงินสด: 508 ล้านดอลลาร์\nความสำเร็จในการดำเนินงาน:\nการอัปเดตเชิงกลยุทธ์และโปรแกรม:\nสรุปในไตรมาสนี้"
    },
    {
        "role": "user",
        "content": f"คุณภาพทางการเงินของ {stock} เป็นอย่างไร โดยใช้ {sheet},{sheet0} และ {sheet2} สรุปในแง่ของโครงสร้างสินทรัพย์และสุขภาพการเงิน ตอบเป็นภาษาไทย"
    },
    {
        "role": "assistant",
        "content": f"### การวิเคราะห์คุณภาพทางการเงินของ {stock}\n\n#### การวิเคราะห์โครงสร้างสินทรัพย์\n\n1. **สินทรัพย์หมุนเวียนเทียบกับสินทรัพย์ไม่หมุนเวียน**\n    - **สินทรัพย์หมุนเวียนเด่น**: หาก {stock} มีสัดส่วนของสินทรัพย์หมุนเวียนสูงกว่า ควรเน้นที่การวิเคราะห์สภาพคล่อง สินทรัพย์เหล่านี้ประกอบด้วยเงินสด ลูกหนี้การค้า และสินค้าคงคลัง อัตราส่วนสภาพคล่องควรสะท้อนถึงความสามารถของบริษัทในการครอบคลุมหนี้สินระยะสั้นได้อย่างสบาย"
    },
    {
        "role": "assistant",
        "content": f"   - **สินทรัพย์ไม่หมุนเวียนเด่น**: หากมีสัดส่วนของสินทรัพย์ไม่หมุนเวียนสูง เช่น ที่ดิน อาคาร และอุปกรณ์ จำเป็นต้องวิเคราะห์ว่าสินทรัพย์เหล่านี้สามารถสร้างรายได้ได้อย่างมีประสิทธิภาพหรือไม่ (เช่น การวิเคราะห์ ROA)"
    },
    {
        "role": "assistant",
        "content": f"2. **การวิเคราะห์รายละเอียดสินทรัพย์**\n    - **องค์ประกอบของสินทรัพย์หมุนเวียน**: สินทรัพย์หมุนเวียนควรประกอบด้วยเงินสด ลูกหนี้การค้า และสินค้าคงคลัง หากมี 'สินทรัพย์หมุนเวียนอื่นๆ' มากเกินไป อาจส่งสัญญาณปัญหาสภาพคล่อง"
    },
    {
        "role": "assistant",
        "content": f"   - **ลูกหนี้การค้า**: หากการเติบโตของลูกหนี้การค้ามากกว่าการเติบโตของยอดขายอย่างมาก อาจเป็นปัญหาเกี่ยวกับการเก็บหนี้หรืออาจเกิดจากการเพิ่มรายได้ที่เกินจริง\n    - **สินค้าคงคลัง**: หากการเติบโตของสินค้าคงคลังมากกว่าการเติบโตของต้นทุนขาย อาจแสดงถึงความเสื่อมสภาพหรือความไม่ประสิทธิภาพในการจัดการสินค้าคงคลัง"
    },
    {
        "role": "assistant",
        "content": f"   - **สินทรัพย์ไม่มีตัวตน**: สัดส่วนสินทรัพย์ไม่มีตัวตนที่สูงเมื่อเทียบกับสินทรัพย์ทั้งหมด อาจบ่งบอกถึงการซื้อกิจการที่มีราคาสูง ทำให้เกิดความกังวลเกี่ยวกับความยั่งยืนของผลตอบแทนจากสินทรัพย์ (ROA)\n    - **สินทรัพย์ถาวรเทียบกับการเติบโตของรายได้**: การเพิ่มขึ้นของสินทรัพย์ถาวร เช่น ที่ดิน อาคาร และอุปกรณ์ ควรจะสัมพันธ์กับการเติบโตของรายได้ เพื่อแสดงถึงการใช้การลงทุนอย่างมีประสิทธิภาพในการเติบโต"
    },
    {
        "role": "user",
        "content": f"งบกำไรขาดทุนของ {stock} เป็นอย่างไร และมีความกังวลเกี่ยวกับรายได้และความสามารถในการทำกำไรหรือไม่ โดยใช้ {sheet},{sheet0} และ {sheet2}ตอบเป็นภาษาไทย"
    },
    {
        "role": "assistant",
        "content": f"### การวิเคราะห์งบกำไรขาดทุนของ {stock}\n\n#### ภาพรวมรายได้และความสามารถในการทำกำไร\n\n1. **แนวโน้มรายได้และกำไรสุทธิ**\n    - **การเติบโตอย่างต่อเนื่อง**: รายได้และกำไรสุทธิควรแสดงการเติบโตอย่างต่อเนื่องในช่วงหลายปีที่ผ่านมา การเพิ่มขึ้นของอัตรากำไรขั้นต้น อัตรากำไร EBIT และอัตรากำไรสุทธิบ่งบอกถึงการควบคุมต้นทุนอย่างมีประสิทธิภาพและความสามารถในการตั้งราคาที่แข็งแกร่ง\n    - **ความกังวลเกี่ยวกับการลดลงของอัตรากำไร**:\n      - **อัตรากำไรขั้นต้นลดลง**: อาจเกิดจากต้นทุนที่สูงขึ้น การผลิตที่ไม่เหมาะสม หรือการแข่งขันด้านราคา\n      - **อัตรากำไร EBIT ลดลง**: แสดงถึงค่าใช้จ่ายในการดำเนินงานที่เพิ่มขึ้นหรือลดลงของความสามารถในการตั้งราคา"
    },
    {
        "role": "assistant",
        "content": f"2. **การวิเคราะห์กำไรโดยละเอียด**\n    - **ความสม่ำเสมอของอัตรากำไรขั้นต้น**: อัตรากำไรขั้นต้นที่มีความสม่ำเสมอในหลายปีแสดงถึงการจัดการต้นทุนอย่างมีประสิทธิภาพ\n    - **ค่าใช้จ่ายในการขาย**: ควรเติบโตสอดคล้องกับรายได้ แสดงถึงการใช้การลงทุนในการตลาดและการขายอย่างมีประสิทธิภาพ\n    - **ค่าใช้จ่ายในการบริหาร**: เช่นเดียวกับค่าใช้จ่ายในการขาย การเติบโตควรสอดคล้องกับการเพิ่มของรายได้\n    - **ต้นทุนทางการเงิน**: หากต้นทุนทางการเงินเกินกว่า 50% ของ EBIT อาจบ่งบอกถึงการใช้เงินกู้มากเกินไปหรือการขยายธุรกิจในระยะเริ่มต้นที่มีต้นทุนสูง"
    },
    {
        "role": "assistant",
        "content": f"2. **การเพิ่มขึ้นของสินค้าคงคลังและลูกหนี้การค้า**: การเติบโตของสินค้าคงคลังและลูกหนี้การค้ามากกว่าการเติบโตของรายได้อาจบ่งบอกถึงความไม่ประสิทธิภาพในการผลิตหรือการเรียกเก็บหนี้"
    },
    {
        "role": "assistant",
        "content": f"#### สรุป\nการวิเคราะห์งบกำไรขาดทุนบ่งบอกว่า {stock}  โครงสร้างรายได้และต้นทุนได้อย่างไร ความสามารถในการทำกำไรของบริษัท [คงที่/ดีขึ้น/ลดลง] และประเด็นเฉพาะเช่น [ต้นทุนทางการเงินที่เพิ่มขึ้น/อัตรากำไรขั้นต้นที่ลดลง] "
    },
    {
        "role": "user",
        "content": f"งบกระแสเงินสดของ {stock} สะท้อนถึงประสิทธิภาพในการดำเนินงานอย่างไรโดยใช้ {sheet} ตอบเป็นภาษาไทย"
    },
    {
        "role": "assistant",
        "content": f"### การวิเคราะห์งบกระแสเงินสดของ {stock}\n\n#### กระแสเงินสดจากการดำเนินงาน\n1. **กระแสเงินสดจากการดำเนินงานเป็นบวก**: กระแสเงินสดจากการดำเนินงานเป็นบวกบ่งบอกว่า {stock} สามารถสร้างกระแสเงินสดได้เพียงพอจากกิจกรรมหลักในการดำเนินธุรกิจ สามารถนำเงินสดไปใช้ลงทุนต่อหรือชำระหนี้ได้\n2. **กระแสเงินสดจากการดำเนินงานเทียบกับกำไรสุทธิ**:\n    - **สัญญาณเตือน**: หากกระแสเงินสดจากการดำเนินงานต่ำกว่ากำไรสุทธิเสมอ อาจบ่งบอกถึงปัญหาการเพิ่มรายได้เกินจริง การเพิ่มขึ้นของลูกหนี้ หรือการมีสินค้าคงคลังมากเกินไป"
    },
    {
        "role": "assistant",
        "content": f"#### กระแสเงินสดจากกิจกรรมการลงทุน\n1. **การลงทุนในสินทรัพย์ถาวร**: การลงทุนที่สำคัญในสินทรัพย์ถาวร (เช่น ที่ดิน อาคาร และอุปกรณ์) ควรสอดคล้องกับการเติบโตของรายได้ เพื่อแสดงถึงการขยายกำลังการผลิตอย่างมีประสิทธิภาพ\n2. **สัญญาณเตือน**: หากกระแสเงินสดที่ใช้ในการลงทุนสูงกว่าค่าเสื่อมราคาอย่างมาก อาจหมายถึงการลงทุนมากเกินไปหรือการจัดสรรเงินทุนที่ไม่เหมาะสม"
    },
    {
        "role": "assistant",
        "content": f"#### กระแสเงินสดจากกิจกรรมการจัดหาเงิน\n1. **การชำระหนี้เทียบกับการกู้ยืมใหม่**: การทำความเข้าใจว่ามีเงินสดที่ใช้ในการชำระหนี้เทียบกับการกู้ยืมใหม่มากน้อยแค่ไหน สามารถบอกได้ว่า {stock} บริหารการกู้ยืมได้อย่างมีประสิทธิภาพหรือไม่"
    },
    {
        "role": "assistant",
        "content": f"#### สรุป\n{stock} มีกระแสเงินสด [แข็งแกร่ง/อ่อนแอ] โดยกระแสเงินสดจากการดำเนินงาน [สอดคล้องกับ/เกิน/น้อยกว่า] กำไรสุทธิ กระแสเงินสดจากการลงทุนแสดงถึง [การเติบโตเชิงกลยุทธ์/การขยายตัวมากเกินไป] และกิจกรรมการจัดหาเงินบ่งชี้ถึง [การบริหารหนี้ที่เหมาะสม/ความกังวลเกี่ยวกับการกู้ยืมที่เพิ่มขึ้น]"
    },
    {
        "role": "user",
        "content": "วิเคราะห์ปัญหาธุรกิจผ่านอัตราส่วนทางการเงินของ {stock} สะท้อนถึงประสิทธิภาพในการดำเนินงานอย่างไรโดยใช้ {sheet2} ตอบเป็นภาษาไทย"
    },
        {
        "role": "assistant",
        "content": f"{stock} มี ROE ผลตอบแทนต่อส่วนของผู้ถือหุ้น ROE > 5 และสม่ำเสมอ แสดงว่าบริษัทสามารถสร้างผลตอบแทนให้กับผู้ถือหุ้นได้ดี \nผลตอบแทนต่อสินทรัพย์ ROA > 5 และสม่ำเสมอ แสดงว่าบริษัทสามารถนำสินทรัพย์ไปสร้างผลตอบแทนกำไรก่อนดอกเบี้ยและภาษีได้ดี \nบริษัทที่ ROA ลดลงต่อเนือ่งแสดงว่ามีปัญหาลงทุนแล้วไม่คุ้มค่าไม่สร้างผลตอบแทนกลับมา ผลประกอบการจะเริ่มโตช้าลงได้\nบริษัทที่อัตราส่วนหนี้สินต่อทุนมากกว่า 1.5 และ กระแสเงินสดจากกิจกรรมดำเนินงานติดลบ ให้ระมัดระวังปัญหาการจ่ายหนี้สิน\nบริษัทที่อัตราส่วนหมุนเวียนทรัพย์สิน asset turnover มีแนวโน้มลดลง อาจอยู่ในช่วงลงทุน สินทรัพย์เพิ่มแต่รายได้ไม่เพิ่มตาม"
    },

    ]


    title_dict = {
        "title": f"Stock Analysis Report for {stock}",
        "sub_title": "Evaluating Financial Quality, Profitability, Cash Flow, Growth Potential, and Valuation"
    }


async def main():
    output_path_executive_summary_pdf = os.path.join(
        configs.reports_dir, "ExecutiveSummary.pdf"
    )  # ✅ Output path สำหรับ PDF

    # ✅✅✅ เรียก design_executive_summary เพื่อสร้าง HTML
    executive_summary_html = await design_executive_summary(
        conversation,
        stock_data_real,
        stock=stock_symbol_main,
        stock_name=stock, # ส่งค่า stock_name
        stock_symbol=stock_symbol_main, # ส่งค่า stock_symbol
    )

    if executive_summary_html:  # ✅ ตรวจสอบว่ามี HTML content
        # ✅ สร้างไฟล์ HTML ชั่วคราว
        with tempfile.NamedTemporaryFile(
            suffix=".html", delete=False, mode="w", encoding="utf-8"
        ) as temp_file:
            temp_file.write(executive_summary_html)
            temp_html_file_path = temp_file.name

        # ✅ เรียก html_to_pdf เพื่อแปลง HTML เป็น PDF
        await html_to_pdf(
            html_file_executive_summary=temp_html_file_path,
            html_file_content=None,  # ✅ หรือ path ของ default content ถ้าจำเป็น
            html_file_title=None,    # ✅ ไม่ใช้ title
            html_file_disclaimer=None, # ✅ ไม่ใช้ disclaimer
            html_file_end=None,       # ✅ ไม่ใช้ end page
            output_path=output_path_executive_summary_pdf,
        )
        print(
            f"✅ Executive Summary PDF สร้างเสร็จ: {output_path_executive_summary_pdf}"
        )
    else:
        print("❌ ไม่สามารถสร้าง Executive Summary HTML ได้")


asyncio.run(main())
# run_generation( 
#          conversation=conversation,
#          title_dict=title_dict,
#          user_name="Dhouchdhanin Lee",
#          llm=os.getenv('LLM', 'gpt'),
#          stock_symbol=stock_symbol,
#          apply_section_dedup=True,
#          stock_data=stock_data_real
#      )
    
    
#export OPENAI_API_KEY="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"