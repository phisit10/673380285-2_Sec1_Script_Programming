# สัปดาห์ที่ 11: ระบบจัดการเอกสารอัตโนมัติด้วยเอเจนต์ (Agentic Document Automation - Advanced PDFs & Word)

โปรเจกต์นี้เป็นการพัฒนาระบบ "Agentic Document Processor" ซึ่งเป็นเอเจนต์ประมวลผลเอกสารอัตโนมัติที่รองรับงานที่มีความซับซ้อนทั้งบนไฟล์เอกสารประเภท PDF และ Word (.docx) ระบบทำงานโดยอ่านชุดคำสั่งจากไฟล์การตั้งค่า JSON (Declarative Config) เพื่อลำดับและดำเนินงานแต่ละขั้นตอนอย่างเป็นระบบ ผ่านการใช้งานไลบรารี `pypdf` (หรือ `PyPDF2`), `python-docx` และ `reportlab`

## แนวคิดหลักของโปรเจกต์ (Key Concepts)

* **Agentic Workflow**: ควบคุมและกำหนดขั้นตอนการทำงานของเอกสารผ่านไฟล์คอนฟิกภายนอก (`configs/document_automation_config.json`) โดยคลาส `DocumentAgent` จะอ่านสเปกงานและประมวลผลภารกิจต่างๆ ตามลำดับแบบไดนามิก
* **Template-Based Word Generation**:
  * ใช้แม่แบบเอกสาร Word (`templates/report_template.docx`) ที่มีข้อความแทนที่ `{{placeholders}}`
  * แทนที่ตัวแปรในแม่แบบด้วยข้อมูลจริงที่ระบุไว้ในไฟล์การตั้งค่า (JSON Config)
  * แทรกตารางข้อมูลลงในตำแหน่ง `{{TABLE_PLACEHOLDER}}` หรือต่อท้ายเอกสารแบบไดนามิก
* **Advanced PDF Watermarking**:
  * สร้างเอกสาร PDF ลายน้ำแบบไดนามิก ณ เวลาที่รันโปรแกรม โดยใช้ไลบรารี `ReportLab`
  * นำลายน้ำที่สร้างขึ้นไปซ้อนทับ (Overlay) ลงบนหน้าเอกสาร PDF ต้นฉบับทุกหน้าด้วย `pypdf` / `PyPDF2`
* **PDF Merging & Text Extraction**: มีฟังก์ชันรวมเอกสาร PDF หลายไฟล์เข้าด้วยกันเป็นไฟล์เดียว รวมถึงการสกัดข้อความ (Text Extraction) ออกจากทั้งไฟล์ PDF และ Word
* **Modular & Robust Design**:
  * จัดโครงสร้างโค้ดอย่างเป็นสัดส่วน แยกโมดูลตามหน้าที่ ได้แก่ `pdf_tasks.py`, `word_tasks.py`, `config_parser.py` และ `utils.py` เพื่อความง่ายในการดูแลรักษา
  * มีระบบจัดการข้อผิดพลาด (Error Handling) และระบบบันทึก Log การทำงาน
  * สร้างรายงานสรุปประวัติการทำงาน (Audit Report) ในรูปแบบ JSON ทุกครั้งที่ประมวลผลเสร็จสิ้น

## การติดตั้งและการใช้งาน (Setup & How to Run)

1. **สลับเข้าสู่โฟลเดอร์โปรเจกต์:**
   ```bash
   cd week11/week11_LabAdv
   ```

2. **ติดตั้งสภาพแวดล้อมเสมือนและไลบรารีที่จำเป็น (Dependencies):**
   แนะนำให้สร้าง Virtual Environment ก่อนการติดตั้ง:
   ```bash
   python -m venv venv
   
   # สำหรับ macOS/Linux:
   source venv/bin/activate  
   
   # สำหรับ Windows:
   venv\Scripts\activate
   
   # ติดตั้งไลบรารีที่จำเป็น
   pip install pypdf python-docx reportlab
   ```
   * *หมายเหตุ:* จำเป็นต้องติดตั้ง `reportlab` สำหรับใช้สร้างลายน้ำ PDF แบบไดนามิก

