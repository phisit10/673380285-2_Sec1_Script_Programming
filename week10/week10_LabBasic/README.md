# Lab Basic: การประมวลผลไฟล์ Excel ด้วย Python (`openpyxl`)

## แนวคิดหลักที่ได้เรียนรู้ (Key Concepts Demonstrated)

* **ไลบรารี `openpyxl`**: ไลบรารีหลักสำหรับอ่าน เขียน และแก้ไขไฟล์ Excel นามสกุล `.xlsx` ในภาษา Python
* **การจัดการ Workbook & Worksheet**: การโหลดไฟล์ที่มีอยู่, การสร้าง Workbook ใหม่, การเข้าถึงและการสร้างแผ่นงาน (Sheet)
* **การจัดการข้อมูลในเซลล์ (Cell Manipulation)**: การอ่านและบันทึกค่าลงในเซลล์โดยอ้างอิงตามพิกัด (Row, Column) หรือชื่อเซลล์ (เช่น `A1`, `B2`)
* **การประมวลผลข้อมูล (Data Processing)**: การวนลูปอ่านข้อมูลทีละแถว และการคำนวณผลลัพธ์ (เช่น การคำนวณราคารวมของสินค้า)
* **การจัดรูปแบบพื้นฐาน (Basic Formatting)**: การปรับแต่งแบบอักษร (Font), สีพื้นหลัง (Fill), เส้นขอบ (Border) และรูปแบบตัวเลข (Number Format)
* **การปรับความกว้างคอลัมน์อัตโนมัติ (Column Width Adjustment)**: การคำนวณและปรับความกว้างของคอลัมน์ให้พอดีกับข้อมูลเพื่อความสวยงามและอ่านง่าย

## การติดตั้งและการใช้งาน (Setup & How to Run)

1. **Clone Repository:**
   ```bash
   git clone https://github.com/phisit10/673380285-2_Sec1_Script_Programming.git
   cd 673380285-2_Sec1_Script_Programming/week10/week10_LabBasic
   ```

2. **ติดตั้ง Dependencies:**
   แนะนำให้สร้างและเปิดใช้งาน Virtual Environment ก่อนทำการติดตั้ง:
   ```bash
   python -m venv venv
   
   # สำหรับ Windows Command Prompt:
   venv\Scripts\activate.bat
   # สำหรับ Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   # สำหรับ macOS/Linux:
   source venv/bin/activate

   # ติดตั้ง openpyxl
   pip install openpyxl
   ```

3. **จัดเตรียมข้อมูลนำเข้า (Input Data):**
   * สร้างโฟลเดอร์ชื่อ `data` ในไดเรกทอรีนี้: `mkdir data`
   * สร้างไฟล์ Excel ชื่อ `input_sales.xlsx` ไว้ภายในโฟลเดอร์ `data`
   * ใส่ข้อมูลตัวอย่างการขายลงใน `input_sales.xlsx` โดยกำหนดให้แถวแรก (A1, B1, C1) เป็น Header ชื่อ "Product Name", "Quantity", และ "Unit Price" ตามลำดับ และเริ่มใส่ข้อมูลตั้งแต่แถวที่ 2 เป็นต้นไป

   **ตัวอย่างข้อมูลใน `input_sales.xlsx`:**

   | Product Name | Quantity | Unit Price |
   | :----------- | :------- | :--------- |
   | Laptop       | 2        | 1200.50    |
   | Mouse        | 5        | 25.00      |
   | Keyboard     | 3        | 75.99      |
   | Monitor      | 1        | 300.00     |
   | Printer      | 1        | 150.00     |

4. **รันโปรแกรม:**
   ```bash
   python main.py
   ```
   *สคริปต์จะทำการ:*
   * อ่านข้อมูลจากไฟล์ `data/input_sales.xlsx`
   * คำนวณราคารวมของแต่ละรายการสินค้า และราคารวมทั้งหมด (Grand Total)
   * บันทึกผลลัพธ์พร้อมการจัดรูปแบบลงในไฟล์ `data/output_sales_report.xlsx`

## โครงสร้างโปรเจกต์ (Project Structure)

```text
week10_LabBasic/
├── data/
│   ├── input_sales.xlsx        # ไฟล์ Excel ข้อมูลนำเข้าตัวอย่าง (ต้องสร้างขึ้นเอง)
│   └── output_sales_report.xlsx # ไฟล์รายงาน Excel ผลลัพธ์ที่โปรแกรมสร้างขึ้น
├── src/
│   ├── __init__.py             # บ่งบอกความเป็น Python Package
│   └── excel_processor.py      # Logic หลักในการอ่าน เขียน และประมวลผล Excel
├── main.py                     # สคริปต์หลักสำหรับเริ่มทำงานโปรแกรม
├── .gitignore                  # กำหนดไฟล์/โฟลเดอร์ที่ไม่ต้องการให้ Git ติดตาม
└── README.md                   # เอกสารอธิบายรายละเอียดและวิธีการใช้งาน
```

