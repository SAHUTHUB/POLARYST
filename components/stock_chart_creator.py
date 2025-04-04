from tvDatafeed import Interval, TvDatafeed
import mplfinance as mpf
import pandas as pd
import os  # Import os module

def create_stock_chart(data: pd.DataFrame, symbol: str, chart_type: str = 'candle', volume: bool = True, moving_averages: tuple = (), indicators: tuple = (), chart_style: str = 'yahoo', output_path: str = 'stock_chart.png'):
    """
    สร้างกราฟหุ้นประเภทต่างๆ ด้วย mplfinance และบันทึกเป็นไฟล์รูปภาพ

    Args:
        data (pd.DataFrame): DataFrame ที่มีข้อมูลราคาหุ้น OHLCV
        symbol (str): ชื่อหุ้น  ✅ ใช้ตัวแปร symbol ที่เป็น argument
        chart_type (str): ประเภทของกราฟหุ้น
        volume (bool): แสดงกราฟ Volume หรือไม่
        moving_averages (tuple): เส้นค่าเฉลี่ยเคลื่อนที่
        indicators (tuple): อินดิเคเตอร์ทางเทคนิค (ยังไม่รองรับ)
        chart_style (str): สไตล์ของกราฟ
        output_path (str): path สำหรับบันทึกไฟล์รูปภาพ

    Returns:
        str: path ของไฟล์รูปภาพที่บันทึกสำเร็จ
             หรือ None หากเกิดข้อผิดพลาด
    """

    # ... (ส่วนตรวจสอบคอลัมน์ และ set index เหมือนเดิม) ...

    # สร้าง Moving Averages keyword arguments
    mav_kwargs = {}
    if moving_averages:
        mav_kwargs['mav'] = moving_averages

    try:
        # บันทึกกราฟเป็นไฟล์ PNG โดยใช้ savefig argument
        mpf.plot(data,
                 type=chart_type,
                 volume=volume,
                 title=f'{symbol} 14-day historical price chart', # ✅ ใช้ตัวแปร symbol ใน title
                 style=chart_style,
                 **mav_kwargs,
                 savefig=dict(fname=output_path) # เพิ่ม savefig เพื่อบันทึกไฟล์ PNG ตาม output_path
                 )
        return output_path # return path ของไฟล์ที่บันทึกสำเร็จ

    except Exception as e:
        print(f"Error creating and saving chart: {e}")
        return None # return None เมื่อเกิด error

