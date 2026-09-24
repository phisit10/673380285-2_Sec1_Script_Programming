# Week 7: Lab Advanced 1 - Advanced Web Scraping & Introduction to Automated Agents

โปรเจกต์นี้เป็นการสร้าง Web Scraper ขั้นสูงที่มีลักษณะการทำงานแบบ "Agent" โดยอาศัย `Selenium` สำหรับจัดการกับเว็บไซต์ที่มีเนื้อหาแบบไดนามิก (Dynamic content) และใช้แนวทางแบบ Configuration-driven เพื่อให้บอทมีความยืดหยุ่น โปรเจกต์นี้สาธิตวิธีการควบคุมเบราว์เซอร์อัตโนมัติ การดึงข้อมูลที่มีโครงสร้าง การจัดการการเปลี่ยนหน้าเว็บ (Pagination) และการบันทึกข้อมูลอย่างเป็นระบบ

## แนวคิดสำคัญ (Key Concepts Demonstrated)

* **Selenium สำหรับเนื้อหาไดนามิก**: ควบคุมเบราว์เซอร์จริง (แบบมีหน้าต่างหรือ Headless) เพื่อดึงข้อมูลเว็บที่เรนเดอร์ด้วย JavaScript
* **การจัดการ WebDriver**: ติดตั้งและตั้งค่าเบราว์เซอร์ไดรเวอร์อัตโนมัติด้วย `webdriver_manager`
* **ระบบทำงานผ่านคอนฟิก (Config-Driven Automation)**: กำหนดพฤติกรรมของ Scraper (เป้าหมายและวิธีการดึงข้อมูล) ไว้ในไฟล์ JSON ภายนอก ทำให้สามารถนำไปปรับใช้กับเว็บไซต์อื่นได้โดยไม่ต้องแก้โค้ด Python เลย
* **การออกแบบ Agent แบบโมดูลาร์ (Modular Agent Design)**: แยกตรรกะการทำงานออกเป็นส่วนๆ เช่น `scraper_agent`, `config_parser`, `data_models`, `utils`, และ `driver_manager` เพื่อให้โค้ดอ่านและดูแลรักษาง่าย
* **ความเสถียร (Robustness)**: ใช้งานกลไกการรอ (Explicit waits), การลองคลิกซ้ำ (Retry mechanisms) และการดักจับข้อผิดพลาดพื้นฐาน (Error handling) สำหรับปัญหาเครือข่ายหรือหน้าเว็บโหลดไม่สมบูรณ์
* **ข้อมูลที่มีโครงสร้าง (Structured Data)**: แปลงข้อมูลที่ดึงมาให้อยู่ในรูปแบบ Python dataclasses และบันทึกผลลัพธ์ออกเป็นไฟล์ JSON

## ข้อควรระวังด้านจริยธรรมและกฎหมาย (Ethical and Legal Considerations)

**โปรดทำความเข้าใจและปฏิบัติตามแนวทางด้านจริยธรรมและกฎหมายอย่างเคร่งครัดในการทำ Web Scraping:**

* **`robots.txt`**: ตรวจสอบไฟล์ `robots.txt` ของเว็บไซต์เสมอ (เช่น `https://example.com/robots.txt`) เพื่อดูว่าส่วนใดอนุญาตหรือไม่อนุญาตให้บอทเข้าถึง
* **ข้อกำหนดการให้บริการ (Terms of Service - ToS)**: ตรวจสอบข้อตกลงของเว็บไซต์ เว็บไซต์หลายแห่งระบุชัดเจนว่าไม่อนุญาตให้ทำการดึงข้อมูลด้วยบอท
* **การจำกัดอัตราการดึงข้อมูล (Rate Limiting)**: อย่าส่งคำขอ (Request) ไปยังเซิร์ฟเวอร์เป้าหมายมากเกินไปในเวลาอันสั้น ควรใช้ `time.sleep()` หรือ Waits ของ Selenium (ตามที่อยู่ใน `scraper_agent.py`) เพื่อหน่วงเวลา
* **การนำข้อมูลไปใช้**: พึงระวังเรื่องสิทธิ์ในทรัพย์สินทางปัญญา โดยทั่วไปคุณไม่สามารถนำข้อมูลที่ดึงมาไปเผยแพร่ต่อหรือแสวงหากำไรโดยไม่ได้รับอนุญาต
* **ความถูกต้องตามกฎหมาย**: โปรเจกต์นี้จัดทำขึ้นเพื่อ **วัตถุประสงค์ทางการศึกษาเท่านั้น** หากมีข้อสงสัยควรหลีกเลี่ยงการกระทำที่สุ่มเสี่ยง

