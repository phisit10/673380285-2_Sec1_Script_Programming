# 🎓 Portfolio: CP352301 Script Programming

> **แฟ้มสะสมผลงานการเรียนรู้และปฏิบัติการ รายวิชา CP352301 Script Programming**  
> **ภาคเรียนที่ 2 ปีการศึกษา 2568**  
> **จัดทำโดย:** นายพิสิษฐ์ ทรัพย์อุดมโชติ  
> **รหัสนักศึกษา:** 673380285-2 | **Section:** 1  

---

## 📌 ภาพรวมของ Portfolio (Repository Overview)

คลังข้อมูลนี้รวบรวมแบบฝึกหัด ปฏิบัติการ (Labs) และโครงงานย่อย (Class Activities) ทั้งหมดในรายวิชา **Script Programming (CP352301)** โดยครอบคลุมเส้นทางการเรียนรู้ตั้งแต่พื้นฐานการเขียนภาษา Python ขั้นพื้นฐาน การประยุกต์ใช้โครงสร้างข้อมูล การเขียนโปรแกรมเชิงวัตถุ (OOP) การดึงข้อมูลเว็บ (Web Scraping) การประมวลผลไฟล์สำนักงาน (Excel, PDF, Word) การสื่อสารอัตโนมัติ (Email & SMS) จนกระทั่งถึงการสร้างระบบประมวลผลอัตโนมัติขั้นสูงด้วยสถาปัตยกรรมเอเจนต์ (Agentic & Config-Driven Workflows)

---

## 📑 สารบัญ (Table of Contents)

