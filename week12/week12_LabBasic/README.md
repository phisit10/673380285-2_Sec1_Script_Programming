# Week 12: Lab Basic - การสื่อสารอัตโนมัติด้วย Python (Email & SMS)

โปรเจกต์ปฏิบัติการนี้สาธิตและใช้งานระบบสื่อสารอัตโนมัติ (Automated Communication System) ในรายวิชา Script Programming โดยใช้ภาษา Python ในการส่งและรับอีเมลผ่านโพรโทคอลมาตรฐานเครือข่าย ได้แก่ **SMTP (Simple Mail Transfer Protocol)** สำหรับการส่งอีเมล และ **IMAP (Internet Message Access Protocol)** สำหรับการรับและประมวลผลอีเมล ตลอดจนการส่งข้อความ SMS ผ่าน **Email-to-SMS Gateway** ของผู้ให้บริการเครือข่าย โดยให้ความสำคัญสูงสุดกับการรักษาความปลอดภัยของข้อมูลประจำตัว (Credentials) ผ่านตัวแปรสภาพแวดล้อม (Environment Variables)

---

## ผลลัพธ์การเรียนรู้และแนวคิดหลัก (Key Concepts Demonstrated)

* **การส่งอีเมลด้วยโพรโทคอล SMTP (`smtplib`)**:
  * การเชื่อมต่อไปยัง SMTP Server (เช่น Gmail SMTP: `smtp.gmail.com:587`)
  * การรักษาความปลอดภัยของช่องทางสื่อสารด้วยการเข้ารหัส STARTTLS
  * การยืนยันตัวตน (Authentication) ผ่าน App Password ของบัญชีผู้ใช้
  * การจัดโครงสร้างอีเมลด้วยแพ็กเกจ `email.mime`:
    * `MIMEText`: สำหรับเนื้อหาข้อความแบบ Plain Text และ HTML
    * `MIMEApplication`: สำหรับไฟล์แนบ (เช่น เอกสาร PDF)
    * `MIMEMultipart`: สำหรับรวมข้อความและไฟล์แนบเข้าด้วยกันในฉบับเดียว
    * การกำหนดค่า Header สำคัญ (`From`, `To`, `Subject`)

* **การรับและประมวลผลอีเมลด้วยโพรโทคอล IMAP (`imaplib`)**:
  * การเชื่อมต่อไปยัง IMAP Server แบบปลอดภัยผ่าน SSL (`imaplib.IMAP4_SSL`) พอร์ต 993
  * การเลือกและเข้าถึงกล่องจดหมาย (`INBOX`)
  * การค้นหาอีเมลตามเงื่อนไข (Search Criteria): `UNSEEN`, `ALL`, กรองตามผู้ส่ง (`FROM`), และหัวข้อ (`SUBJECT`)
  * การดึงและแยกชิ้นส่วนข้อความ (Fetch & Parse) ตามมาตรฐาน RFC822
  * การถอดรหัสข้อความและหัวเรื่องภาษาไทย/อักขระพิเศษด้วย `email.header.decode_header`
  * การเดินท่องโครงสร้าง MIME (`msg.walk()`) เพื่อดึงเนื้อความและดาวน์โหลดไฟล์แนบอัตโนมัติ
  * การทำเครื่องหมายว่าอ่านแล้ว (`\Seen`) หลังประมวลผลสำเร็จ

* **การส่งข้อความ SMS ผ่าน Email-to-SMS Gateway (`sms_gateway.py`)**:
  * การทำความเข้าใจโครงสร้างเกตเวย์ของผู้ให้บริการเครือข่ายโทรศัพท์เคลื่อนที่ (เช่น `[phone_number]@txt.att.net`)
  * การแปลงหมายเลขโทรศัพท์และชื่อเครือข่ายให้เป็นที่อยู่อีเมลเกตเวย์เพื่อส่งข้อความ SMS ผ่านโพรโทคอล SMTP โดยตรง

* **การจัดการความปลอดภัยและข้อมูลประจำตัว (Secure Credential Handling)**:
  * การใช้ไฟล์ `.env` ร่วมกับไลบรารี `python-dotenv` ในการโหลดค่า Sensitive Data เข้าสู่ระบบ
  * หลีกเลี่ยงการ Hardcode ข้อมูลสำคัญ (เช่น อีเมล, รหัสผ่านแอป) ในซอร์สโค้ด
  * การใช้ไฟล์ `.gitignore` เพื่อป้องกันการ Commit ไฟล์ `.env` ขึ้นสู่ Public Repository

