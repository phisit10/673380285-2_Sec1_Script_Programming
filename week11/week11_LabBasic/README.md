# Week 11: Lab Basic - การจัดการเอกสาร PDF และ Word อัตโนมัติด้วย Python

โปรเจกต์ปฏิบัติการนี้สาธิตการจัดการและทำงานกับไฟล์เอกสาร PDF และ Microsoft Word แบบอัตโนมัติโดยใช้ภาษา Python ในรายวิชา Script Programming โดยเน้นการใช้งานไลบรารี `PyPDF2` (สำหรับการอ่านและรวมไฟล์ PDF) และ `python-docx` (สำหรับการสร้างและจัดรูปแบบเอกสาร Word)

## แนวคิดหลักที่เรียนรู้ (Key Concepts Demonstrated)

* **การดึงข้อความจาก PDF (PDF Text Extraction)**: การอ่านเนื้อหาข้อความภายในไฟล์ PDF ผ่านสคริปต์ Python
* **การรวมไฟล์ PDF (PDF Merging)**: การนำไฟล์ PDF หลายไฟล์มารวมกันให้เป็นไฟล์เดียว
* **การสร้างเอกสาร Word (Word Document Creation)**: การสร้างไฟล์นามสกุล `.docx` ใหม่ด้วยโค้ด
* **การเพิ่มเนื้อหาและจัดรูปแบบใน Word**: การแทรกหัวข้อ (Headings), ย่อหน้า (Paragraphs), การจัดตัวหนา/ตัวเอียง/ขนาดฟอนต์ และการสร้างตาราง (Tables)
* **การออกแบบแบบแยกโมดูล (Modular Design)**: การแบ่ง Logic การทำงานออกเป็นสัดส่วนอย่างชัดเจน เช่น โมดูลจัดการ PDF (`pdf_processor.py`) และโมดูลจัดการ Word (`word_processor.py`)
* **ความเสถียรและการจัดการข้อผิดพลาด (Robustness & Error Handling)**: การดักจับ Exception เบื้องต้นเกี่ยวกับการเปิด/อ่านไฟล์ พร้อมการแสดงผลบันทึกระบบ (Logging)

## การติดตั้งและการใช้งาน (Setup & How to Run)

1. **Clone Repository และย้ายเข้าโฟลเดอร์แล็บ:**
```bash
git clone https://github.com/phisit10/673380285-2_Sec1_Script_Programming.git
cd 673380285-2_Sec1_Script_Programming/week11/week11_LabBasic
```

2. **ติดตั้ง Dependencies:**
แนะนำให้สร้าง Virtual Environment ก่อนทำการติดตั้ง:
```bash
# สร้างและเปิดใช้งาน Virtual Environment
python -m venv venv
source venv/bin/activate  # สำหรับ macOS/Linux
# venv\Scripts\activate.bat  # สำหรับ Windows

# ติดตั้งไลบรารีที่จำเป็น
pip install PyPDF2 python-docx
```

3. **เตรียมไฟล์เอกสารสำหรับทดสอบ (Input Documents):**
* สร้างโฟลเดอร์ชื่อ `documents` ไว้ที่ Root ของโปรเจกต์: `mkdir documents`
* **`input_article.pdf`**: วางไฟล์ PDF ตัวอย่างที่มีข้อความไว้ในโฟลเดอร์ `documents` (เพื่อใช้ทดสอบการอ่านและดึงข้อความไปใส่ใน Word)
* **`dummy_doc1.pdf` และ `dummy_doc2.pdf`**: วางไฟล์ PDF ขนาดเล็กอย่างละ 1 ไฟล์ไว้ในโฟลเดอร์ `documents` เพื่อใช้ทดสอบการรวมไฟล์ PDF

**ตัวอย่างเนื้อหาสำหรับสร้างไฟล์ `input_article.pdf`:**
```text
Introduction to Automation

Automation is the creation and application of technology to produce and deliver goods and services with minimal human intervention. The implementation of automation technologies, techniques, and processes improves the efficiency, reliability, and speed of many tasks that were previously performed manually.

Benefits of Automation

1. Increased Efficiency: Tasks are completed faster.
2. Cost Reduction: Lower labor costs.
3. Improved Accuracy: Minimizes human error.

Conclusion

Automation is transforming industries globally.
```

4. **รันสคริปต์หลัก:**
```bash
python main.py
```
เมื่อรันสคริปต์แล้ว โปรแกรมจะทำงานดังนี้:
* อ่านและดึงข้อความออกจากไฟล์ `input_article.pdf`
* สร้างไฟล์ `output_report.docx` ในโฟลเดอร์ `documents` ซึ่งบรรจุข้อความที่ดึงมา พร้อมหัวข้อและการสร้างตารางสรุป
* หากมีไฟล์ `dummy_doc1.pdf` และ `dummy_doc2.pdf` โปรแกรมจะรวมทั้งสองไฟล์เข้าด้วยกันเป็น `merged_output.pdf`

## โครงสร้างโปรเจกต์ (Project Structure)

