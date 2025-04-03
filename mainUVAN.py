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


stock_data_real = {}
sheet0 = pd.read_csv('UVAN4.csv')
sheet = pd.read_csv('UVAN.csv')
sheet2 = pd.read_csv('ROEROAUVAN.csv')

news= """
With reference to the Univanich Palm Oil Public Company Limited Board of Directors meeting No.
1/2025 held on 28th February 2025, the Board has made key decisions concerning agenda of the 2025
Annual General Meeting of shareholders as follows:

1. Approved to convene the 2025 AGM. The AGM will be held on 25th April 2025 at 09.00 hrs. at
Pinnacle 1-2 room, 4th Floor, Intercontinental Hotel, No. 973 Ploenchit Road, Lumpini, Pathumwan,
Bangkok 10330.

2. To fix record date for shareholders to be entitled to attend the Annual General Meeting of
Shareholders has been set as 14th March 2025.

3. Approved the final dividend payment against the 2024 performance outcomes at Baht 0.60 per
share. The Record Date for the right to receive dividend on 14th March 2025, and the dividend
payment is proposed to be made by 23th May 2025.

Feb 28 (Reuters) - Univanich Palm Oil PCL ::FY SALES OF GOODS 13.55 BILLION BAHT.PROFIT ATTRIBUTABLE FOR THE YEAR 1.27 BILLION BAHT.Further company coverage: UVAN.BK.
Mar 21 2025, 16:40 GMT+7 price UVAN.BK is 9.15 THB
Open
9.20
Prev. Close
9.20
Bid / Ask
 9.15 / 9.20
VWAP
9.1745
Turnover
THB
2.04M
Volume
222,400
YTD
0.55%
Beta (5Y Monthly)
0.40
* Default Market Share Type = Listed
THB
8.61B
PE (LTM)
6.78
Div Yield
10.93%
"""
if __name__ == '__main__':
    stock = "Univanich Palm Oil PCL"
    stock_symbol_main = 'UVAN'

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
        "content": f"คุณภาพทางการเงินของ {stock} เป็นอย่างไร โดยใช้ {sheet}, และ {sheet2} สรุปในแง่ของโครงสร้างสินทรัพย์และสุขภาพการเงิน ตอบเป็นภาษาไทย"
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
        "content": f"งบกำไรขาดทุนของ {stock} เป็นอย่างไร และมีความกังวลเกี่ยวกับรายได้และความสามารถในการทำกำไรหรือไม่ โดยใช้ {sheet}, และ {sheet2}ตอบเป็นภาษาไทย"
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
        "content": f"งบกระแสเงินสดของ {stock} สะท้อนถึงประสิทธิภาพในการดำเนินงานอย่างไรโดยใช้ {sheet0} ตอบเป็นภาษาไทย"
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


# async def main():
#     output_path_executive_summary_pdf = os.path.join(
#         configs.reports_dir, "ExecutiveSummary.pdf"
#     )  # ✅ Output path สำหรับ PDF

#     # ✅✅✅ เรียก design_executive_summary เพื่อสร้าง HTML
#     executive_summary_html = await design_executive_summary(
#         conversation,
#         stock_data_real,
#         stock=stock_symbol,
#         stock_name="Univanich Palm Oil PCL", # ส่งค่า stock_name
#         stock_symbol="UVAN", # ส่งค่า stock_symbol
#     )

#     if executive_summary_html:  # ✅ ตรวจสอบว่ามี HTML content
#         # ✅ สร้างไฟล์ HTML ชั่วคราว
#         with tempfile.NamedTemporaryFile(
#             suffix=".html", delete=False, mode="w", encoding="utf-8"
#         ) as temp_file:
#             temp_file.write(executive_summary_html)
#             temp_html_file_path = temp_file.name

#         # ✅ เรียก html_to_pdf เพื่อแปลง HTML เป็น PDF
#         await html_to_pdf(
#             html_file_executive_summary=temp_html_file_path,
#             html_file_content=None,  # ✅ หรือ path ของ default content ถ้าจำเป็น
#             html_file_title=None,    # ✅ ไม่ใช้ title
#             html_file_disclaimer=None, # ✅ ไม่ใช้ disclaimer
#             html_file_end=None,       # ✅ ไม่ใช้ end page
#             output_path=output_path_executive_summary_pdf,
#         )
#         print(
#             f"✅ Executive Summary PDF สร้างเสร็จ: {output_path_executive_summary_pdf}"
#         )
#     else:
#         print("❌ ไม่สามารถสร้าง Executive Summary HTML ได้")


# asyncio.run(main())
run_generation( 
         conversation=conversation,
         title_dict=title_dict,
         user_name="Dhouchdhanin Lee",
         llm=os.getenv('LLM', 'gpt'),
         stock_symbol=stock_symbol_main,
         apply_section_dedup=True,
         stock_data=stock_data_real
     )
    
    
#export OPENAI_API_KEY=