* **การออกแบบเชิงโมดูลและความเสถียร (Modular Design & Logging)**:
  * การแยกโค้ดออกเป็นโมดูลย่อยตามหน้าที่ (`email_sender.py`, `email_receiver.py`, `sms_gateway.py`, `utils.py`)
  * การใช้โมดูล `logging` แสดงผลการทำงานอย่างละเอียด พร้อมการดักจับข้อผิดพลาด (Exception Handling) เช่น การตรวจสอบไฟล์แนบ และการเชื่อมต่อเครือข่าย

---

## การติดตั้งและการใช้งาน (Setup & How to Run)

1. **Clone Repository และย้ายเข้าสู่โฟลเดอร์โปรเจกต์:**
   ```bash
   git clone https://github.com/phisit10/673380285-2_Sec1_Script_Programming.git
   cd 673380285-2_Sec1_Script_Programming/week12/week12_LabBasic/email-sms-automator
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

   # ติดตั้งไลบรารีที่จำเป็น (python-dotenv)
   pip install -r requirements.txt
   ```

3. **เตรียมไฟล์และโฟลเดอร์ข้อมูล (Input Data Files):**
   * ตรวจสอบว่ามีโฟลเดอร์ `data/attachments` สำหรับบันทึกไฟล์แนบที่ดาวน์โหลดจากอีเมล:
     ```bash
     mkdir -p data/attachments
     ```
   * วางไฟล์ PDF ตัวอย่างชื่อ `dummy_report.pdf` ไว้ในโฟลเดอร์ `data/` เพื่อใช้ทดสอบการส่งไฟล์แนบ

