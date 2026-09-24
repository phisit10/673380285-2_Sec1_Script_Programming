# สัปดาห์ที่ 10: การประมวลผลกระดาษทำการขั้นสูงด้วยเวิร์กโฟลว์อัตโนมัติ (Advanced Spreadsheet Automation & Agentic Workflows)

โปรเจกต์นี้เป็นการจำลองระบบ "Agentic Spreadsheet Processor" ที่ทำหน้าที่ประมวลผลและจัดการไฟล์ Excel (`.xlsx`) ตามลำดับคำสั่งที่กำหนดไว้ในไฟล์คอนฟิกแบบ JSON โดยนำเสนอการใช้งานไลบรารี `openpyxl` ขั้นสูง เช่น การสร้างแผนภูมิ การจัดรูปแบบตามเงื่อนไข (Conditional Formatting) และการใช้สูตรคำนวณ ภายใต้โครงสร้างการทำงานแบบ Task-driven อัตโนมัติ

## แนวคิดสำคัญที่นำเสนอ (Key Concepts Demonstrated)

* **ฟีเจอร์ขั้นสูงของ `openpyxl`**:
    * การสร้างแผนภูมิชนิดต่างๆ ด้วยโค้ด (Bar Chart, Line Chart, Pie Chart)
    * การใส่เงื่อนไขจัดรูปแบบข้อมูลอัตโนมัติ (Color Scales, Data Bars, Custom Formulas)
    * การแทรกและจัดการสูตรคำนวณของ Excel
    * การจัดการชีตและเซลล์ข้อมูลพื้นฐาน
* **การออกแบบเวิร์กโฟลว์ด้วยการกำหนดค่า (Agentic Design with Configuration)**: การทำงานหลักจะถูกขับเคลื่อนผ่านไฟล์ `example_spreadsheet_config.json` ซึ่งกำหนดลำดับขั้นของงาน (เช่น `copy_data`, `calculate_column`, `conditional_format`, `chart`) ช่วยให้ระบบยืดหยุ่นและนำกลับมาใช้ใหม่ได้ง่าย
* **โครงสร้างโค้ดแบบแยกส่วน (Modular Code Structure)**: แยกหน้าที่การทำงานอย่างชัดเจนออกเป็น `spreadsheet_agent.py`, `config_parser.py` และ `utils.py` เพื่อการดูแลรักษาและขยายระบบในอนาคต
* **ระบบบันทึกประวัติการทำงาน (Audit Logging)**: สร้างชีต "Audit Log" ในไฟล์ Excel ผลลัพธ์โดยอัตโนมัติ เพื่อบันทึกสถานะการทำงานในแต่ละขั้นตอนทั้งที่สำเร็จและล้มเหลว

## การติดตั้งและการใช้งาน (Setup & How to Run)

1. **ดาวน์โหลด Repository:**
    ```bash
    git clone https://github.com/phisit10/673380285-2_Sec1_Script_Programming.git
    cd 673380285-2_Sec1_Script_Programming/week10/week10_LabAdv
    ```