3. **เตรียมไฟล์เอกสารอินพุตและแม่แบบ (Input Documents & Templates):**
   * ตรวจสอบให้แน่ใจว่ามีโฟลเดอร์ `documents/` และ `templates/` อยู่ในโปรเจกต์
   * **`templates/report_template.docx`**: เอกสาร Word แม่แบบที่มีตัวแปรแทรก เช่น `{{REPORT_TITLE}}`, `{{REPORT_DATE}}`, `{{AUTHOR_NAME}}`, `{{COMPANY_NAME}}`, `{{INTRODUCTION_TEXT}}`, `{{MONTH_PERIOD}}` และตัวแปรระบุตำแหน่งตาราง `{{TABLE_PLACEHOLDER}}`
   * **`documents/source_document.pdf`**: ไฟล์ PDF ต้นฉบับสำหรับการทดสอบใส่ลายน้ำ
   * **`documents/dummy_doc1.pdf` และ `documents/dummy_doc2.pdf`**: ไฟล์ PDF ตัวอย่างสองไฟล์สำหรับทดสอบการรวมไฟล์ (PDF Merging)

4. **ตรวจสอบไฟล์กำหนดค่า `configs/document_automation_config.json`:**
   * ตรวจสอบพาธของไฟล์ เช่น `template_path`, `input_pdf`, `input_pdfs`, `output_path` ให้ถูกต้องเมื่ออ้างอิงจากโฟลเดอร์หลักของโปรเจกต์
   * ปรับแต่งข้อมูลใน `global_data` หรือข้อมูลเฉพาะของแต่ละภารกิจ (`data`) ตามต้องการ

5. **เรียกทำงานสคริปต์หลัก:**
   ```bash
   python main.py
   ```
   
   เมื่อรันสคริปต์ ระบบจะดำเนินการตามขั้นตอนดังนี้:
   * อ่านชุดคำสั่งจาก `document_automation_config.json`
   * สร้างไฟล์ `documents/generated_report.docx` จากแม่แบบ โดยเติมข้อมูลลงในตัวแปรและแทรกตารางข้อมูล
   * สร้างไฟล์ `documents/watermarked_document.pdf` โดยประทับลายน้ำ (เช่น ข้อความ "CONFIDENTIAL") ลงบน `source_document.pdf`
   * รวมไฟล์ `dummy_doc1.pdf` และ `dummy_doc2.pdf` ออกมาเป็น `documents/merged_docs.pdf`
   * สกัดข้อความจากเอกสาร Word และ PDF ที่กำหนด แล้วบันทึกเป็นไฟล์ `.txt`
   * สร้างรายงานการทำงาน (Audit Log) จัดเก็บเป็นไฟล์ JSON ไว้ในโฟลเดอร์ `documents/reports/`

## โครงสร้างโปรเจกต์ (Project Structure)

```text
week11_LabAdv/
├── src/
│   ├── __init__.py                     # ตัวระบุแพ็กเกจ Python
│   ├── document_agent.py               # คลาสหลักที่ควบคุมการทำงานของภารกิจต่างๆ ตาม Config
│   ├── pdf_tasks.py                    # รวมฟังก์ชันจัดการ PDF (ใส่ลายน้ำ, รวมไฟล์, สกัดข้อความ)
│   ├── word_tasks.py                   # รวมฟังก์ชันจัดการ Word (แทนที่ Template, ใส่ตาราง, สกัดข้อความ)
│   ├── config_parser.py                # โหลดและตรวจสอบความถูกต้องของไฟล์การตั้งค่า JSON
│   └── utils.py                        # ระบบ Logging, จัดการไดเรกทอรี และการสร้าง Audit Report
├── configs/
│   └── document_automation_config.json # ไฟล์กำหนดภารกิจและการตั้งค่าของ Agent
├── templates/
│   └── report_template.docx            # แม่แบบเอกสาร Word พร้อม Placeholders
├── documents/
│   ├── source_document.pdf             # PDF ต้นฉบับสำหรับทดสอบใส่ลายน้ำ
│   ├── dummy_doc1.pdf                  # PDF ตัวอย่าง 1 สำหรับทดสอบรวมไฟล์
│   ├── dummy_doc2.pdf                  # PDF ตัวอย่าง 2 สำหรับทดสอบรวมไฟล์
│   ├── generated_report.docx           # [Output] เอกสาร Word ที่สร้างขึ้นสำเร็จ
│   ├── watermarked_document.pdf        # [Output] เอกสาร PDF ที่ประทับลายน้ำแล้ว
│   ├── merged_docs.pdf                 # [Output] เอกสาร PDF ที่รวมไฟล์แล้ว
│   ├── extracted_pdf_text.txt          # [Output] ข้อความที่สกัดได้จาก PDF
│   ├── extracted_word_text.txt         # [Output] ข้อความที่สกัดได้จาก Word
│   └── reports/                        # โฟลเดอร์เก็บรายงานการทำงาน
│       └── audit_report_YYYYMMDD_HHMMSS.json # [Output] บันทึก Audit Log
├── main.py                             # จุดเริ่มต้นการทำงานของโปรแกรม (Entry Point)
├── .gitignore                          # กำหนดไฟล์/โฟลเดอร์ที่ไม่ต้องติดตามในระบบ Git
└── README.md                           # เอกสารอธิบายรายละเอียดโปรเจกต์
```