## วิธีการติดตั้งและการใช้งาน (Setup & How to Run)

1. **โคลน Repository ลงมาที่เครื่อง:**

```bash
git clone https://github.com/phisit10/673380285-2_Sec1_Script_Programming.git
cd 673380285-2_Sec1_Script_Programming/week7/LabAdv1
```

2. **ติดตั้ง Dependencies:**
   แนะนำให้สร้าง Virtual Environment ก่อนการติดตั้งแพ็กเกจ:

```bash
python -m venv venv

# สำหรับ Windows:
venv\Scripts\activate.bat
# สำหรับ Mac/Linux:
source venv/bin/activate

pip install -r requirement.txt
```

3. **เตรียมพร้อม Browser และ WebDriver:**

* ระบบจะใช้ `webdriver_manager` เพื่อดาวน์โหลด WebDriver ให้ตรงเวอร์ชันกับเบราว์เซอร์ของคุณโดยอัตโนมัติ
* ตรวจสอบให้แน่ใจว่าคุณติดตั้ง **Google Chrome** หรือ **Mozilla Firefox** ไว้ในเครื่องแล้ว

4. **การตั้งค่าใน `configs/example_site_config.json`:**

* ไฟล์นี้ใช้สำหรับตั้งค่าว่า Scraper จะดึงข้อมูลอะไรและทำอย่างไร (ค่าเริ่มต้นตั้งไว้สำหรับดึงข้อมูลหนังสือจาก `books.toscrape.com`)
* **จุดสำคัญ:** คุณต้องปรับแก้ตัวเลือก Selectors ตามโครงสร้าง HTML ของเว็บไซต์เป้าหมาย โดยใช้ Developer Tools (F12) บนเบราว์เซอร์ของคุณ

5. **รันโปรแกรม Scraper:**

```bash
python main.py
```

Scraper จะทำการเปิดเบราว์เซอร์ขึ้นมา (ค่าเริ่มต้นคือทำงานเบื้องหลังแบบ Headless) เข้าสู่เว็บไซต์ ดึงข้อมูล และบันทึกผลลัพธ์ลงไปที่ `data/scraped_products.json`

## โครงสร้างโปรเจกต์ (Project Structure)

```text
LabAdv1/
├── src/
│   ├── __init__.py         # มาร์กเกอร์บอกว่าเป็น Python package
│   ├── scraper_agent.py    # ตรรกะหลัก: อ่านคอนฟิก, ควบคุมการท่องเว็บ, ดึงข้อมูล, เปลี่ยนหน้า
│   ├── config_parser.py    # โหลดและตรวจสอบความถูกต้องของไฟล์ JSON
│   ├── data_models.py      # คลาสสำหรับจัดการโครงสร้างข้อมูลที่ดึงมา
│   ├── utils.py            # ฟังก์ชันย่อย (บันทึกไฟล์, รอหน้าเว็บ, จัดการการคลิกที่ซับซ้อน)
│   └── driver_manager.py   # จัดการการตั้งค่าและปิดการทำงานของ Selenium WebDriver
├── configs/
│   └── example_site_config.json # ไฟล์กฎการดึงข้อมูลเฉพาะเว็บไซต์
├── data/
│   └── scraped_products.json    # ไฟล์ผลลัพธ์ที่ได้จากการดึงข้อมูล
├── main.py                 # จุดเริ่มต้นแอปพลิเคชันสำหรับการรัน (Entry point)
├── .gitignore              # ไฟล์และโฟลเดอร์ที่ไม่ต้องการนำเข้า Git
├── README.md               # ไฟล์อธิบายภาพรวมของโปรเจกต์ (ไฟล์นี้)
└── docs/
    └── ETHICS.md           # ข้อควรปฏิบัติเกี่ยวกับจริยธรรมและข้อกฎหมายในการทำ Web Scraping
```

## การแก้ปัญหาเบื้องต้น (Debugging Advanced Web Scraping)

