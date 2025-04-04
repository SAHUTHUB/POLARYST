import base64
import os
import pandas as pd
import matplotlib.pyplot as plt
from common.utils import configs
from tvDatafeed import TvDatafeed, Interval
from components.stock_chart_creator import create_stock_chart  # ✅ Import ฟังก์ชัน create_stock_chart จากไฟล์ใหม่

async def create_matplotlib_chart_html(stock_symbol): # ✅ รับ argument stock_symbol
    print(f"✅ create_matplotlib_chart_html() เริ่มต้น: stock_symbol = {stock_symbol}") # ✅ Print: เริ่มต้นฟังก์ชัน + stock symbol
    try:
        tv = TvDatafeed(username='sahut_chensirasoorath', password='SahutChensirasoorath22!') # ⚠️ แก้ตรงนี้ ใส่ username password ของคุณ
        print(f"✅ TvDatafeed() instance สร้างสำเร็จ") # ✅ Print: TvDatafeed instance สร้างสำเร็จ
        data = tv.get_hist(symbol=stock_symbol, exchange='SET', interval=Interval.in_daily, n_bars=30) # ✅ เปลี่ยนเป็น keyword argument 'symbol' ที่ถูกต้อง
        if data is None:
            print(f"❌ Error: TvDatafeed().get_hist() returns None for stock: {stock_symbol}") # ✅ Print: get_hist() คืนค่า None
            return ""  # หรือ return error HTML message
        df = pd.DataFrame(data)
        print(f"✅ DataFrame สร้างจาก TvDatafeed สำเร็จ, shape: {df.shape}") # ✅ Print: DataFrame สร้างสำเร็จ + shape

        # --- เรียกฟังก์ชัน create_stock_chart เพื่อสร้างและบันทึกกราฟ PNG ---
        image_filename = f"{stock_symbol}_chart_line.png" # ✅ ใช้ stock_symbol ในชื่อไฟล์
        image_path = os.path.join(configs.assets_dir, image_filename) # path ของไฟล์ที่จะบันทึกใน assets folder
        chart_image_path = create_stock_chart( # ✅ เรียกฟังก์ชัน create_stock_chart
            data=df,
            symbol=stock_symbol, # ✅ ส่ง stock_symbol ไปยัง create_stock_chart
            chart_type='line', # ✅ ใช้กราฟเส้น (ตามที่คุณต้องการ)
            output_path=image_path # ✅ path ที่จะบันทึกไฟล์ PNG
        )

        if chart_image_path:
            print(f"✅ สร้างและบันทึกกราฟ PNG สำเร็จ: {chart_image_path}") # ✅ Print: สร้างและบันทึกกราฟ PNG สำเร็จ
            return chart_image_path # ✅ Return path ของไฟล์รูปภาพ

        else:
            error_message = f"❌ Error: create_stock_chart() failed to save chart image for {stock_symbol}"
            print(error_message)
            return f"<p style='color:red;'>{error_message}</p>" # หรือ return error HTML message


    except Exception as e:
        error_message = f"❌ Exception in create_matplotlib_chart_html: {e}"
        print(error_message) # ✅ Print: Exception ที่เกิดขึ้น
        return f"<p style='color:red;'>{error_message}</p>" # หรือ return error HTML message
    finally:
        print(f"✅ create_matplotlib_chart_html() จบการทำงาน: stock_symbol = {stock_symbol}") # ✅ Print: จบการทำงานฟังก์ชัน
        
        