1. [สรุปผลงานรายสัปดาห์ (Weekly Labs)](#-สรุปผลงานรายสัปดาห์-weekly-labs)
   - [Week 1: พื้นฐานภาษา Python และการคำนวณรูปทรงเรขาคณิต](#week-1-python-basics--geometric-area-calculator)
   - [Week 2: คำสั่งเงื่อนไขและการควบคุมทิศทางโปรแกรม](#week-2-control-flow--conditionals)
   - [Week 3: การวนซ้ำและลูป (Loops & Iterations)](#week-3-loops-iteration--debugging)
   - [Week 4: โครงสร้างข้อมูล List และ Tuple](#week-4-data-structures-lists--tuples)
   - [Week 5: โครงสร้างข้อมูล Dictionary และ Set](#week-5-data-structures-dictionaries--sets)
   - [Week 6: ฟังก์ชันและโมดูล (Functions & Modular Programming)](#week-6-functions--modular-programming)
   - [Week 7: การดึงข้อมูลเว็บเบื้องต้นและขั้นสูง (Web Scraping & Selenium)](#week-7-web-scraping--automated-agents)
   - [Week 8: การจัดการข้อมูล CSV และ JSON (Data Processing & Agentic Workflow)](#week-8-data-processing-csv--json)
   - [Week 10: การจัดการกระดาษทำการ Excel อัตโนมัติ (Spreadsheet Automation)](#week-10-spreadsheet-automation-openpyxl)
   - [Week 11: การจัดการเอกสาร PDF และ Word อัตโนมัติ (Document Automation)](#week-11-document-automation-pdf--word)
   - [Week 12: ระบบสื่อสารอัตโนมัติ Email และ SMS (Communication Automation)](#week-12-communication-automation-email--sms)
2. [สรุปกิจกรรมในชั้นเรียน (Class Activities)](#-สรุปกิจกรรมในชั้นเรียน-class-activities)
   - [Class Activity 1: Building a Simple CLI Application & Defensive Programming](#class-activity-1-building-a-simple-cli-application)
   - [Class Activity 2: OOP Fundamentals & Refactoring CLI Task Manager](#class-activity-2-oop-fundamentals--refactoring)
   - [Class Activity 3: Interacting with Web APIs & JSON Data Processing](#class-activity-3-interacting-with-web-apis)
   - [Class Activity 4: Project Planning & Design: Building an Enhanced Task Manager](#class-activity-4-project-planning--design-enhanced-task-manager)
3. [ตารางสรุปทักษะและเทคโนโลยีที่ใช้ (Tech Stack Summary)](#-ตารางสรุปทักษะและเทคโนโลยีที่ใช้-tech-stack-summary)

---

## 📅 สรุปผลงานรายสัปดาห์ (Weekly Labs)

---

### [Week 1](Week1/): Python Basics & Geometric Area Calculator
*ไฟล์งาน:* `Sec1_Week1_673380285_2.ipynb`

* **ทำอะไร:** เขียนคำสั่งพื้นฐานไวยากรณ์ Python, ทดลองตัวแปรชนิดต่างๆ, การรับค่าผ่านคีย์บอร์ด, แก้ไขปริศนาเรื่อง Type Casting และสร้างโปรแกรมคำนวณพื้นที่รูปเรขาคณิต (สี่เหลี่ยมผืนผ้า, วงกลม, สามเหลี่ยม)
* **เกี่ยวกับเรื่องอะไร:** ชนิดข้อมูลพื้นฐาน (`int`, `float`, `str`, `bool`), ตัวดำเนินการทางคณิตศาสตร์, ฟังก์ชัน `print()`, `type()`, `input()` และการควบคุมเงื่อนไขเบื้องต้นด้วย `if-elif-else`
* **ทำยังไง:** 
  * ใช้งาน Jupyter Notebook ประกาศตัวแปรและทดสอบผลลัพธ์ผ่าน interactive cells
  * ใช้ `input()` รับค่าความกว้าง ความยาว หรือรัศมี แล้วแปลงเป็น `float` ก่อนนำไปคำนวณตามสูตรคณิตศาสตร์
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจชนิดข้อมูลของ Python, เข้าใจว่าค่าที่ได้จาก `input()` จะเป็น `str` เสมอซึ่งต้องแปลงชนิดข้อมูล (Type Casting) ก่อนคำนวณ และฝึกการควบคุมเงื่อนไขเมนูตัวเลือกอย่างเป็นระบบ

---

### [Week 2](Week2/): Control Flow & Conditionals
*ไฟล์งาน:* `lab2_1.py`, `lab2_2.py` และเอกสารปฏิบัติการใน `Lab2_Activity/`

* **ทำอะไร:**
  * **Lab 2.1 (Number Classifier):** ตรวจสอบตัวเลขว่าเป็นบวก ลบ หรือศูนย์, ตรวจสอบว่าเป็นเลขคู่หรือเลขคี่ และ Challenge การวิเคราะห์เงื่อนไขผสม (เช่น Positive Even, Negative Odd)
  * **Lab 2.2 (Movie Recommendation):** ระบบแนะนำภาพยนตร์ตามช่วงอายุ และถามความชอบเฉพาะแนวเพื่อแนะนำภาพยนตร์แบบเจาะจง
* **เกี่ยวกับเรื่องอะไร:** โครงสร้างเงื่อนไข `if`, `elif`, `else`, ตัวดำเนินการเปรียบเทียบ (`>`, `<`, `==`, `>=`), ตัวดำเนินการหารเอาเศษ (`%`) และตรรกะแบบผสม (`and`, `or`)
* **ทำยังไง:** เขียนสคริปต์ Python เดี่ยว รับค่าตัวเลขผ่าน Terminal ตรวจสอบเงื่อนไขตามลำดับ และใช้เงื่อนไขซ้อน (Nested conditions) เพื่อตอบสนองตามคำตอบของผู้ใช้
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจลำดับการประเมินเงื่อนไขของโปรแกรม การใช้ Nested if เพื่อจำแนกความต้องการที่ซับซ้อนขึ้น และการจัดการกรณีข้อมูลไม่ถูกต้อง (Invalid input)

---

### [Week 3](Week3/): Loops, Iteration & Debugging
*ไฟล์งาน:* `Sec1_Week3_673380285_2.ipynb`

* **ทำอะไร:**
  * **Lab 3.1 (Multiplication Table):** สร้างตารางสูตรคูณแม่เดี่ยว และตารางสูตรคูณแบบตารางกริดเต็ม 12x12
  * **Lab 3.2 (Countdown & Guessing Game):** โปรแกรมนับถอยหลังด้วย `while` loop และเกมทายตัวเลขปริศนาพร้อมคำใบ้ Too High / Too Low
  * **Activity 3.1 & 3.2 (Debugging & Patterns):** แก้ไขบั๊กลูป (Infinite loop, ผิด range, misplaced break) และวาดรูปแบบดาว (สี่เหลี่ยม, สามเหลี่ยมมุมฉากตรงและกลับด้าน)
* **เกี่ยวกับเรื่องอะไร:** โครงสร้างการวนซ้ำ `for`, `while`, ฟังก์ชัน `range()`, คำสั่งควบคุมลูป `break`, ลูปซ้อนลูป (Nested Loops) และการจัดรูปแบบ String Output
* **ทำยังไง:** 
  * ใช้ `for i in range(...)` ซ้อนกัน 2 ชั้นเพื่อวนแถวและคอลัมน์ในการวาดลวดลายและพิมพ์ตารางสูตรคูณ
  * ใช้ `while True` ร่วมกับ `break` เพื่อรับค่าทายตัวเลขจากผู้ใช้จนกว่าจะถูกต้อง
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจกลไกการวนซ้ำ ทักษะการวิเคราะห์และแก้ไขปัญหาลูปไม่สิ้นสุด (Infinite loop) การควบคุมการจัดระยะช่องว่างในการแสดงผล และการแก้ปัญหาอัลกอริทึมเชิงมิติด้วย Nested Loops

---

### [Week 4](week4/): Data Structures: Lists & Tuples
*ไฟล์งาน:* `Sec1_Week4_673380285_2.ipynb`

* **ทำอะไร:**
  * **Lab 4.1 (Student Management System):** ระบบจัดการรายชื่อนักศึกษา (เพิ่ม, ค้นหา, ลบ, จัดเรียง, นับจำนวน)
  * **Lab 4.2 (Geometric Calculations):** เก็บพิกัด 2 มิติ (x, y) ด้วย Tuple, สาธิตความไม่สามารถเปลี่ยนแปลงค่าได้ (Immutability) และคำนวณระยะทางแบบ Euclidean
  * **Activity 4.1 & 4.2:** เปรียบเทียบสถานการณ์จริงว่าควรใช้ List หรือ Tuple พร้อมสร้างระบบ Interactive To-Do List CLI
* **เกี่ยวกับเรื่องอะไร:** โครงสร้างข้อมูล List (Mutable) และ Tuple (Immutable), Indexing, Slicing, เมธอด `.append()`, `.remove()`, `.sort()`, `len()`, `math.sqrt()` และการจัดการข้อผิดพลาด `TypeError`
* **ทำยังไง:** 
  * ใช้เมนูวนลูป `while` รับคำสั่งจัดการ List ข้อมูลนักศึกษาและงาน To-Do
  * ใช้ Tuple บรรจุพิกัดและลองเขียนทับค่าเพื่อดักจับข้อผิดพลาด `try...except TypeError` เพื่อพิสูจน์คุณสมบัติความคงที่
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจความแตกต่างระหว่างโครงสร้างข้อมูลที่แก้ไขได้ (Mutable) กับแก้ไขไม่ได้ (Immutable) และสามารถเลือกใช้โครงสร้างข้อมูลให้สอดคล้องกับลักษณะความปลอดภัยของข้อมูลในงานจริง

---

### [Week 5](week5/): Data Structures: Dictionaries & Sets
*ไฟล์งาน:* `Sec1_Week5_673380285_2.ipynb`

* **ทำอะไร:**
  * **Lab 5.1 (Contact Book Manager):** สร้างสมุดบันทึกผู้ติดต่อ (ชื่อ, เบอร์โทร, อีเมล) แบบโต้ตอบ รองรับ CRUD (เพิ่ม/อัปเดต, ดูข้อมูล, แสดงรายการทั้งหมด, ลบ)
  * **Lab 5.2 (Course Enrollment & Collaboration):** เปรียบเทียบรายชื่อนักศึกษาข้ามวิชาด้วยเซต หา Intersection, Union, Difference, Symmetric Difference และการลบข้อมูลซ้ำจาก List
  * **Activity 5.1 & 5.2:** วิเคราะห์การประยุกต์ใช้ในอุตสาหกรรม และสร้างโปรแกรมนับความถี่ของคำ (Word Frequency Counter) พร้อมตัดเครื่องหมายวรรคตอน
* **เกี่ยวกับเรื่องอะไร:** Dictionary (Key-Value, Hashing), Set Operations, การเข้าถึงข้อมูลแบบ Nested, เมธอด `.get()`, `.items()`, `.pop()`, การแปลง `list(set(...))` และการประมวลผลข้อความ (Text Processing)
* **ทำยังไง:** 
  * ใช้ Nested Dictionary จัดเก็บข้อมูลผู้ติดต่อโดยใช้ชื่อเป็น Key
  * ใช้ฟังก์ชันทางเซต `intersection()`, `union()`, `difference()` ในการวิเคราะห์กลุ่มข้อมูล
  * แปลงข้อความเป็นพิมพ์เล็ก แยกคำด้วย `.split()` ทำความสะอาดด้วย `.strip('.,!?\"')` และนับลงใน Dictionary
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจประสิทธิภาพในการสืบค้นข้อมูลด้วย Key (O(1) lookups) การจัดการความไม่ซ้ำซ้อนของข้อมูลด้วย Set และการนำโครงสร้างข้อมูลพื้นฐานมาประยุกต์แก้ปัญหาการประมวลผลข้อมูลจริง

---

### [Week 6](week6/): Functions & Modular Programming
*ไฟล์งาน:* `Activity/6.1/activity_6.1.py`, `Activity/6.2/Activity_6.2.md`, `Lab/6.1/lab6_1.py`, `Lab/6.2/my_utils.py`, `Lab/6.2/main_program.py`

* **ทำอะไร:**
  * **Lab 6.1 (Simple Calculator):** สร้างฟังก์ชันบวก ลบ คูณ หาร และยกกำลัง พร้อมระบบรับค่าโต้ตอบ
  * **Lab 6.2 (Custom Modules):** สร้างโมดูลอรรถประโยชน์ `my_utils.py` บรรจุฟังก์ชันทักทายและตรวจสอบจำนวนเฉพาะ (`is_prime`) แล้ว import มาใช้ใน `main_program.py` ร่วมกับ `math` และ `random`
  * **Activity 6.1:** Refactoring โค้ดแล็บ Number Classifier จาก Week 2 ที่เป็นแบบเขียนยาวไฟล์เดียว ให้กลายเป็นฟังก์ชันแยกส่วนที่นำกลับมาใช้ใหม่ได้
  * **Activity 6.2:** สรุปเอกสารข้อดีของการเขียนโปรแกรมแบบแยกโมดูล และสำรวจ Python Standard Library (`datetime`, `os`, `json`)
* **เกี่ยวกับเรื่องอะไร:** นิยามฟังก์ชัน `def`, Parameters & Arguments, Default Arguments, Return Values, การสร้าง Custom Module, การจัดระเบียบโค้ดตามแนวทาง DRY (Don't Repeat Yourself) และ `if __name__ == "__main__":`
* **ทำยังไง:** แยกโค้ด logic ออกเป็นฟังก์ชันย่อยๆ ใส่ Docstrings อธิบายการทำงาน และแยกไฟล์ utility ออกจากไฟล์หลักแล้วเรียกผ่านคำสั่ง `import`
* **ทำแล้วได้เรียนรู้อะไร:** รู้วิธีจัดระเบียบโค้ดให้สะอาด ป้องกันโค้ดซ้ำซ้อน นำกลับมาใช้ใหม่ได้ง่ายขึ้น และเข้าใจโครงสร้างพื้นฐานในการสร้างโปรแกรมขนาดใหญ่

---

### [Week 7](week7/): Web Scraping & Automated Agents
*ไฟล์งาน:* `LabBasic1/` (Simple Web Scraper), `LabAdv1/` (Advanced Selenium Scraper Agent)

* **ทำอะไร:**
  * **Lab Basic:** พัฒนาตัวดึงข้อมูลเว็บ (Web Scraper) เพื่อดึงชื่อหนังสือและรายชื่อบทเรียนทั้งหมดจากเว็บไซต์ *Automate the Boring Stuff with Python* (3rd Edition)
  * **Lab Advanced:** พัฒนาระบบ Scraper ขั้นสูงในรูปแบบ Agentic Automation ที่ใช้ Selenium ควบคุมเบราว์เซอร์อัตโนมัติ รองรับเนื้อหาแบบ Dynamic ที่เรนเดอร์ด้วย JavaScript, การเปลี่ยนหน้า (Pagination), และควบคุมผ่านไฟล์คอนฟิกภายนอก
* **เกี่ยวกับเรื่องอะไร:** HTTP Requests, HTML Parsing, CSS Selectors, DOM Inspection, จริยธรรมการดึงข้อมูล (`robots.txt`, Rate Limiting), Selenium WebDriver, Headless Browser, Config-Driven Architecture, และ Dataclasses
* **ทำยังไง:** 
  * *Basic:* ใช้ไลบรารี `requests` ดาวน์โหลด HTML และใช้ `BeautifulSoup4` ค้นหาแท็กและดึงข้อความ
  * *Adv:* ใช้ `selenium` ร่วมกับ `webdriver_manager`, ตั้งค่าเงื่อนไขการดึงข้อมูลใน `configs/example_site_config.json`, ใช้ Explicit Waits (`WebDriverWait`) เพื่อรอให้เนื้อหาโหลดสมบูรณ์ และบันทึกข้อมูลออกเป็น `data/scraped_products.json`
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจกระบวนการแปลงข้อมูลจากหน้าเว็บเป็น Structured Data, ข้อแตกต่างระหว่างการดึงหน้าเว็บแบบ Static เทียบกับ Dynamic ที่ต้องใช้ Browser Automation รวมถึงการตระหนักถึงกฎหมายและจริยธรรมในการ Scraping

---

### [Week 8](week8/): Data Processing (CSV & JSON)
*ไฟล์งาน:* `week8_LabBasic/`, `week8_LabAdv/`

* **ทำอะไร:**
  * **Lab Basic:** พัฒนาโปรแกรมอ่าน/เขียนไฟล์ CSV ด้วย `csv.DictReader`/`DictWriter` เพื่อคัดกรองยอดขายและคำนวณผลสรุป พร้อมอ่านและอัปเดตสต็อกสินค้าในไฟล์ JSON
  * **Lab Advanced:** สร้างระบบ **Agentic Data Processor** (`DataAgent`) ที่ขับเคลื่อนเวิร์กโฟลว์ผ่านคอนฟิก `data_pipeline_config.json` รองรับการรวมกลุ่มข้อมูล (Aggregation/Grouping), การอัปเดตแบบ Dynamic Nested Path, การแปลงข้อมูลข้ามรูปแบบ (CSV <-> JSON) และบันทึกประวัติการทำงาน (Audit Report)
* **เกี่ยวกับเรื่องอะไร:** โครงสร้างไฟล์ Plaintext (CSV, JSON), Serialization/Deserialization, State Management ภายใน Agent, การประมวลผลข้อมูล Pipeline และระบบบันทึก Log
* **ทำยังไง:**
  * *Basic:* ใช้โมดูลมาตรฐาน `csv` และ `json` วนลูปประมวลผลข้อมูลและเขียนผลลัพธ์ลงโฟลเดอร์ `data/`
  * *Adv:* ออกแบบระบบโมดูลาร์ (`csv_tasks.py`, `json_tasks.py`, `conversion_tasks.py`, `data_agent.py`) มีหน่วยความจำชั่วคราว (`data_store`) เพื่อส่งผ่านผลลัพธ์ระหว่าง Task ใน Pipeline อัตโนมัติ
* **ทำแล้วได้เรียนรู้อะไร:** ได้เรียนรู้เทคนิคการประมวลผลข้อมูลอัตโนมัติแบบหลายขั้นตอน (Data Pipeline) การส่งผ่านสถานะข้อมูลระหว่างโมดูล และการออกแบบซอฟต์แวร์ที่ปรับแต่งขั้นตอนได้ผ่าน Configuration โดยไม่ต้องแก้โค้ด

---

### [Week 10](week10/): Spreadsheet Automation (openpyxl)
*ไฟล์งาน:* `week10_LabBasic/`, `week10_LabAdv/`

* **ทำอะไร:**
  * **Lab Basic:** สร้างโปรแกรมอ่านข้อมูลการขายจากไฟล์ Excel (`.xlsx`), คำนวณราคารวมและยอดรวมสุทธิ, จัดรูปแบบเซลล์ (ฟอนต์, สีพื้นหลัง, ขอบ) และปรับขนาดความกว้างคอลัมน์อัตโนมัติ
  * **Lab Advanced:** สร้างระบบ **Spreadsheet Agent** อัตโนมัติ ควบคุมการทำงานผ่าน `example_spreadsheet_config.json` รองรับการแทรกสูตรคำนวณของ Excel, การสร้างแผนภูมิ (Bar/Line/Pie Charts), การจัดรูปแบบตามเงื่อนไข (Conditional Formatting) และการสร้างชีต Audit Log
* **เกี่ยวกับเรื่องอะไร:** การจัดการ Spreadsheet, ไลบรารี `openpyxl` (Workbook, Worksheet, Cell, Styles, Chart, Formatting), Task-driven Automation
* **ทำยังไง:**
  * *Basic:* โหลดไฟล์ด้วย `openpyxl.load_workbook`, วนลูปอ่านข้อมูลทีละแถว ทำการคำนวณและเขียนค่ากลับลงเซลล์ พร้อมตกแต่งสไตล์
  * *Adv:* พัฒนาคลาส `SpreadsheetAgent` อ่านงานจากไฟล์คอนฟิก สั่งสร้างกราฟ จัดกลุ่มข้อมูลตามเงื่อนไข และบันทึกผลการดำเนินงานแต่ละ Task
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจการนำโค้ด Python เข้าไปทำงานแทนมนุษย์ในงานเอกสารสำนักงาน (Office Automation) การสร้างรายงานสรุปผลที่มีการตกแต่งและแสดงผลเป็นภาพกราฟิกอย่างมืออาชีพ

---

### [Week 11](week11/): Document Automation (PDF & Word)
*ไฟล์งาน:* `week11_LabBasic/`, `week11_LabAdv/`

* **ทำอะไร:**
  * **Lab Basic:** สร้างโปรแกรมดึงข้อความจากไฟล์ PDF, รวมไฟล์ PDF หลายไฟล์เข้าด้วยกันเป็นไฟล์เดียว และสร้างเอกสารรายงาน Microsoft Word (`.docx`) พร้อมจัดรูปแบบหัวข้อ ย่อหน้า และตาราง
  * **Lab Advanced:** พัฒนาระบบ **Document Agent** จัดการเอกสารอัตโนมัติขั้นสูง ควบคุมผ่านไฟล์คอนฟิก รองรับการสร้างเอกสาร Word จากเทมเพลตที่มี Placeholders `{{...}}`, การสกัดข้อความ และการสร้าง/ประทับลายน้ำ (Watermarking) ลงในไฟล์ PDF ทุกหน้าแบบไดนามิก
* **เกี่ยวกับเรื่องอะไร:** การประมวลผลไฟล์เอกสาร, ไลบรารี `PyPDF2` / `pypdf`, `python-docx`, `reportlab` (Dynamic Watermarking), Template Engine พื้นฐาน, และ Audit Logging
* **ทำยังไง:**
  * *Basic:* ใช้ `PyPDF2.PdfMerger` รวมไฟล์ และใช้ `python-docx` สร้าง Document object เพิ่มย่อหน้าและตารางข้อมูล
  * *Adv:* ใช้ `reportlab` วาดหน้ากระดาษลายน้ำในหน่วยความจำ แล้วนำไปซ้อนทับ (Overlay) บนหน้า PDF ต้นฉบับด้วย `pypdf` พร้อมเขียนฟังก์ชันค้นหาและแทนที่ข้อความ Placeholders ในโครงสร้าง XML ของเอกสาร Word
* **ทำแล้วได้เรียนรู้อะไร:** ได้เรียนรู้เทคนิคการทำงานกับไฟล์เอกสารมาตรฐานธุรกิจ (PDF/Word) เข้าใจข้อจำกัดของเอกสารแบบ Binary และการใช้เทมเพลตเพื่อสร้างรายงานอัตโนมัติจำนวนมากได้อย่างรวดเร็ว

---

### [Week 12](week12/): Communication Automation (Email & SMS)
*ไฟล์งาน:* `week12_LabBasic/` (`email-sms-automator`), `week12_LabAdv/` (`Week_12_LabX_ADV_Agentic_Communication_Workflows...`)

* **ทำอะไร:**
  * **Lab Basic:** พัฒนาชุดเครื่องมือสื่อสารอัตโนมัติ รองรับการส่งอีเมลผ่าน SMTP (พร้อม STARTTLS, HTML และไฟล์แนบ), การส่ง SMS ผ่าน Carrier Email Gateway, และการเชื่อมต่อ IMAP เพื่อค้นหา กรอง อ่าน และดาวน์โหลดไฟล์แนบจากอีเมลเข้า
  * **Lab Advanced:** พัฒนาระบบ **Communication Agent** ขับเคลื่อนผ่านไฟล์คอนฟิก `comm_pipeline_config.json` รันเวิร์กโฟลว์ส่งรายงานประจำวัน, จำลองคำขอข้อมูล, ประมวลผลกล่องข้อความเข้าตามกฎ (Rule-based Inbox Processing), ตรวจจับอีเมลที่มีคีย์เวิร์ดด่วน (Urgent) เพื่อส่งแจ้งเตือน SMS อัตโนมัติ และส่งอีเมลตอบกลับอัตโนมัติ (Auto-reply)
* **เกี่ยวกับเรื่องอะไร:** โปรโตคอลการสื่อสารบนอินเทอร์เน็ต (SMTP, IMAP), MIME Multi-part messaging, การจัดการความปลอดภัยข้อมูลสำคัญ (Credentials Security via `.env`), Clean Architecture, และ Rule-based Event Triggering
* **ทำยังไง:**
  * *Basic:* ใช้ Standard Libraries (`smtplib`, `imaplib`, `email`) ร่วมกับ `python-dotenv` โหลด Gmail App Password จาก `.env`, สร้าง Unit Test Suite ด้วย `unittest.mock`
  * *Adv:* พัฒนาคลาส `CommunicationAgent` วนลูปอ่านเงื่อนไขในคอนฟิก สแกน Inbox ตรวจสอบเงื่อนไขตามข้อความและไฟล์แนบ แล้วกระตุ้นการทำงานของทาสก์ถัดไป (เช่น ส่ง SMS Alert หรือส่งเมลตอบกลับ)
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจสถาปัตยกรรมระบบแจ้งเตือนและระบบตอบกลับอัตโนมัติในระดับ Production การป้องกันความลับของระบบด้วยตัวแปรสภาพแวดล้อม และการเขียน Mock Unit Tests เพื่อทดสอบระบบเครือข่ายโดยไม่ต้องเชื่อมต่อจริง

---

## 🚀 สรุปกิจกรรมในชั้นเรียน (Class Activities)

---

### [Class Activity 1](Class_activity_1/): Building a Simple CLI Application
*โฟลเดอร์โปรเจกต์:* `Class_activity_1/Class_activity_1_Building-a-Simple-CLI-Application-main/`

* **ทำอะไร:** สร้างแอปพลิเคชันจัดการงานผ่านบรรทัดคำสั่ง (CLI Task Manager) ที่รองรับการเพิ่ม แสดงสถานะ ทำเครื่องหมายเสร็จสิ้น ลบ และค้นหางาน พร้อมระบบบันทึกข้อมูลถาวร
* **เกี่ยวกับเรื่องอะไร:** สถาปัตยกรรมแบบแยกส่วน (Modular Architecture / Separation of Concerns), การเขียนโปรแกรมเชิงป้องกัน (Defensive Programming), การจัดเก็บข้อมูลถาวรด้วยไฟล์ JSON และการดีบักโปรแกรมด้วย VS Code
* **ทำยังไง:**
  * แบ่งโครงสร้างโค้ดออกเป็น 3 เลเยอร์:
    * `main.py`: Presentation Layer (เมนู CLI และการรับค่าอย่างปลอดภัย)
    * `src/task_logic.py`: Business Logic Layer (คำนวณและประมวลผลงาน)
    * `src/task_data.py`: Data Access Layer (อ่าน/เขียนไฟล์ `data/tasks.json`)
  * ป้องกันโปรแกรมแครชด้วยการครอบ `try...except` สำหรับดักจับ `FileNotFoundError`, `json.JSONDecodeError` และข้อผิดพลาดจากการป้อนตัวเลข
* **ทำแล้วได้เรียนรู้อะไร:** เปลี่ยนวิธีคิดจากการเขียนสคริปต์ไฟล์เดียวสู่การออกแบบซอฟต์แวร์แบบแยกเลเยอร์หน้าที่ความรับผิดชอบ และฝึกฝนการใช้ Breakpoint / Step Over ใน VS Code เพื่อหาข้อผิดพลาดของโค้ด

---

### [Class Activity 2](Class_activity_2/): OOP Fundamentals & Refactoring
*โฟลเดอร์โปรเจกต์:* `Class_activity_2/my-oop-task-manager/`

* **ทำอะไร:** ปรับปรุงโค้ดระบบ Task Manager จากแบบวิธีดั้งเดิม (Procedural ที่ใช้ Dictionary) ให้กลายเป็นระบบที่ขับเคลื่อนด้วยการเขียนโปรแกรมเชิงวัตถุ (Object-Oriented Programming: OOP) อย่างสมบูรณ์
* **เกี่ยวกับเรื่องอะไร:** คลาสและออบเจกต์ (Classes & Objects), Constructor (`__init__`), ตัวแปร `self`, การห่อหุ้มข้อมูลและพฤติกรรม (Encapsulation), Dunder / Magic Methods (`__str__`, `__repr__`), Serialization / Deserialization และ Automated Unit Testing
* **ทำยังไง:**
  * สร้างคลาส `Task` ทำหน้าที่เป็นพิมพ์เขียวของงานแต่ละรายการ มีแอตทริบิวต์ `id`, `description`, `completed` และเมธอด `mark_complete()`, `to_dict()`
  * สร้างคลาส `TaskManager` ทำหน้าที่เก็บและจัดการคอลเลกชันของ Task, เชื่อมต่อกับไฟล์ JSON
  * เขียน Unit Tests ในโฟลเดอร์ `tests/` ด้วยโมดูล `unittest` เพื่อตรวจสอบความถูกต้องของ Logic
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจหลักการของ OOP อย่างลึกซึ้ง มองเห็นข้อดีของการผูกข้อมูลและพฤติกรรมไว้ด้วยกัน ซึ่งช่วยให้โค้ดมีความปลอดภัย มีระเบียบ และสามารถเขียนชุดทดสอบอัตโนมัติได้อย่างมีประสิทธิภาพ

---

### [Class Activity 3](Class_activity_3/): Interacting with Web APIs
*โฟลเดอร์โปรเจกต์:* `Class_activity_3/my-api-fetcher/`

* **ทำอะไร:** สร้างแอปพลิเคชัน CLI เชื่อมต่อไปยัง Web API ภายนอก (JSONPlaceholder) เพื่อดึงข้อมูลงานเดี่ยว ดึงรายการโพสต์ ดึงงานตามผู้ใช้ ดึงโปรไฟล์ผู้ใช้ ดึงความคิดเห็น และส่งออกข้อมูลเป็นไฟล์ JSON
* **เกี่ยวกับเรื่องอะไร:** Application Programming Interface (API), โปรโตคอล HTTP, กริยา HTTP GET, HTTP Status Codes (200, 404, 500), การแปลงโครงสร้าง JSON <-> Python, การจัดการแพ็กเกจด้วย `pip` และ `requirements.txt`
* **ทำยังไง:**
  * ติดตั้งและใช้งานไลบรารี `requests`
  * สร้างคลาส `APIClient` ใน `src/api_client.py` เพื่อรวมศูนย์การส่ง Request และดักจับความผิดพลาดของเครือข่าย เช่น `ConnectionError`, `Timeout`, `HTTPError`
  * ออกแบบเมนู CLI โต้ตอบและสร้างฟังก์ชันส่งออกข้อมูล `export_to_json_file()` ด้วยการระบุ `encoding='utf-8'`
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจว่าแอปพลิเคชันในโลกปัจจุบันสื่อสารแลกเปลี่ยนข้อมูลกันอย่างไรผ่าน REST API รู้วิธีการถอดรหัสข้อมูล JSON ที่ซับซ้อน และการรับมือกับสถานการณ์เครือข่ายขัดข้องได้อย่างรัดกุม

---

### [Class Activity 4](Class_activity_4/): Project Planning & Design: Enhanced Task Manager
*โฟลเดอร์โปรเจกต์:* `Class_activity_4/enhanced-task-manager-design/`

* **ทำอะไร:** วางแผน ออกแบบสถาปัตยกรรม และพัฒนาระบบ **Enhanced Task Manager CLI** ที่รองรับงานหลากหลายรูปแบบ (งานทั่วไป, งานที่มีวันครบกำหนด, งานที่มีระดับความสำคัญ) พร้อมฟังก์ชันค้นหา กรองข้อมูล และจัดเรียงลำดับ
* **เกี่ยวกับเรื่องอะไร:** Software Engineering Architecture, Separation of Concerns (SoC), OOP ขั้นสูง: การสืบทอดคุณสมบัติ (Inheritance) และความหลากหลายของรูปแบบ (Polymorphism), การวางแผนงานผ่านเอกสาร `PLAN.md`
* **ทำยังไง:**
  * ออกแบบลำดับชั้นคลาสใน `src/task.py`:
    * คลาสแม่: `Task`
    * คลาสลูกที่สืบทอด: `DueDateTask` (เพิ่ม `due_date`), `PriorityTask` (เพิ่ม `priority`)
  * แยกโครงสร้างระบบ 4 ชั้น: UI (`cli_interface.py`), Logic (`task_manager.py`), Models (`task.py`), Data (`data_persistence.py`)
  * พัฒนาระบบค้นหาแบบไม่สนใจตัวพิมพ์เล็ก-ใหญ่ (`case-insensitive search`), ระบบกรองหลายมิติ (`filter_tasks`), และระบบจัดเรียงข้อมูลชนิดผสมผสาน (`sort_tasks` with Heterogeneous Data Sorting)
* **ทำแล้วได้เรียนรู้อะไร:** เข้าใจความสำคัญของ "การออกแบบก่อนลงมือเขียนโค้ด" (Design Before Code) เพื่อป้องกันโค้ดยุ่งเหยิง (Spaghetti Code) และสามารถนำหลักการ OOP ขั้นสูงอย่าง Inheritance และ Polymorphism มาใช้แก้ปัญหาที่มีความซับซ้อนได้อย่างเป็นมืออาชีพ

---

## 🛠️ ตารางสรุปทักษะและเทคโนโลยีที่ใช้ (Tech Stack Summary)

| กลุ่มเทคโนโลยี | เครื่องมือ / ไลบรารี / โมดูล | วัตถุประสงค์และการนำไปใช้ |
| :--- | :--- | :--- |
| **Core Programming** | Python 3, Jupyter Notebook | การเขียนสคริปต์, โครงสร้างข้อมูลพื้นฐาน, การทดลองโค้ด |
| **Development Best Practices** | OOP, Modular Architecture, SoC | การแบ่งเลเยอร์ซอฟต์แวร์, การเขียนโค้ดตามหลัก DRY, การออกแบบคลาส |
| **Testing & Debugging** | VS Code Debugger, `unittest`, `unittest.mock` | การตั้ง Breakpoint, การเขียนชุดทดสอบ และการจำลองระบบเครือข่าย |
| **Web Scraping & Automation** | `requests`, `BeautifulSoup4`, `selenium`, `webdriver_manager` | การดึงข้อมูลเว็บทั้งแบบ Static HTML และ Dynamic JavaScript |
| **Web API & Data Formats** | `requests`, `json`, `csv` | การเชื่อมต่อ REST API, การประมวลผลไฟล์ CSV และ JSON Data Pipeline |
| **Office & Documents** | `openpyxl`, `PyPDF2` / `pypdf`, `python-docx`, `reportlab` | การสร้างและปรับแต่งไฟล์ Excel, รวม/สกัดไฟล์ PDF, ลายน้ำ, เทมเพลต Word |
| **Communication Automation** | `smtplib`, `imaplib`, `email`, `python-dotenv` | การส่ง-รับอีเมล, การดาวน์โหลดไฟล์แนบ, การส่ง SMS ผ่าน Gateway |
| **Agentic Workflows** | Config-driven JSON (`DataAgent`, `DocumentAgent`, `SpreadsheetAgent`, `CommunicationAgent`) | การสร้างระบบประมวลผลและตอบสนองอัตโนมัติตามลำดับคำสั่งและเงื่อนไข |
| **Version Control** | Git, GitHub | การจัดการเวอร์ชันของโค้ดและการส่งงาน |

---

*เอกสารฉบับนี้จัดทำขึ้นเพื่อเป็นสรุปผลงานวิชา CP352301 Script Programming สำหรับการประเมินและทบทวนความรู้ความสามารถทางด้านการเขียนโปรแกรมสคริปต์*
