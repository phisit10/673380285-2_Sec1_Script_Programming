# Week 8: Agentic Data Processing (Advanced CSV & JSON Workflows)

โปรเจกต์นี้สาธิตการทำงานของ **"Agentic Data Processor"** ระบบประมวลผลข้อมูลอัตโนมัติที่ควบคุมและจัดลำดับการทำงาน (Workflow Orchestration) สำหรับไฟล์ CSV และ JSON ผ่านไฟล์การตั้งค่าแบบ Declarative JSON ระบบรองรับการแปลงรูปแบบข้อมูลข้ามประเภท การประมวลผลขั้นสูง และการจัดการสถานะข้อมูลย่อยภายในตัว Agent อย่างเป็นระบบ

---

## แนวคิดสำคัญที่นำเสนอ (Key Concepts Demonstrated)

* **Agentic Workflow Orchestration**: `DataAgent` อ่านลำดับขั้นตอนการประมวลผลข้อมูลจากไฟล์ `configs/data_pipeline_config.json` และดำเนินการแต่ละงาน (Tasks) ตามลำดับ พร้อมจัดการการไหลของข้อมูลระหว่างขั้นตอน
* **Internal Data Store**: Agent มีระบบจัดเก็บข้อมูลชั่วคราวในหน่วยความจำ (`self.data_store`) เพื่อส่งผ่านข้อมูลที่ผ่านการประมวลผล (ในรูปแบบ List of Dicts หรือ Nested Dicts/Lists) ไปยัง Task ถัดไปโดยใช้อ้างอิงผ่านคีย์ (Key)
* **การประมวลผล CSV ขั้นสูง (Advanced CSV Processing)**:
  * โหลดข้อมูล CSV เข้าสู่ระบบในรูปแบบ List of Dictionaries (`csv.DictReader`)
  * **Aggregation / Grouping**: จัดกลุ่มข้อมูลตามฟิลด์ที่กำหนด (เช่น `Customer`) และคำนวณผลรวม/ค่าต่างๆ (เช่น `sum` ของ `Amount`)
  * บันทึกข้อมูลที่ประมวลผลเสร็จแล้วกลับลงไฟล์ CSV (`csv.DictWriter`)
* **การประมวลผล JSON ขั้นสูง (Advanced JSON Processing)**:
  * การอ่านและบันทึกไฟล์ JSON
  * **Dynamic Updates**: อัปเดตข้อมูลโครงสร้าง JSON ซับซ้อน (Nested JSON) แบบไดนามิกผ่าน Dot-notation path เช่น การกำหนดค่า (`set`) หรือการอัปเดตหมายเหตุ
  * **Querying Data**: การคิวรีดึงข้อมูลเฉพาะส่วนจาก Nested JSON ผ่านระบุ Path
* **การแปลงรูปแบบข้อมูลข้ามประเภท (Cross-Format Conversion)**:
  * แปลงข้อมูลประเภท List of Dictionaries (จาก CSV) ให้เป็นโครงสร้าง JSON (Python Data Types)
  * รองรับการแปลง JSON กลับเป็น CSV สำหรับโครงสร้างพื้นฐาน
* **การออกแบบโมดูลแบบเปิดกว้าง (Modularity)**: แยกโค้ดออกเป็นสัดส่วนชัดเจน ได้แก่ `csv_tasks.py`, `json_tasks.py`, `conversion_tasks.py`, `config_parser.py`, `data_agent.py` และ `utils.py` เพื่อความง่ายในการอ่านและนำกลับมาใช้ใหม่
* **ความเสถียรและการตรวจสอบระบบ (Robustness & Audit Logging)**: มีการจัดการข้อผิดพลาด (Error Handling) ครอบคลุมทุกจุด พร้อมระบบบันทึก Audit Log เพื่อติดตามสถานะการทำงานในแต่ละขั้นตอนอย่างแม่นยำ

---

## การติดตั้งและการใช้งาน (Setup & How to Run)