2. **ติดตั้ง Dependencies:**
    แนะนำให้ใช้งานผ่าน Virtual Environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # สำหรับ Windows: venv\Scripts\activate.bat
    pip install openpyxl
    ```

3. **เตรียมข้อมูลนำเข้า (Input Data):**
    * สร้างโฟลเดอร์ชื่อ `data` ที่ Root ของโปรเจกต์: `mkdir data`
    * สร้างไฟล์ Excel ชื่อ `input_data.xlsx` ไว้ภายในโฟลเดอร์ `data`
    * ใส่ข้อมูลตัวอย่างยอดขายในชีตชื่อ `SalesData` โดยมีคอลัมน์ "Product Name", "Quantity", และ "Unit Price"

    **ตัวอย่างข้อมูลใน `data/input_data.xlsx` (Sheet: `SalesData`):**

    | Product Name | Quantity | Unit Price |
    | :----------- | :------- | :--------- |
    | Laptop       | 2        | 1200.50    |
    | Mouse        | 5        | 25.00      |
    | Keyboard     | 3        | 75.99      |
    | Monitor      | 1        | 300.00     |
    | Projector    | 1        | 850.00     |
    | Webcam       | 10       | 45.00      |
    | Headset      | 4        | 99.99      |
    | SSD          | 2        | 180.00     |
    | Router       | 1        | 70.00      |

4. **ตรวจสอบไฟล์ `configs/example_spreadsheet_config.json`:**
    * ไฟล์นี้ระบุลำดับงานที่ Agent จะต้องทำ
    * **สำคัญ:** ตรวจสอบชื่อชีต (เช่น `"SalesData"`, `"Raw Data"`) และช่วงของเซลล์ (เช่น `"D2:D100"`, `"A1:A5"`) ในไฟล์คอนฟิกให้ตรงกับโครงสร้างไฟล์ `input_data.xlsx`
5. **รันสคริปต์:**
    ```bash
    python main.py
    ```
    สคริปต์จะทำการ:
    * โหลดไฟล์ `input_data.xlsx`
    * ประมวลผล Task ตามที่กำหนดไว้ใน `example_spreadsheet_config.json`
    * สร้างไฟล์ผลลัพธ์ `output_report.xlsx` ในโฟลเดอร์ `data` ซึ่งประกอบด้วยชีตข้อมูล คอลัมน์คำนวณ การจัดรูปแบบตามเงื่อนไข กราฟสรุป และชีต "Audit Log"

## โครงสร้างโปรเจกต์ (Project Structure)

```text
week10_LabAdv/
├── src/
│   ├── __init__.py               # บ่งบอกความเป็น Python Package
│   ├── spreadsheet_agent.py      # โค้ดหลักของ Agent: จัดการ Task และสั่งงาน openpyxl
│   ├── config_parser.py          # อ่านและตรวจสอบความถูกต้องของไฟล์ JSON Config
│   ├── utils.py                  # ฟังก์ชันช่วยเหลือ (Helper Functions) และการทำ Logging
│   └── google_sheets_utils.py    # โครงร่างสำหรับการเชื่อมต่อ Google Sheets API ในอนาคต
├── configs/
│   └── example_spreadsheet_config.json  # ไฟล์กำหนดลำดับงานอัตโนมัติ
├── data/
│   ├── input_data.xlsx           # ไฟล์ Excel ข้อมูลนำเข้า
│   └── output_report.xlsx        # ไฟล์ Excel ผลลัพธ์ที่สร้างขึ้น
├── main.py                       # จุดเริ่มต้นการทำงานของโปรแกรม (Entry Point)
└── README.md                     # เอกสารอธิบายรายละเอียดโปรเจกต์
```

## การแก้ไขปัญหาที่พบบ่อย (Debugging)

* **`KeyError: 'SheetName'`**: เกิดจาก `openpyxl` หาชื่อชีตไม่พบ ให้ตรวจสอบตัวสะกดชื่อชีตในไฟล์ `input_data.xlsx` และไฟล์คอนฟิกให้ตรงกัน
* **`AttributeError`**: มักเกิดจากการพยายามเข้าถึงพร็อพเพอร์ตี้ของออบเจกต์ที่เป็น `None` ให้ตรวจสอบการอ้างอิงตำแหน่งเซลล์หรือขอบเขตข้อมูลในไฟล์คอนฟิก
* **`Formula Error` ใน Excel**: หากไฟล์ที่สร้างได้ขึ้นข้อผิดพลาด `#NAME?` หรือ `#VALUE!` แสดงว่าไวยากรณ์ของสูตร Excel ที่ใส่ในไฟล์ JSON ไม่ถูกต้อง ให้ทดลองพิมพ์สูตรนั้นใน Excel ก่อนนำมาใส่ในคอนฟิก
* **แผนภูมิหรือ Conditional Formatting ไม่แสดง**:
    * ตรวจสอบว่า `data_range` และ `category_range` ระบุขอบเขตที่มีข้อมูลอยู่จริง
    * ตรวจสอบว่าช่วงเซลล์ของ Conditional Formatting ถูกต้องและประมวลผลหลังจากมีข้อมูลแล้ว
* **ตรวจสอบ Log**: ตรวจสอบข้อความแจ้งเตือนผ่าน Console หรือดูรายละเอียดในชีต "Audit Log" ที่ถูกสร้างขึ้นใน `output_report.xlsx`

## แนวทางการพัฒนาต่อในอนาคต (Extension Ideas)

* **การเชื่อมต่อ Google Sheets API**: พัฒนาไฟล์ `google_sheets_utils.py` เพื่อรองรับการทำงานกับ Google Sheets ผ่านไลบรารี `gspread`
* **การเชื่อมต่อฐานข้อมูล**: เพิ่ม Task สำหรับอ่านข้อมูลจาก SQL Database (เช่น SQLite, PostgreSQL) มาลงในชีตโดยตรง
* **การดึงข้อมูลจาก REST API**: เพิ่มคำสั่งสำหรับดึงข้อมูลจาก Web API ภายนอกมาสร้างเป็นรายงาน
* **การรับพารามิเตอร์ผ่าน Command Line**: ปรับให้ `main.py` รับอาร์กิวเมนต์ระบุพาธของไฟล์คอนฟิกหรือไฟล์ผลลัพธ์ได้
* **การสร้าง GUI**: พัฒนาหน้าต่างโปรแกรม (เช่น ใช้ `Tkinter` หรือ `PyQt`) สำหรับช่วยผู้ใช้สร้างไฟล์ JSON Configuration ได้ง่ายขึ้น

## แหล่งที่มา (References)

1. https://github.com/kykoo/gcam
2. https://github.com/dreamYiZ/AutoSite