4. **การตั้งค่า Environment Variables (`.env`):**
   * คัดลอกไฟล์ตัวอย่าง `.env.example` มาสร้างเป็นไฟล์ `.env`:
     ```bash
     cp .env.example .env
     ```
   * **ขั้นตอนการสร้าง Gmail App Password (จำเป็นสำหรับ 2-Factor Authentication):**
     1. เข้าสู่บัญชี Google Account (https://myaccount.google.com/)
     2. ไปที่เมนู **ความปลอดภัย (Security)**
     3. ตรวจสอบว่าได้เปิดใช้งาน **การยืนยันแบบ 2 ขั้นตอน (2-Step Verification)** แล้ว
     4. ค้นหาหรือเลือก **รหัสผ่านสำหรับแอป (App passwords)**
     5. สร้างรหัสผ่านใหม่ (เช่น ตั้งชื่อแอปว่า "Python Automator")
     6. คัดลอกรหัสผ่าน 16 หลักนำมากรอกในไฟล์ `.env`
   * กำหนดค่าตัวแปรในไฟล์ `.env` ดังนี้:
     ```ini
     # Sender Email Credentials (Gmail)
     SENDER_EMAIL=your_email@gmail.com
     SENDER_APP_PASSWORD=your_16_character_app_password

     # Mail Server Configuration
     SMTP_SERVER=smtp.gmail.com
     SMTP_PORT=587
     IMAP_SERVER=imap.gmail.com

     # Test Recipient Targets
     TEST_RECIPIENT_EMAIL=your_test_recipient@gmail.com
     TEST_SMS_PHONE_NUMBER=1234567890
     TEST_SMS_CARRIER=att
     ```

5. **รันโปรแกรมหลัก:**
   ```bash
   python main.py
   ```

   **ขั้นตอนการทำงานของโปรแกรม (Execution Workflow):**
   * **Task 1 (Plaintext Email):** ส่งอีเมลข้อความธรรมดาไปยัง `TEST_RECIPIENT_EMAIL`
   * **Task 2 (Email with Attachment):** ส่งอีเมลพร้อมแนบไฟล์ `data/dummy_report.pdf` ไปยัง `TEST_RECIPIENT_EMAIL`
   * **Task 3 (SMS via Gateway):** ส่งข้อความ SMS ไปยังหมายเลขปลายทางผ่าน Email-to-SMS Gateway ของเครือข่ายที่ระบุ
   * **Task 4 (Receive & Process Email):**
     * ส่งอีเมลทดสอบหาตนเอง (`SENDER_EMAIL`) พร้อมแนบไฟล์
     * รอให้อีเมลเข้าสู่ระบบ จากนั้นเชื่อมต่อ IMAP เพื่อค้นหาอีเมลที่ยังไม่ได้อ่าน (`UNSEEN`)
     * อ่านและแสดงข้อมูลผู้ส่ง, หัวข้อ, และตัวอย่างข้อความ (Body Snippet)
     * ดาวน์โหลดไฟล์แนบลงในโฟลเดอร์ `data/attachments/`
     * ทำเครื่องหมายว่าอ่านแล้ว (`\Seen`)

---

## โครงสร้างโปรเจกต์ (Project Structure)

```text
week12_LabBasic/
├── email-sms-automator/
│   ├── src/
│   │   ├── __init__.py          # เครื่องหมายระบุว่าเป็น Python Package
│   │   ├── email_sender.py      # คลาส EmailSender จัดการส่งอีเมลผ่าน SMTP (รองรับ TLS, HTML, ไฟล์แนบ)
│   │   ├── email_receiver.py    # คลาส EmailReceiver จัดการรับ/ค้นหา/อ่านอีเมลผ่าน IMAP และดาวน์โหลดไฟล์แนบ
│   │   ├── sms_gateway.py       # คลาส SMSGateway จัดการส่งข้อความ SMS ผ่าน Email-to-SMS Gateways
│   │   └── utils.py             # ฟังก์ชันช่วยเหลือ (Logging, โหลด Environment Variables, ตรวจสอบไดเรกทอรี)
│   ├── data/
│   │   ├── attachments/         # ไดเรกทอรีสำหรับเก็บไฟล์แนบที่ดาวน์โหลดจากอีเมล
│   │   │   └── .gitkeep
│   │   └── dummy_report.pdf     # ไฟล์ตัวอย่าง PDF สำหรับใช้ทดสอบการแนบไฟล์
│   ├── tests/
│   │   └── test_automator.py    # Unit Test Suite จำลองการทำงานทุกโมดูลแบบ Offline
│   ├── .env                     # ไฟล์จัดเก็บ Credentials และการตั้งค่าระบบ (ไม่ commit ขึ้น Git)
│   ├── .env.example             # ไฟล์ตัวอย่างโครงสร้าง Environment Variables
│   ├── .gitignore               # รายการไฟล์และโฟลเดอร์ที่ยกเว้นจากการติดตามของ Git
│   ├── main.py                  # สคริปต์หลักสำหรับควบคุมการทำงานทั้ง 4 Tasks
│   ├── requirements.txt         # รายการแพ็กเกจไลบรารีภายนอก (python-dotenv)
│   └── README.md                # เอกสารคู่มือโปรเจกต์ email-sms-automator
├── week12_LabBasic_Result/
│   └── image.png                # ภาพผลลัพธ์การรันโปรแกรม
├── .env                         # ไฟล์ Environment Variables ประจำโฟลเดอร์แล็บ
├── .gitignore                   # กำหนดรายการไฟล์ที่ไม่ต้องการ commit ขึ้น Git
└── README.md                    # เอกสารอธิบายรายละเอียดและวิธีการใช้งานแล็บ
```

---

## การแก้ปัญหาและการตรวจสอบข้อผิดพลาด (Debugging & Troubleshooting)

* **`ValueError: Environment variable '...' not set`**:
  * ตรวจสอบว่าได้สร้างไฟล์ `.env` ไว้ในไดเรกทอรีที่ถูกต้องแล้วหรือไม่
  * ตรวจสอบการสะกดชื่อตัวแปรใน `.env` ให้ตรงกับที่โปรแกรมเรียกใช้ เช่น `SENDER_EMAIL`, `SENDER_APP_PASSWORD`
* **`SMTPAuthenticationError` หรือ `IMAP4.error (Authentication failed)`**:
  * **สาเหตุที่พบบ่อยที่สุด:** กรอก App Password ไม่ถูกต้อง หรือใช้รหัสผ่านปกติของบัญชี Google แทนการใช้ **Google App Password (16 หลัก)**
  * ตรวจสอบว่าบัญชีได้เปิดใช้งาน 2-Step Verification เรียบร้อยแล้ว
* **`SMTPConnectError` หรือการเชื่อมต่อล้มเหลว (Connection Timeout)**:
  * ตรวจสอบค่า `SMTP_SERVER` (`smtp.gmail.com`), `SMTP_PORT` (`587`), และ `IMAP_SERVER` (`imap.gmail.com`)
  * ตรวจสอบการเชื่อมต่ออินเทอร์เน็ต และตรวจสอบว่า Firewall หรือโครงข่ายไม่ได้บล็อกพอร์ต 587 หรือ 993
* **อีเมลไม่ปรากฏในกล่องข้อความปลายทาง**:
  * ตรวจสอบในโฟลเดอร์ Spam / จดหมายขยะ ของอีเมลผู้รับ
  * ตรวจสอบสถานะการส่งใน Console Log ว่าฟังก์ชันส่งอีเมลคืนค่า `True` หรือไม่
* **ปัญหาการส่งและดาวน์โหลดไฟล์แนบ (Attachments)**:
  * ตรวจสอบว่าไฟล์ `dummy_report.pdf` มีอยู่จริงในไดเรกทอรี `data/`
  * ตรวจสอบสิทธิ์การเขียนไฟล์ในโฟลเดอร์ `data/attachments/`
* **ข้อความ SMS ไม่เข้าโทรศัพท์มือถือ**:
  * ตรวจสอบว่าระบุเครือข่าย (`TEST_SMS_CARRIER`) ถูกต้อง และเครือข่ายนั้นรองรับ Email-to-SMS Gateway
  * ในบางเครือข่าย ข้อความจากเกตเวย์อาจถูกระบบกรองสแปมบล็อกไว้

---

## แนวทางการพัฒนาต่อยอด (Extension Ideas)

* **ระบบแจ้งเตือนตามกำหนดเวลา (Scheduled Notifications)**: นำไลบรารีตั้งเวลา เช่น `schedule` หรือ `APScheduler` มาเชื่อมต่อเพื่อส่งรายงานประจำวันหรือข้อความเตือนความจำโดยอัตโนมัติ
* **การสร้างเนื้อหาอีเมลแบบไดนามิก (Dynamic Email Templating)**: ประยุกต์ใช้ Template Engine เช่น `Jinja2` เพื่อสร้างอีเมลรูปแบบ HTML ที่ปรับเปลี่ยนข้อมูลรายบุคคลได้ตามฐานข้อมูล
* **ระบบโต้ตอบผ่านคำสั่งในอีเมล (Interactive Email Processing)**: ออกแบบระบบที่สามารถอ่านคีย์เวิร์ดในหัวข้ออีเมล (เช่น `STATUS`, `REPORT`) แล้วดึงข้อมูลตอบกลับผู้ส่งโดยอัตโนมัติ
* **การผสานรวม SMS API ระดับ Production**: พัฒนาต่อยอดโดยเปลี่ยนมาใช้บริการ SMS API มาตรฐาน เช่น Twilio, Vonage หรือ ThaiBulkSMS เพื่อความแม่นยำและการตรวจสอบรายงานผลการส่ง (Delivery Reports)
* **ระบบแจ้งเตือนข้อผิดพลาดฉุกเฉิน (Automated Error Alerting)**: พัฒนาระบบให้ส่งอีเมลหรือ SMS แจ้งเตือนแอดมินทันทีเมื่อเซิร์ฟเวอร์หรือสคริปต์ตรวจพบข้อผิดพลาดร้ายแรง (Critical Error)

---

## แหล่งที่มา (References)

1. [GustavoFulber/Notas-Profesores](https://github.com/GustavoFulber/Notas-Profesores)
2. [B2B-GJR-Nestle/B2BEmailBlast](https://github.com/B2B-GJR-Nestle/B2BEmailBlast)
3. [AlexaneTrubert/discord-email-bot](https://github.com/AlexaneTrubert/discord-email-bot)
4. [AhmedB102/News-GPT-Project](https://github.com/AhmedB102/News-GPT-Project)
5. [Automate the Boring Stuff with Python - Chapter 18: Sending Email and Text Messages](https://automatetheboringstuff.com/2e/chapter18/)