### 1. ดาวน์โหลด Repository
```bash
git clone https://github.com/phisit10/673380285-2_Sec1_Script_Programming.git
cd 673380285-2_Sec1_Script_Programming/week8/week8_LabAdv
```

### 2. การเตรียมสภาพแวดล้อม Virtual Environment (แนะนำ)
เนื่องจากโปรเจกต์นี้ใช้โมดูลมาตรฐานของ Python (`csv`, `json` ฯลฯ) เป็นหลัก แต่การสร้าง Virtual Environment จะช่วยแยกสภาพแวดล้อมของโปรเจกต์ให้เป็นสัดส่วน:
```bash
python -m venv venv

# สำหรับ Windows:
venv\Scripts\activate

# สำหรับ macOS / Linux:
source venv/bin/activate
```

### 3. การเตรียมไฟล์ข้อมูลอินพุต (Prepare Input Data Files)
สร้างโฟลเดอร์ชื่อ `data` ที่ Root ของโปรเจกต์ (`week8_LabAdv/data`) หากยังไม่มี:
```bash
mkdir -p data
```
สร้างไฟล์ตัวอย่างดังนี้:
* **`data/input_sales.csv`**: ไฟล์ข้อมูลยอดขายดิบ (บรรทัดแรกเป็น Header เช่น `TransactionID,Customer,Amount,Date`)
* **`data/input_inventory.json`**: ไฟล์ข้อมูลคลังสินค้าตัวอย่างในรูปแบบ JSON

### 4. ตรวจสอบไฟล์ตั้งค่า `configs/data_pipeline_config.json`
* ไฟล์นี้กำหนด Workflow ทั้งหมดในการประมวลผลข้อมูล
* **สำคัญมาก**: ตรวจสอบให้แน่ใจว่าค่า `file_path` ในไฟล์คอนฟิกชี้ไปยังตำแหน่งไฟล์อินพุตถูกต้อง (อ้างอิงแบบ Relative Path จากโปรเจกต์)
* คุณสามารถปรับแต่งรายการ `tasks` เพื่อทดลองการทำ Aggregation, การกรองข้อมูล หรือการแปลง JSON รูปแบบอื่นๆ ได้ตามต้องการ

### 5. รันโปรแกรม
```bash
python main.py
```

เมื่อรันคำสั่ง ระบบจะประมวลผลตาม Pipeline ที่กำหนดไว้ใน `data_pipeline_config.json`:
1. โหลดข้อมูลจาก `input_sales.csv`
2. ทำการสถิติตัวเลขสรุปยอดขายแยกตามลูกค้า และบันทึกลง `data/processed_sales_by_customer.csv`
3. แปลงข้อมูลยอดขายดิบไปเป็นไฟล์ JSON และบันทึกลง `data/sales_data.json`
4. โหลดข้อมูลคลังสินค้าจาก `input_inventory.json`
5. ปรับปรุงข้อมูลใน JSON (เช่น การอัปเดตจำนวนสต็อก หรือเพิ่มรายการสินค้าใหม่)
6. ดึงข้อมูลเฉพาะจุด (Query) จากโครงสร้าง JSON ที่อัปเดตแล้ว
7. บันทึกข้อมูลคลังสินค้าที่อัปเดตลงไฟล์ `data/updated_inventory.json`
8. สร้างรายงานสรุปประวัติการทำงาน `audit_report_*.json` ไว้ในโฟลเดอร์ `reports/`

---

## โครงสร้างโปรเจกต์ (Project Structure)

