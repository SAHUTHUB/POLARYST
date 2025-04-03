import os
import asyncio
from tqdm import tqdm
from typing import List, Dict, Literal
from tenacity import retry, stop_after_attempt

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

logger = configs.logger




@retry(stop=stop_after_attempt(3))
async def generate_executive_summary_content(conversation: List[Dict], llm: str, stock_symbol: str, stock_data: str): # ✅ [แก้ไข] เปลี่ยน parameter แรกเป็น conversation: List[Dict]
    executive_summary_html = await design_executive_summary(conversation=conversation, stock_data=stock_data, stock=stock_symbol, llm=llm) # ✅ [แก้ไข] ส่ง conversation ตรงๆ
    return executive_summary_html

@retry(stop=stop_after_attempt(3))
async def generate_section_content(serialized_conversation: str, section: Dict, previous_text: str,
                                   llm: str, apply_dedup: bool = False) -> (str, str):
    section_html = await design_section(serialized_conversation, section, previous_text, llm)
    if apply_dedup:
        section_html = await deduplicate_section(section_html, previous_text, llm)
    return extract_html_body_content(section_html)


async def generate_report(conversation: List[Dict],serialized_conversation: str, report_skeleton: List[Dict], references: List[str],
                          llm: str, apply_section_dedup: bool, stock_symbol: str,stock_data) -> (str, str): # ✅ Correct: มี parameter 'stock_symbol'
    # Initialize lists to hold HTML and text sections of the report
    html_sections, text_sections = [], []

    html_executive_summary = await generate_executive_summary_content(
        conversation=conversation, # ✅ [แก้ไข] ส่ง conversation ตรงๆ
        llm=llm, stock_symbol=stock_symbol, stock_data=stock_data) # ✅ [แก้ไข] ส่ง stock_symbol และ stock_data ให้ครบ

    # ...
   

    for section in tqdm(report_skeleton, desc="Generating report..."):
        # Combine all previously generated text sections into one string
        previous_text = '\n'.join(text_sections)
        # Generate the content for the current section in both HTML and text formats
        html_section, text_section = await generate_section_content(
            serialized_conversation, section, previous_text, llm=llm, apply_dedup=apply_section_dedup
        )

        # Append the generated HTML and text content to their respective lists
        html_sections.append(html_section)
        text_sections.append(text_section)

    # Concatenate all HTML sections into a single HTML document
    html_report = '\n'.join(html_sections)

    # Compile the complete HTML report, incorporating references, and return it
    return await compile_full_html(
        html_content={"executive_summary": html_executive_summary, "report": html_report},
        references=references
    )
async def run_generation_async(conversation: List[Dict], title_dict: Dict[str, str], user_name: str, request_id: int,
                               llm: Literal['gpt', 'claude'] | None, apply_section_dedup: bool, stock_symbol: str,stock_data): # ✅ แก้ไข: เพิ่ม stock_symbol: str
    # Configure the llm to use
    match llm:
        case 'claude':
            llm_instance = anthropic[openai[os.getenv('CLAUDE_MODEL', 'claude-3-opus')]]
        case _:
            llm_model = os.getenv('GPT_MODEL', 'gpt-4o').strip("{}'")
            llm_instance = openai.get(llm_model, openai['gpt-4o'])
    logger.info(f"Using LLM: {llm}")

    # Serialize the input conversation and extract references
    serialized_conversation, references = await serialize_conversation(conversation)

    logger.info(f"Serialized input conversation. Now generating report skeleton...")
    # Design the report skeleton based on the serialized conversation
    report_skeleton = await design_report_skeleton(serialized_conversation, llm=llm_instance)
    logger.info(f"Report skeleton generated: {report_skeleton}\n\nNow generating report sections with `section_dedup` "
                f"set to {apply_section_dedup}...")

    # Generate the report sections based on the serialized conversation, report skeleton, and references
    html_executive_summary, html_report = await generate_report( # ✅ [แก้ไข] ส่ง conversation ให้ generate_report
    conversation=conversation, serialized_conversation=serialized_conversation, report_skeleton=report_skeleton, references=references, # ✅ [แก้ไข] ส่ง conversation
    llm=llm_instance, apply_section_dedup=apply_section_dedup, stock_symbol=stock_symbol, stock_data=stock_data) # ✅ [แก้ไข] เปลี่ยน llm_instance เป็น llm
    # Generate executive summary content, passing stock_symbol
   

    # Save the generated HTML executive summary & report
    for html_content, filename in zip([html_executive_summary, html_report], ["executive_summary.html", "index.html"]):
        html_filepath = os.path.join(configs.assets_dir, filename)
        with open(html_filepath, 'w', encoding='utf-8') as file:
            file.write(html_content)

    html_executive_summary_filepath = os.path.join(configs.assets_dir, 'executive_summary.html')
    html_report_filepath = os.path.join(configs.assets_dir, 'index.html')
    sanitized_title = sanitize_filename(title_dict["title"])
    # Define paths for the HTML title, temporary title for PDF conversion, and the final PDF report
    html_title_filepath = os.path.join(configs.assets_dir, 'title.html')
    html_temp_title_filepath = os.path.join(configs.assets_dir, 'temp_title.html')
    pdf_filepath = os.path.join(configs.reports_dir, f'{sanitized_title}.pdf')

    # Add title information to the HTML report
    await add_title_to_html(
        title_info=title_dict,
        user_name=user_name,
        html_title_path=html_title_filepath,
        output_path=html_temp_title_filepath
    )
    logger.info("HTML report successfully generated! Converting HTML to PDF file now!")

    # Convert the combined HTML content into a PDF report
    await html_to_pdf(
        html_file_executive_summary=html_executive_summary_filepath,
        html_file_content=html_report_filepath,
        html_file_title=html_temp_title_filepath,
        html_file_disclaimer=os.path.join(configs.assets_dir, 'disclaimer.html'),
        html_file_end=os.path.join(configs.assets_dir, 'end.html'),
        output_path=pdf_filepath
    )

    # Remove temporary HTML files used in the PDF conversion process
    for tbd_file in [html_executive_summary_filepath, html_report_filepath, html_temp_title_filepath]:
        os.remove(tbd_file)
    logger.info(f"PDF report on {title_dict['title']} generated and saved to {pdf_filepath}")


def run_generation(conversation: List[Dict], title_dict: Dict[str, str], user_name: str, request_id: int | None = None, # ✅ [คงเดิม] conversation รับ List[Dict]
                   llm: Literal['gpt', 'claude'] = 'gpt', apply_section_dedup: bool = True, stock_symbol: str = None, stock_data: str = None): # ✅ [คงเดิม] stock_symbol, stock_data
    asyncio.run(run_generation_async(conversation=conversation, title_dict=title_dict, user_name=user_name, request_id=request_id, llm=llm, apply_section_dedup=apply_section_dedup, stock_symbol=stock_symbol, stock_data=stock_data)) # ✅ [แก้ไข] ส่ง conversation ตรงๆ