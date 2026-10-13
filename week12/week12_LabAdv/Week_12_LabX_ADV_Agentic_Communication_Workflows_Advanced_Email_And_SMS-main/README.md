# Week 12: Lab Advance - เวิร์กโฟลว์การสื่อสารอัตโนมัติด้วยเอเจนต์ (Agentic Communication Workflows - Advanced Email & SMS)

โปรเจกต์ปฏิบัติการขั้นสูงนี้เป็นการยกระดับระบบสื่อสารอัตโนมัติขึ้นสู่ระดับ **Agentic Communication Workflows** ในรายวิชา Script Programming โดยพัฒนาคลาส **`CommunicationAgent`** ที่สามารถจัดลำดับและควบคุมกระบวนการส่งและรับอีเมล ตลอดจนการส่งข้อความ SMS แบบอัตโนมัติตามโครงสร้างการตั้งค่าแบบ Declarative JSON (`configs/comm_pipeline_config.json`) รองรับการสร้างเนื้อหาข้อความแบบไดนามิกผ่านระบบ Template พร้อมการประมวลผลกล่องข้อความขาเข้าตามเงื่อนไข (Rule-Based Inbox Processing) และการบันทึกรายงานประวัติการทำงาน (Audit Logging) ที่ครอบคลุม

> 📹 **วิดีโอสาธิตการทำงาน (Video Demonstration):** [คลิกเพื่อดูวิดีโอสาธิตบน Google Drive](https://drive.google.com/file/d/1IQG5n4ZtnCZXstkHJfyGHwmwLuJx7XBq/view?usp=sharing)  
> URL สำรอง: `https://drive.google.com/file/d/1IQG5n4ZtnCZXstkHJfyGHwmwLuJx7XBq/view?usp=sharing`

---

## ผลลัพธ์การเรียนรู้และแนวคิดหลัก (Key Concepts Demonstrated)

* **สถาปัตยกรรมเอเจนต์การสื่อสาร (Communication Agent Architecture)**:
  * คลาส `CommunicationAgent` ทำหน้าที่เป็นศูนย์กลาง (Central Orchestrator) ในการจัดคิวและกระจายภารกิจ (Task Dispatcher) ไปยังโมดูลผู้เชี่ยวชาญเฉพาะทางตามประเภทงาน
  * รองรับการทำงานแบบไปป์ไลน์อัตโนมัติที่เชื่อมโยงแต่ละ Task เข้าด้วยกัน
* **การกำหนดค่าแบบเปิดเผย (Declarative JSON Configuration)**:
  * กำหนดลำดับขั้นตอนการทำงาน (Workflow Tasks) และพารามิเตอร์ทั้งหมดในไฟล์ `configs/comm_pipeline_config.json` ช่วยให้ปรับเปลี่ยนเงื่อนไขและข้อมูลได้ง่ายโดยไม่ต้องแก้โค้ด Python
  * มีคลาส `ConfigParser` ทำหน้าที่ตรวจสอบความถูกต้องของโครงสร้างฟิลด์และชนิดข้อมูล (Config Validation) ก่อนเริ่มทำงาน
* **การจัดการบริบทและสถานะ (Context Management & State Tracking)**:
  * เอเจนต์เก็บรักษาข้อมูลสถานะภายใน (`self.context`) เพื่อส่งผ่านตัวแปรระหว่างภารกิจ (Chaining Data Flow) เช่น ข้อมูลวันที่รายงาน, ตัวเลขยอดขาย, จำนวนลูกค้า หรือผลลัพธ์ของ Task ก่อนหน้าผ่าน `output_context_key`
* **การสร้างเนื้อหาแบบไดนามิกด้วยแม่แบบ (Dynamic Templating)**:
  * คลาส `TemplateRenderer` นำข้อมูลจาก Context มาแทนที่ตัวแปรใน Subject, Body และ SMS Template ในรูปแบบ `{placeholder}` เช่น `{report_date}`, `${sales_figure:.2f}`
* **ระบบประมวลผลกล่องจดหมายตามเงื่อนไข (Rule-Based Inbox Processing)**:
  * ตรวจสอบและค้นหาอีเมลในกล่องจดหมาย (`INBOX`) ด้วยโพรโทคอล IMAP ตามเกณฑ์ที่ระบุ (`status`, `from_sender`, `subject_contains`)
  * ปรับใช้ระบบเงื่อนไข **If-Then Rules** กับอีเมลแต่ละฉบับที่ตรวจพบ:
    * **เงื่อนไข (Conditions):** `subject_contains`, `body_contains`, `has_attachments`
    * **การดำเนินการ (Actions):** ดาวน์โหลดไฟล์แนบไปยัง `data/incoming_attachments/`, ส่ง SMS แจ้งเตือนฉุกเฉิน (`send_sms_alert`), และตอบกลับอีเมลอัตโนมัติด้วยเทมเพลต (`reply_with_template`)
* **การส่งข้อความ SMS แบบไดนามิก (Enhanced SMS via Gateway)**:
  * คลาส `SMSTasks` ส่ง SMS ไปยังหมายเลขโทรศัพท์หลายหมายเลขพร้อมกันผ่าน Email-to-SMS Gateway โดยเนื้อหาข้อความถูกสร้างขึ้นจากบริบทของเอเจนต์
* **ความปลอดภัยของข้อมูลประจำตัว (Secure Credential Management)**:
  * โหลดข้อมูล Credentials สำคัญ (เช่น `SENDER_EMAIL`, `SENDER_APP_PASSWORD`) จากไฟล์ `.env` ร่วมกับ `python-dotenv` และป้องกันการ Commit ขึ้น Git ด้วย `.gitignore`
* **ระบบบันทึกและตรวจสอบประวัติการทำงาน (Audit Logging & Reporting)**:
  * บันทึกทุกขั้นตอน การตัดสินใจ กฎที่จับคู่สำเร็จ และข้อผิดพลาดลงในระบบ Audit Log
  * ส่งออกรายงานผลสรุปเป็นไฟล์ JSON อัตโนมัติ (`reports/audit_report_comm_YYYYMMDD_HHMMSS.json`)

---

## การติดตั้งและการใช้งาน (Setup & How to Run)

1. **Clone Repository และย้ายเข้าสู่โฟลเดอร์โปรเจกต์:**
   ```bash
   git clone https://github.com/phisit10/673380285-2_Sec1_Script_Programming.git
   cd 673380285-2_Sec1_Script_Programming/week12/week12_LabAdv/Week_12_LabX_ADV_Agentic_Communication_Workflows_Advanced_Email_And_SMS-main
   ```

2. **สร้างและเปิดใช้งาน Virtual Environment:**
   ```bash
   # สร้าง Virtual Environment
   python -m venv venv

   # สำหรับ Windows PowerShell:
   .\venv\Scripts\Activate.ps1
   # สำหรับ Windows Command Prompt:
   venv\Scripts\activate.bat
   # สำหรับ macOS/Linux:
   source venv/bin/activate

   # ติดตั้งไลบรารีที่จำเป็น
   pip install python-dotenv openpyxl
   ```

3. **เตรียมไฟล์และไดเรกทอรีสำหรับทดสอบ (Input Data & Reports):**
   * ตรวจสอบหรือสร้างโฟลเดอร์ที่จำเป็น:
     ```bash
     mkdir -p data/reports data/incoming_attachments configs reports
     ```
   * **`data/reports/sales_report.pdf`**: ไฟล์ PDF ตัวอย่างสำหรับใช้ทดสอบการแนบไฟล์รายงาน
   * **`data/reports/summary_data.xlsx`**: ไฟล์ Excel สรุปข้อมูลยอดขายสำหรับใช้แนบในอีเมล

4. **การตั้งค่า Environment Variables (`.env`):**
   * สร้างไฟล์ `.env` ในโฟลเดอร์โปรเจกต์:
     ```ini
     # Sender Email Credentials (Gmail)
     SENDER_EMAIL=your_email@gmail.com
     SENDER_APP_PASSWORD=your_16_digit_app_password

     # Mail Server Configuration
     SMTP_SERVER=smtp.gmail.com
     SMTP_PORT=587
     IMAP_SERVER=imap.gmail.com

     # Test Recipient Targets
     TEST_RECIPIENT_EMAIL=your_test_recipient@gmail.com
     TEST_SMS_PHONE_NUMBER=1234567890
     TEST_SMS_CARRIER=att
     ```
   * **หมายเหตุสำคัญสำหรับการใช้งาน Gmail:** ต้องเปิดการยืนยันแบบ 2 ขั้นตอน (2-Step Verification) ใน Google Account แล้วสร้าง **App Password (16 หลัก)** นำมากรอกใน `SENDER_APP_PASSWORD`

5. **ตรวจสอบไฟล์กำหนดค่า `configs/comm_pipeline_config.json`:**
   * ตรวจสอบว่าที่อยู่อีเมลผู้รับใน `recipients` และหมายเลขโทรศัพท์ใน `alert_phone_numbers` ถูกตั้งค่าตรงกับบัญชีที่ต้องการทดสอบ

6. **รันสคริปต์หลัก:**
   ```bash
   python main.py
   ```

   **ขั้นตอนการทำงานของเอเจนต์ (Pipeline Execution):**
   * **Task 1 (Send Daily Sales Report Email):** เอเจนต์ดึงข้อมูลวันที่ ยอดขาย และจำนวนลูกค้าจาก Context มาสร้างอีเมลและส่งพร้อมแนบไฟล์ `sales_report.pdf` และ `summary_data.xlsx` ไปยังผู้รับ
   * **Task 2 (Simulate Incoming Request Email):** ส่งอีเมลจำลองคำขอด่วน (Urgent Data Request) เข้าหาตนเอง (`SENDER_EMAIL`) พร้อมแนบไฟล์ เพื่อสร้างข้อมูลจำลองในกล่องข้อความ
   * **Task 3 (Process Incoming Data Requests):**
     * เชื่อมต่อ IMAP เพื่อค้นหาอีเมลคำขอที่เข้ามา
     * ตรวจสอบเงื่อนไขตามกฎ (Rules):
       * หากหัวข้อมีคำว่า "Urgent" และมีไฟล์แนบ -> ส่ง SMS แจ้งเตือนด่วนผ่าน Gateway
       * หากเนื้อความมีคำว่า "new data processing" -> ส่งอีเมลตอบกลับผู้ส่งอัตโนมัติ
     * ดาวน์โหลดไฟล์แนบไปยังโฟลเดอร์ `data/incoming_attachments/` และทำเครื่องหมายว่าอ่านแล้ว (`\Seen`)
   * **Audit Report Generation:** บันทึกประวัติและผลลัพธ์ของทุก Task ลงในโฟลเดอร์ `reports/`

---

## โครงสร้างโปรเจกต์ (Project Structure)

```text
Week_12_LabX_ADV_Agentic_Communication_Workflows_Advanced_Email_And_SMS-main/
├── src/
│   ├── __init__.py               # ตัวระบุ Python Package
│   ├── communication_agent.py    # เอเจนต์หลัก: ควบคุมไปป์ไลน์ กระจายงาน และจัดการ Context
│   ├── email_tasks.py            # ฟังก์ชันจัดการส่ง/รับอีเมลผ่าน SMTP และ IMAP
│   ├── sms_tasks.py              # ฟังก์ชันส่งข้อความ SMS ผ่าน Email-to-SMS Gateway
│   ├── config_parser.py          # โหลดและตรวจสอบความถูกต้องของ JSON Configuration
│   ├── template_renderer.py      # ยูทิลิตีเรนเดอร์ข้อความแม่แบบด้วยตัวแปรจาก Context
│   └── utils.py                  # ฟังก์ชันช่วยเหลือ (Logging, .env, สร้างโฟลเดอร์, บันทึก Audit)
├── configs/
│   └── comm_pipeline_config.json # ไฟล์กำหนดขั้นตอนการทำงานและกฎ (Rules) ของ Agent
├── data/
│   ├── reports/
│   │   ├── sales_report.pdf      # ไฟล์ PDF ตัวอย่างสำหรับแนบในอีเมล
│   │   └── summary_data.xlsx     # ไฟล์ Excel ตัวอย่างสำหรับแนบในอีเมล
│   └── incoming_attachments/     # โฟลเดอร์จัดเก็บไฟล์แนบที่ดาวน์โหลดจากอีเมลขาเข้า
├── reports/
│   └── audit_report_comm_*.json  # [Output] รายงาน Audit Log สรุปผลการทำงานของเอเจนต์
├── .env                          # ไฟล์ Credentials (ไม่ commit ขึ้น Git)
├── .gitignore                    # ไฟล์ยกเว้นการติดตามของ Git
├── main.py                       # สคริปต์หลักสำหรับเริ่มทำงานเอเจนต์
└── README.md                     # เอกสารคู่มือโปรเจกต์
```

---

## การแก้ปัญหาและการตรวจสอบข้อผิดพลาด (Debugging & Troubleshooting)

* **`ValueError: Environment variable '...' not set`**:
  * ตรวจสอบว่ามีไฟล์ `.env` อยู่ในไดเรกทอรี และสะกดชื่อตัวแปรถูกต้อง (`SENDER_EMAIL`, `SENDER_APP_PASSWORD`, `SMTP_SERVER`, ฯลฯ)
* **`SMTPAuthenticationError` หรือ `IMAP4.error (Authentication failed)`**:
  * ให้สร้างและใช้ **Google App Password (16 หลัก)** แทนรหัสผ่านปกติของบัญชี Google
  * ตรวจสอบว่าได้เปิดใช้งาน 2-Step Verification ในบัญชี Google เรียบร้อยแล้ว
* **`SEARCH command error: BAD [Could not parse command]` ใน IMAP**:
  * คำค้นหาที่มีช่องว่าง (เช่น `"Data Request"`) จำเป็นต้องใส่เครื่องหมายคำพูด (Quotes) ครอบไว้ตามมาตรฐานโพรโทคอล IMAP เพื่อป้องกันข้อผิดพลาดในการแยกโทเคนคำสั่ง
* **ไม่พบอีเมลใน Task Process Inbox (`No UNSEEN emails found`)**:
  * ระบบอีเมลของ Gmail เมื่อส่งหาตนเองบางครั้งอาจใช้เวลา 2-5 วินาทีในการส่งมอบ หรือถูกระบุสถานะเป็นอ่านแล้วโดยอัตโนมัติ แนะนำให้เพิ่มการหน่วงเวลา (`time.sleep`) สั้นๆ ก่อนค้นหา และมีระบบค้นหาด้วยเกณฑ์ `ALL` สำรอง
* **ไฟล์แนบไม่ถูกแนบหรือหาไม่พบ (`Attachment file not found`)**:
  * ตรวจสอบว่าพาธของไฟล์แนบใน `comm_pipeline_config.json` อ้างอิงสัมพันธ์กับโฟลเดอร์หลักถูกต้อง และมีไฟล์ `sales_report.pdf` และ `summary_data.xlsx` อยู่จริงใน `data/reports/`
* **การตรวจสอบบันทึกผลการทำงาน (Audit Report)**:
  * สามารถเปิดดูรายละเอียดผลลัพธ์ของแต่ละ Task, ข้อมูลที่ดึงได้ และข้อผิดพลาดอย่างละเอียดได้ที่ไฟล์ `reports/audit_report_comm_*.json`

---

## แนวทางการพัฒนาต่อยอด (Extension Ideas)

* **การเชื่อมต่อกับ Data Agent (Multi-Agent Pipeline)**: นำเอเจนต์ประมวลผลข้อมูล (Data Agent) มาสร้างรายงานอัตโนมัติ แล้วส่งผ่านพาธไฟล์และตัวเลขสรุปมาให้ `CommunicationAgent` เพื่อส่งอีเมลและ SMS ต่อแบบครบวงจร
* **ตัวกระตุ้นจากเหตุการณ์ภายนอก (Event-Driven Triggers / Webhooks)**: ผสานรวมกับไลบรารีตรวจจับไฟล์ เช่น `watchdog` หรือ Webhook Listener เพื่อเริ่มการทำงานของเอเจนต์ทันทีเมื่อมีไฟล์ใหม่หรือมีสัญญาณแจ้งเตือนเข้ามา
* **ระบบจัดการฐานข้อมูล (Database Logging)**: จัดเก็บประวัติการส่งอีเมล ข้อมูลเมทาดาทา และผลการประมวลผลลงในฐานข้อมูล เช่น SQLite หรือ PostgreSQL เพื่อการสืบค้นย้อนหลัง
* **การใช้แม่แบบขั้นสูง (Jinja2 Template Engine)**: เปลี่ยนจากการใช้ `str.format` พื้นฐาน มาเป็น `Jinja2` เพื่อสร้างอีเมล HTML ที่มีลูกเล่นขั้นสูง เช่น การวนลูปแสดงแถวข้อมูลในตาราง และการจัดรูปแบบสไตล์อย่างมืออาชีพ
* **การวิเคราะห์เนื้อหาด้วย NLP (Natural Language Processing)**: นำ NLP เข้ามาวิเคราะห์เจตนา (Intent) และอารมณ์ความรู้สึก (Sentiment) ของอีเมลขาเข้าในขั้นตอน Inbox Processing เพื่อเลือกรูปแบบการตอบกลับอัตโนมัติที่เหมาะสมยิ่งขึ้น
* **การผสานรวม SMS API ระดับสากล**: เชื่อมต่อกับบริการ SMS API เช่น Twilio หรือ Vonage เพื่อให้ส่ง SMS ถึงเบอร์มือถือจริงได้อย่างเสถียรและแม่นยำ พร้อมระบบแจ้งสถานะการส่ง (Delivery Receipts)

---

## แหล่งที่มา (References)

1. [Cernurt/INF876_Automne2023](https://github.com/Cernurt/INF876_Automne2023)
2. [Metal Toad - AWS CodeWhisperer ML-Augmented Development](https://www.metaltoad.com/blog/aws-codewhisperer-ml-augmented-development-3-3)
3. [B2B-GJR-Nestle/B2BEmailBlast](https://github.com/B2B-GJR-Nestle/B2BEmailBlast)
4. [Automate the Boring Stuff with Python - Chapter 18: Sending Email and Text Messages](https://automatetheboringstuff.com/2e/chapter18/)