```text
week8_LabAdv/
├── src/
│   ├── __init__.py          # ตัวระบุแพ็กเกจ Python
│   ├── data_agent.py        # โค้ดหลักของ Agent: ควบคุมการรัน Tasks และจัดการสถานะ Data Store
│   ├── csv_tasks.py         # ฟังก์ชันจัดการ CSV (โหลด, บันทึก, จัดกลุ่ม/สรุปผล, กรองข้อมูล)
│   ├── json_tasks.py        # ฟังก์ชันจัดการ JSON (โหลด, บันทึก, อัปเดตข้อมูลแบบไดนามิก, คิวรี)
│   ├── conversion_tasks.py  # ฟังก์ชันแปลงข้อมูลข้ามรูปแบบระหว่าง CSV <-> JSON
│   ├── config_parser.py     # โหลดและตรวจสอบความถูกต้องของไฟล์ตั้งค่า Pipeline
│   └── utils.py             # ฟังก์ชันช่วยเหลือ เช่น ระบบ Logging, การจัดการโฟลเดอร์ และ Audit Log
├── configs/
│   └── data_pipeline_config.json  # ไฟล์ JSON กำหนดลำดับขั้นตอนการทำงาน (Pipeline Configuration)
├── data/
│   ├── input_sales.csv            # ไฟล์อินพุต CSV (สร้างก่อนรันโปรแกรม)
│   ├── input_inventory.json        # ไฟล์อินพุต JSON (สร้างก่อนรันโปรแกรม)
│   ├── processed_sales_by_customer.csv # ผลลัพธ์: CSV ยอดขายที่ผ่านการจัดกลุ่มและสรุปผล
│   ├── sales_data.json            # ผลลัพธ์: ข้อมูลยอดขายดิบที่แปลงเป็น JSON
│   └── updated_inventory.json     # ผลลัพธ์: ข้อมูลคลังสินค้า JSON ที่ได้รับการอัปเดตแล้ว
├── reports/                       # โฟลเดอร์เก็บไฟล์ Audit Report ย้อนหลัง
├── main.py                        # จุดเริ่มต้นการทำงานของโปรแกรม (Entry Point)
└── README.md                      # เอกสารอธิบายโปรเจกต์ภาษาไทย
```

---

## การแก้ปัญหาและการดีบัก (Debugging Advanced Data Workflows)

* **`FileNotFoundError`**:
  * ตรวจสอบว่าไฟล์ `input_sales.csv` และ `input_inventory.json` ถูกวางอยู่ในโฟลเดอร์ `data/` เรียบร้อยแล้ว
  * ตรวจสอบว่า `file_path` ใน `data_pipeline_config.json` ระบุตำแหน่งอ้างอิงตรงกับโครงสร้างโฟลเดอร์
* **`KeyError` ระหว่างการประมวลผล CSV/JSON**:
  * ตรวจสอบชื่อหัวคอลัมน์ใน CSV และคีย์ในไฟล์ JSON ว่าสะกดตรงกับที่ระบุใน Tasks หรือไม่ (เช่น `Customer`, `Amount` ใน CSV หรือ `id`, `stock` ใน JSON)
  * สำหรับการอัปเดต/คิวรีด้วย Dot-notation path (เช่น `key1.key2.index`) ตรวจสอบว่าระดับชั้น (Hierarchy) ของข้อมูลตรงกับโครงสร้าง JSON จริง
* **รูปแบบ JSON/CSV ไม่ถูกต้อง (Invalid Format)**:
  * ใช้เครื่องมือตรวจสอบไวยากรณ์ (Syntax Validator) เพื่อเช็กไวยากรณ์ใน `input_inventory.json` และ `data_pipeline_config.json` (เช่น ลืมเครื่องหมายจุลภาค หรือเปิด/ปิดวงเล็บไม่ครบ)
  * สำหรับไฟล์ CSV ตรวจสอบตัวแบ่งคอลัมน์ (Delimiter) และการใช้เครื่องหมายอัญประกาศ (`"`) หากข้อมูลมีเครื่องหมายจุลภาคผสมอยู่