## การแก้ปัญหาและการตรวจสอบข้อผิดพลาด (Debugging & Troubleshooting)

* **`FileNotFoundError`**: ตรวจสอบว่าไฟล์อินพุตและแม่แบบ (`.pdf`, `.docx`) วางอยู่ในโฟลเดอร์ `documents/` และ `templates/` ถูกต้องหรือไม่ และเช็คพาธใน `document_automation_config.json` ให้ตรงกับโครงสร้างไดเรกทอรีจริง
* **`ImportError: No module named 'reportlab'` หรือ `pypdf`**: แสดงว่ายังไม่ได้ติดตั้งไลบรารีที่เกี่ยวข้อง ให้รันคำสั่ง `pip install reportlab pypdf python-docx`
* **ตัวแปรในเอกสาร Word ไม่ถูกแทนที่ (Placeholder Not Replaced)**:
  * ตรวจสอบชื่อตัวแปรในแม่แบบ `.docx` กับในไฟล์ JSON Config ว่าสะกดตรงกันทุกตัวอักษรหรือไม่ (Case-sensitive)
  * ตรวจสอบว่าไม่มีช่องว่างเกินหรืออักขระแฝงอยู่ในตัวแปร `{{placeholder}}` บนไฟล์ Word (บางครั้งโปรแกรม Word แยกรูปแบบฟอนต์ทำให้ข้อความถูกแบ่งเป็นหลาย Run)
* **ลายน้ำใน PDF ไม่แสดงผลหรือไม่ตรงตำแหน่ง**:
  * ปรับค่า `font_size`, สี/ความโปร่งแสง (`color`), และมุมเอียง (`angle`) ในภารกิจ `apply_pdf_watermark` ของไฟล์การตั้งค่า
* **ตารางไม่ถูกแทรกในเอกสาร Word**:
  * ตรวจสอบว่ามีตัวแปร `{{TABLE_PLACEHOLDER}}` ในไฟล์แม่แบบ Word หรือไม่
  * ตรวจสอบรูปแบบข้อมูล `table_data` ในคอนฟิกว่าอยู่ในรูปแบบ List ของ List (มิติ 2D) ที่ถูกต้องหรือไม่
* **การตรวจสอบบันทึกการทำงาน**: นอกจากการดู Log บนหน้าจอ Console แล้ว สามารถเปิดดูรายละเอียดผลการรันย่อและข้อผิดพลาดอย่างละเอียดได้ที่ไฟล์ `documents/reports/audit_report_*.json`

## แนวทางการพัฒนาต่อยอด (Future Extension Ideas)

* **การกรอกแบบฟอร์ม PDF (PDF Form Filling)**: เชื่อมต่อไลบรารีเพิ่มเติม เช่น `PyMuPDF` หรือ `pdfrw` เพื่ออ่าน เติมข้อมูล และบันทึกแบบฟอร์ม PDF อัตโนมัติ
* **การเซ็นสัญญาดิจิทัล (Digital Signatures)**: เพิ่มฟังก์ชันประทับลายเซ็นดิจิทัล (Digital Signature) บนเอกสาร PDF เพื่อยืนยันความถูกต้องและความปลอดภัย
* **การจัดการรูปภาพใน Word**: เพิ่มระบบการแทรกรูปภาพ ปรับขนาด จัดตำแหน่ง และปรับการพันรอบข้อความ (Text Wrapping) ในเอกสาร Word
* **ระบบเงื่อนไขในการสร้างเนื้อหา (Conditional Content)**: เขียน logic เพิ่มเติมใน `word_tasks.py` ให้สามารถเพิ่ม/ซ่อน ย่อหน้า ตาราง หรือเซกชันตามเงื่อนไขของข้อมูลอินพุต
* **การประมวลผลแบบกลุ่ม (Batch Processing)**: ปรับแต่งให้เอเจนต์สามารถรับชุดข้อมูลอินพุตพร้อมกันหลายชุด เพื่อสร้างเอกสารจำนวนมากได้ในการรันครั้งเดียว

---

## แหล่งที่มา (Sources)

1. https://github.com/kykoo/gcam
2. https://github.com/aanorlondo/pdf-watermark
3. https://github.com/KBGA/Furhat_Dialog_Converter
4. https://github.com/3000alex/sistema_reportes2.0
5. https://github.com/SANTIAGOPATRICIA/RKP
6. https://github.com/ClaudioOliveira89/Python
7. https://github.com/Akaymaz2635/DISP
8. https://github.com/greeenCode/translators-pool-search
9. https://github.com/MikeyBeez/RAGAgent