* **ข้อผิดพลาด WebDriver (`WebDriverException`, `SessionNotCreatedException`)**: มักเกิดจากการหาไดรเวอร์ไม่เจอ หรือเวอร์ชันเบราว์เซอร์อัปเดตไม่ตรงกัน ตรวจสอบให้แน่ใจว่าติดตั้ง `webdriver-manager` แล้ว และอัปเดตเบราว์เซอร์ให้เป็นเวอร์ชันล่าสุด
* **หา Element ไม่เจอ (`NoSuchElementException`)**: CSS Selector หรือ XPath ไม่ถูกต้อง หรือหน้าเว็บส่วนนั้นยังโหลดไม่เสร็จ

  * *วิธีแก้*: ใช้ DevTools (F12) เพื่อตรวจสอบ Selectors ใหม่ และเพิ่มคำสั่ง Explicit waits (`WebDriverWait`) เพื่อรอให้หน้าเว็บพร้อมก่อนเข้าถึง
* **ข้อผิดพลาดรอจนหมดเวลา (`TimeoutException`)**: Element ไม่แสดงขึ้นมาภายในเวลาที่กำหนด

  * *วิธีแก้*: ลองเพิ่มเวลารอ (Timeout) หรือสังเกตว่าเว็บโหลดช้าจริงๆ หรือเกิดจากปัจจัยอื่น
* **Stale Element Reference (`StaleElementReferenceException`)**: Element ที่เคยดึงมาหลุดจากการเชื่อมต่อกับ DOM (เช่น หน้ารีเฟรชตัวเอง)

  * *วิธีแก้*: ให้ทำการค้นหา Element ชิ้นนั้นใหม่อีกครั้ง (Re-find) หลังจากโหลดหน้าเว็บหรือโหลด AJAX เสร็จ
* **การเปลี่ยนหน้าวนลูปไม่รู้จบ (Infinite Pagination Loops)**: Scraper หาปุ่ม "หน้าถัดไป" เจอเสมอแม้จะถึงหน้าสุดท้ายแล้ว

  * *วิธีแก้*: ตรวจสอบสถานะปุ่ม Next ในหน้าสุดท้าย มักจะมีการเปลี่ยนคลาสเป็น disabled หรือหายไป ให้เพิ่มเงื่อนไขตรวจเช็คจุดนี้ด้วย
* **ปัญหาการทำงานแบบ Headless**: หากเจอปัญหาเฉพาะเมื่อรันแบบซ่อนเบราว์เซอร์ ให้ลองเปลี่ยนเป็น `headless=False` ใน `main.py` เพื่อดูว่าบอทกำลังติดปัญหาที่หน้าต่างไหน

## ไอเดียการพัฒนาต่อยอด (Extension Ideas / Future Work)

* **เพิ่มความเสถียรป้องกันการถูกบล็อก**: ใส่ระบบ Proxy rotation, การสุ่มแก้ CAPTCHA ด้วยบริการภายนอก หรือใช้กลยุทธ์การสลับ User-Agent
* **เชื่อมต่อระบบจัดการข้อมูล (Data Pipelines)**: เปลี่ยนจากบันทึกลง JSON ไปบันทึกลงฐานข้อมูล เช่น SQLite, PostgreSQL หรือ Cloud Storage แทน
* **การจัดการและแจ้งเตือนข้อผิดพลาด**: เพิ่มระบบ Logging อย่างละเอียด และตั้งให้ส่งอีเมลแจ้งเตือนเมื่อระบบรันล้มเหลว
* **Scraping แบบคู่ขนาน (Concurrent Scraping)**: ใช้ `threading` หรือ `asyncio` เพื่อดึงข้อมูลหลายหน้าพร้อมๆ กัน (ต้องจัดการเรื่อง Rate limiting ให้ดี)
* **การประยุกต์ใช้งานร่วมกับ AI (Advanced AI Integration)**:

  * **LLM-driven Selector Generation**: ใช้ LLM สร้าง Selector จากคำสั่งทั่วไป เช่น "ช่วยดึงราคาสินค้าจากหน้านี้ให้หน่อย"
  * **Adaptive Navigation**: ให้ LLM ตัดสินใจเองว่าจะคลิกอะไรต่อไปตามจุดประสงค์ที่ตั้งไว้
  * **Failure Recovery**: ให้ AI ช่วยกู้คืนข้อผิดพลาดอัตโนมัติเวลาเว็บมีการเปลี่ยนโครงสร้าง HTML

---

## แหล่งอ้างอิง

- Automate the Boring Stuff with Python, 2nd Edition - Chapter 12: Web Scraping: https://automatetheboringstuff.com/2e/chapter12/

## แหล่งที่มา

1. https://devpress.csdn.net/python/63051124c67703293080ea76.html
2. https://github.com/BobTheSnob1/dominion_staff_timeline
3. https://github.com/MikeyBeez/RAGAgent
4. https://automatetheboringstuff.com/2e/chapter12/