```text
week11_LabBasic/
├── src/
│   ├── __init__.py         # เครื่องหมายระบุว่าเป็น Python Package
│   ├── pdf_processor.py    # โค้ดสำหรับจัดการไฟล์ PDF (ดึงข้อความ, รวมไฟล์)
│   ├── word_processor.py   # โค้ดสำหรับจัดการไฟล์ Word (สร้างเอกสาร, ใส่ข้อความ, จัดรูปแบบ)
│   └── utils.py            # ฟังก์ชันช่วยเหลือทั่วไป (เช่น การจัดการการบันทึก Log หรือการสร้างโฟลเดอร์)
├── documents/
│   ├── input_article.pdf   # ไฟล์ PDF สำหรับทดสอบการดึงข้อความ (ผู้ใช้ต้องสร้าง/วางเอง)
│   ├── dummy_doc1.pdf      # ไฟล์ PDF ตัวอย่างสำหรับทดสอบการรวมไฟล์ (ผู้ใช้ต้องสร้าง/วางเอง)
│   ├── dummy_doc2.pdf      # ไฟล์ PDF ตัวอย่างสำหรับทดสอบการรวมไฟล์ (ผู้ใช้ต้องสร้าง/วางเอง)
│   ├── output_report.docx  # ไฟล์ Word ผลลัพธ์ที่โปรแกรมสร้างขึ้น
│   └── merged_output.pdf   # ไฟล์ PDF ผลลัพธ์ที่เกิดจากการรวมไฟล์
├── main.py                 # สคริปต์หลักสำหรับควบคุมและสั่งการทำงานทั้งหมด
└── README.md               # เอกสารอธิบายรายละเอียดของโปรเจกต์
```

## การแก้ไขปัญหาและการค้นหาข้อผิดพลาด (Debugging)

* **`FileNotFoundError`**: ตรวจสอบให้แน่ใจว่าไฟล์ PDF ขาเข้า (`input_article.pdf`, `dummy_doc1.pdf`, `dummy_doc2.pdf`) อยู่ในโฟลเดอร์ `documents` และตั้งชื่อตรงกับที่ระบุไว้ใน `main.py`
* **`PyPDF2.errors.PdfReadError`**: มักเกิดจากไฟล์ PDF เสียหาย, ติดรหัสผ่านที่ไม่อนุญาตให้อ่าน หรือไม่ใช่ไฟล์ PDF ที่สมบูรณ์ ให้ทดลองใช้ไฟล์ PDF ตัวอย่างอื่น
* **เอกสาร Word ว่างเปล่า / เนื้อหาไม่ขึ้น**:
  * ตรวจสอบว่าฟังก์ชัน `pdf_processor.extract_text_from_pdf()` คืนค่าข้อความกลับมาหรือไม่ หากไฟล์ PDF เป็นภาพสแกน (Image-based PDF) `PyPDF2` จะไม่สามารถอ่านข้อความออกมาได้
  * ตรวจสอบว่าคำสั่ง `add_paragraph`, `add_heading`, หรือ `add_table` ทำงานเรียบร้อยก่อนที่จะเรียกคำสั่ง `save_document`
* **ปัญหาการจัดรูปแบบใน Word**:
  * การจัดรูปแบบเฉพาะส่วนข้อความภายในย่อหน้า ต้องอ้างอิงผ่าน `paragraph.runs`
  * การกำหนดขนาดฟอนต์ใน `python-docx` จำเป็นต้องระบุหน่วยด้วย `Pt()` เช่น `Pt(12)`
* **การดู Log การทำงาน**: ระบบมีการใช้โมดูล `logging` เพื่อแสดงสถานะ ให้สังเกตข้อความระดับ `ERROR` หรือ `WARNING` บน Console เพื่อวิเคราะห์จุดที่เกิดปัญหา

## แนวทางการพัฒนาต่อยอด (Extension Ideas)

* **การสร้างเอกสารผ่าน Template**: สร้างไฟล์เทมเพลต Word (`.docx`) ที่มีตัวแปรสำรองไว้ เช่น `{{name}}`, `{{date}}` แล้วใช้ Python ค้นหาและทดแทนที่ข้อมูลจาก Excel/CSV หรือ Database
* **การวิเคราะห์ PDF ขั้นสูง**: ใช้ไลบรารีอื่นเพิ่มเติม เช่น `pdfplumber` หรือ `PyMuPDF` (Fitz) หากต้องการดึงข้อมูลจาก PDF ที่มีเลย์เอาต์ซับซ้อน หรือมีตารางข้อมูล
* **การแปลงไฟล์ข้ามฟอร์แมต**: พัฒนาระบบให้รองรับการแปลงไฟล์ Word เป็น PDF หรือ PDF เป็นรูปภาพ
* **การทำ Mail Merge อัตโนมัติ**: ดึงข้อมูลจากตารางนำมาออกเอกสารเฉพาะบุคคล เช่น ใบรับรอง หรือจดหมายแจ้งเตือน จำนวนมากแบบอัตโนมัติ

---

## แหล่งที่มา (Sources)

1. https://github.com/3000alex/sistema_reportes2.0
2. https://careerkarma.com/blog/automation/
3. https://www.nitw.ac.in/siemens/facilities.html
4. https://www.anhenterprise.com/
5. https://github.com/MikeyBeez/RAGAgent
6. https://automatetheboringstuff.com/2e/chapter15/