* **ข้อมูลไม่อัปเดต หรือประมวลผลไม่ถูกต้อง**:
  * **ตรวจสอบ `input_data_key` และ `output_data_key`**: ตรวจสอบให้แน่ใจว่า `output_data_key` จาก Task ก่อนหน้า มีชื่อตรงกับ `input_data_key` ของ Task ถัดไปหากต้องการส่งต่อข้อมูลไปประมวลผลต่อ
  * **ตรวจสอบพารามิเตอร์ของ Task**: ตรวจสอบค่าพารามิเตอร์ เช่น `group_by_field`, `aggregate_field`, `operator`, `path`, `value` ในไฟล์คอนฟิก
  * **ตรวจสอบ Console Log และ Audit Report**: สังเกตข้อความ Log บนหน้าจอ Terminal หรือเปิดไฟล์ `reports/audit_report_*.json` เพื่อดูสถานะการทำงาน ข้อผิดพลาด และข้อมูลชั่วคราวในแต่ละขั้นตอน
* **ปัญหาการแปลงประเภทข้อมูล (Type Conversion Issues)**:
  * ฟังก์ชัน `csv_to_json` จะพยายามแปลงชนิดข้อมูลพื้นฐาน (`int`, `float`, `boolean`, `null`) ให้อัตโนมัติ หากข้อมูลมีความซับซ้อนขึ้น (เช่น ชนิดข้อมูลวันที่/เวลา) สามารถเพิ่ม Logic ในการแปลงข้อมูลได้ที่ `src/conversion_tasks.py`

---

## แนวทางการพัฒนาต่อยอด (Extension Ideas)

* **การ Join/Merge ข้อมูล CSV ที่ซับซ้อน**: เพิ่มฟังก์ชันสนับสนุนการรวมข้อมูลแบบ SQL (`INNER JOIN`, `LEFT JOIN`) ระหว่างไฟล์ CSV หลายไฟล์ หรือใช้ไลบรารี `pandas` สำหรับชุดข้อมูลขนาดใหญ่
* **การแปลงโครงสร้าง JSON ขั้นสูง (Jinja2 / JMESPath)**: ใช้ Template Engine (เช่น Jinja2) หรือภาษาคิวรี JSON อย่าง JMESPath เพื่อแปลงโครงสร้างข้อมูลซับซ้อนตามเงื่อนไขไดนามิก
* **การตรวจสอบความถูกต้องด้วย Schema (Data Validation)**: นำไลบรารี `jsonschema` มาใช้ตรวจสอบความถูกต้องของข้อมูลอินพุต CSV/JSON ก่อนเริ่มการประมวลผล เพื่อเพิ่มความน่าเชื่อถือของข้อมูล
* **กลยุทธ์การจัดการข้อผิดพลาด (Advanced Error Handling)**: เพิ่มระบบลองใหม่อัตโนมัติ (Retry), การทำงานทดแทน (Fallback Operations) หรือแจ้งเตือนผ่านช่องทางต่างๆ เช่น Email หรือ Webhook เมื่อโปรเซสล้มเหลว
* **การรัน Task ตามเงื่อนไข (Conditional Task Execution)**: เพิ่มความสามารถให้ `DataAgent` สามารถเลือกรัน Task ย่อยตามผลลัพธ์หรือสถานะที่ได้จาก Task ก่อนหน้า
* **การระบุแหล่งข้อมูลแบบ Dynamic Paths / External Sources**: รองรับการตั้งชื่อไฟล์ปลายทางแบบไดนามิก (เช่น เติมวันที่ลงในชื่อไฟล์) หรือการดึงข้อมูลอินพุตผ่าน Web API, Database หรือ Cloud Storage
* **ส่วนต่อประสานผู้ใช้แบบเว็บ (Web Interface)**: สร้าง UI อย่างง่ายด้วย Streamlit หรือ Flask เพื่อให้ผู้ใช้งานอัปโหลดไฟล์คอนฟิก ดูสถานะการทำงาน และดาวน์โหลดผลลัพธ์ผ่านหน้าเว็บได้สะดวก


## แหล่งที่มา
1. https://github.com/kykoo/gcam 
2. https://github.com/MarshallDoyle/Patent 
3. https://github.com/MikeyBeez/RAGAgent