## การแก้ปัญหาเบื้องต้น (Debugging Spreadsheet Automation)

* **`FileNotFoundError`**: ตรวจสอบว่ามีไฟล์ `input_sales.xlsx` อยู่ในโฟลเดอร์ `data` จริงหรือไม่ และชื่อไฟล์ตรงกับที่ระบุในโค้ดหรือไม่
* **`InvalidFileException` (หรือข้อผิดพลาดเกี่ยวกับ `openpyxl`)**: มักเกิดจากไฟล์ชำรุด หรือไฟล์ไม่ได้เป็น นามสกุล `.xlsx` จริง (เช่น เป็นไฟล์ `.xls` รุ่นเก่า ซึ่ง `openpyxl` ไม่รองรับ) ตรวจสอบให้มั่นใจว่าไฟล์ถูกบันทึกเป็น `.xlsx`
* **`IndexError` หรือ `TypeError`**: เกิดขึ้นเมื่อโค้ดพยายามนำข้อความมาคำนวณทางคณิตศาสตร์ หรือเข้าถึงแถว/คอลัมน์ที่ไม่มีอยู่จริง ควรเพิ่ม `try-except` หรือเช็กค่า `None` ก่อนการคำนวณ
* **ลำดับข้อมูลไม่ตรง (Data Mismatches)**: โค้ดจะอ้างอิงลำดับคอลัมน์ตามที่กำหนด (Product Name, Quantity, Unit Price) หากไฟล์นำเข้ามีลำดับคอลัมน์ต่างออกไป ผลการคำนวณจะผิดพลาด ให้แก้ไขโค้ดใน `excel_processor.py` ให้ตรงกับโครงสร้างไฟล์จริง
* **รูปแบบไม่เปลี่ยน (Formatting Issues)**: หากสไตล์ที่ตั้งค่าไว้ไม่แสดงผล ให้ตรวจสอบการเรียกใช้ module `openpyxl.styles` และตรวจสอบว่าได้ปรับแต่งสไตล์ลงในออบเจกต์เซลล์เรียบร้อยก่อนสั่ง `.save()`

## แนวทางการต่อยอดในอนาคต (Extension Ideas)

* **การเชื่อมต่อกับ Google Sheets**: นำไลบรารี `gspread` มาใช้เพื่ออ่านและอัปเดตข้อมูลบน Google Sheets ผ่าน API บนระบบคลาวด์
* **การตรวจสอบความถูกต้องของข้อมูล (Automated Data Validation)**: เพิ่มระบบตรวจสอบค่าว่าง (Missing Values) หรือประเภทข้อมูลที่ผิดพลาดก่อนนำไปคำนวณ
* **การวิเคราะห์ข้อมูลขั้นสูง (Advanced Data Analysis)**: เพิ่มการคำนวณยอดขายเฉลี่ยต่อสินค้า หรือการจัดกลุ่มข้อมูลสร้าง Pivot Table
* **การสร้างกราฟ (Chart Generation)**: ใช้ฟังก์ชันสร้างแผนภูมิของ `openpyxl` เช่น Bar Chart หรือ Line Chart เพื่อแสดงสรุปยอดขายในไฟล์ Excel
* **การจัดรูปแบบตามเงื่อนไข (Conditional Formatting)**: ใส่สีไฮไลต์เซลล์ตามเงื่อนไข เช่น ไฮไลต์สินค้าที่ยอดขายต่ำกว่าเกณฑ์ หรือสต็อกคงเหลือต่ำ
* **การพัฒนาส่วนต่อประสานผู้ใช้ (GUI)**: สร้างหน้าต่างโปรแกรมด้วย `Tkinter` หรือ `PyQt` เพื่อให้ผู้ใช้งานเลือกไฟล์และกดประมวลผลได้ง่ายขึ้น
* **การเชื่อมต่อกับฐานข้อมูล**: อ่านข้อมูลจากไฟล์ Excel แล้วบันทึกลงในฐานข้อมูล (Database) หรือดึงข้อมูลจาก SQL มาส่งออกเป็นรายงาน Excel อัตโนมัติ

---

## แหล่งที่มา (References)

1. [GideonJagen/auto-budget](https://github.com/GideonJagen/auto-budget)
2. [KijaziAbraham/Managing-Subscription-Payment](https://github.com/KijaziAbraham/Managing-Subscription-Payment)
3. [MikeyBeez/RAGAgent](https://github.com/MikeyBeez/RAGAgent)
4. [Automate the Boring Stuff with Python - Chapter 13 Working with Excel Spreadsheets](https://automatetheboringstuff.com/2e/chapter13/)