# Week 7: Introduction to Web Scraping

โปรเจกต์นี้แนะนำพื้นฐานของ Web Scraping โดยใช้ไลบรารี `requests` และ `BeautifulSoup4` ของ Python สาธิตวิธีการดาวน์โหลดเนื้อหา HTML จากเว็บไซต์ และดึงข้อมูลตามโครงสร้าง HTML

**ข้อควรระวังด้านจริยธรรมและกฎหมาย:**
ควรตรวจสอบไฟล์ `robots.txt` ของเว็บไซต์เสมอ (เช่น `https://example.com/robots.txt`) และข้อกำหนดการให้บริการ (Terms of Service) ของเว็บไซต์นั้นๆ เคารพข้อจำกัดอัตราการเข้าถึง (rate limit) และหลีกเลี่ยงการส่ง request จำนวนมากจนเป็นภาระต่อเซิร์ฟเวอร์ โปรเจกต์นี้จัดทำขึ้นเพื่อการศึกษาเท่านั้น และไม่ควรนำไปใช้เพื่อการเก็บข้อมูลโดยไม่ได้รับอนุญาตหรือในทางที่ไม่เหมาะสม

## ฟีเจอร์ที่ทำ

* **ดาวน์โหลด HTML**: ใช้ไลบรารี `requests` เพื่อดึงเนื้อหาหน้าเว็บ
* **แปลง HTML**: ใช้ `BeautifulSoup4` แปลง (parse) เนื้อหา HTML ที่ดาวน์โหลดมา
* **ดึงข้อมูล**: ดึงชื่อหนังสือหลักและรายการชื่อบท (chapter titles) จากหน้าเว็บไซต์ "Automate the Boring Stuff with Python" (ฉบับที่ 3)
* **จัดการข้อผิดพลาด**: มีการดักจับข้อผิดพลาดพื้นฐานสำหรับปัญหาเครือข่ายและ HTTP response ต่างๆ (HTTP error, connection error, timeout)

## วิธีการรัน

1. **Clone repository:**

   ```bash
   git clone https://github.com/phisit10/673380285-2_Sec1_Script_Programming.git
   cd 673380285-2_Sec1_Script_Programming/week7/LabBasic1
   ```
2. **ติดตั้ง Dependencies:**
   แนะนำให้สร้าง virtual environment ก่อนติดตั้ง:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # บน Windows: .venv\Scripts\activate
   pip install -r requirement.txt
   ```
3. **รันตัว scraper:**

   ```bash
   python main.py
   ```

   สคริปต์จะพิมพ์ชื่อหนังสือและรายชื่อบทที่ scrape ได้ออกทาง console

## โครงสร้างโปรเจกต์

```
LabBasic1/
├── src/
│   ├── __init__.py         # ทำให้ 'src' เป็น Python package
│   └── scraper.py          # โค้ด logic หลักของ web scraping (SimpleWebScraper)
├── main.py                 # จุดเริ่มต้นของแอปพลิเคชัน
├── requirement.txt         # รายการ dependencies ที่ต้องติดตั้ง
├── week7_LabBasic_Result/  # ภาพผลลัพธ์การรันโปรแกรม
└── README.md                # ไฟล์นี้
```

## ผลลัพธ์ที่ได้

เป้าหมายของ scraper คือหน้า `https://automatetheboringstuff.com/3e/` ซึ่งดึงข้อมูลออกมาได้ดังนี้:

- **ชื่อหนังสือ:** 3rd Edition
- **ชื่อบท:** รายการบทที่ 1–24 พร้อมภาคผนวก A และ B ของหนังสือ (เช่น Introduction, Python Basics, Loops, Web Scraping, PDF and Word Documents, Controlling the Keyboard and Mouse ฯลฯ) รวมทั้งหมด 27 หัวข้อ

ดูภาพหน้าจอผลลัพธ์การรันจริงได้ที่ `week7_LabBasic_Result/week7_LabBasic_Result.png`

## การ Debug Web Scraping

* **ตรวจสอบ HTML:** ใช้ developer tools ของเบราว์เซอร์ (F12 หรือ Ctrl+Shift+I) เพื่อดูโครงสร้าง HTML ของหน้าที่ต้องการ scrape เพื่อหา tag, class, หรือ id ที่ถูกต้องสำหรับใช้กับ `BeautifulSoup`
* **พิมพ์ `response.status_code`:** ตรวจสอบว่า request สำเร็จ (200 OK) หรือมีปัญหา (เช่น 403 Forbidden, 404 Not Found)
* **พิมพ์ `response.text`:** บางครั้งการพิมพ์เนื้อหา HTML ดิบจะช่วยให้เห็นว่าได้ข้อมูลตามที่คาดไว้หรือไม่ โดยเฉพาะเมื่อการ parse ล้มเหลว
* **ตรวจสอบค่า `None`:** เมื่อใช้ `find()` หรือ `select()` ควรตรวจสอบเสมอว่าผลลัพธ์เป็น `None` หรือไม่ ก่อนเข้าถึง attribute หรือ text ของ element เพื่อป้องกัน `AttributeError`
* **User-Agent:** บางเว็บไซต์บล็อก request ที่ไม่มี `User-Agent` header การเพิ่ม header เช่น `headers = {'User-Agent': '...'}` จะช่วยแก้ปัญหานี้ได้ (โปรเจกต์นี้ตั้งค่า User-Agent ไว้แล้วใน `scraper.py`)
* **Rate Limiting:** หากส่ง request ถี่เกินไป เว็บไซต์อาจบล็อกชั่วคราว ควรเพิ่ม `time.sleep()` ระหว่าง request (import `time`)

## แนวทางต่อยอด

* **บันทึกข้อมูลลงไฟล์**: ปรับ `scraper.py` ให้บันทึกข้อมูลที่ดึงมาลงไฟล์ CSV หรือ JSON
* **Scrape หลายหน้า**: ขยายให้ scraper สามารถไล่ดึงข้อมูลจากหลายหน้าได้ (เช่น เดินหน้าไปตามหน้าถัดไปของบล็อก)
* **ดึงข้อมูลเพิ่มเติม**: นอกจากชื่อบทแล้ว อาจดึงลิงก์ วันที่ ผู้เขียน หรือเนื้อหาบทความเพิ่มเติม
* **จัดการเนื้อหาแบบ Dynamic (Selenium)**: สำหรับเว็บไซต์ที่โหลดเนื้อหาแบบ dynamic ด้วย JavaScript อาจศึกษาและทดลองใช้ `Selenium` เพื่อควบคุมเบราว์เซอร์ (ต้องติดตั้ง browser driver เพิ่ม)
* **บันทึก Error Log**: เพิ่มระบบบันทึกข้อผิดพลาดที่ซับซ้อนขึ้นลงไฟล์
* **รับค่า URL/Selector แบบ Parameterize**: อนุญาตให้ผู้ใช้ป้อน URL และ CSS selector เองได้

## แหล่งอ้างอิง

- Automate the Boring Stuff with Python, 3rd Edition: https://automatetheboringstuff.com/3e/

## แหล่งที่มา

1. https://devpress.csdn.net/python/63051124c67703293080ea76.html
2. https://github.com/BobTheSnob1/dominion_staff_timeline
3. https://github.com/MikeyBeez/RAGAgent
4. https://automatetheboringstuff.com/2e/chapter12/
