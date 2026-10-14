# 🎤 คู่มือการนำเสนอผลงาน (Final Project Presentation Guide)
## โครงงาน: Enhanced Task Manager CLI Application
> **วิชา**: CP352301 Script Programming  
> **ผู้จัดทำ**: นายพิสิษฐ์ ทรัพย์อุดมโชติ (รหัสนักศึกษา: 673380285-2) | Section 1  
> **เวลาที่ใช้ในการนำเสนอ**: 5 - 7 นาที

---

## 📑 สรุปโครงสร้างสไลด์การนำเสนอ (7 ส่วนหลัก)

| สไลด์ที่ | หัวข้อ | เนื้อหาสำคัญ | เวลาโดยประมาณ |
| :---: | :--- | :--- | :---: |
| **1** | **Introduction** | แนะนำตัว, ชื่อโปรเจกต์, วัตถุประสงค์ของการพัฒนา | 30 วินาที |
| **2** | **Problem Solved** | ปัญหาที่พบในการจัดการงาน และโปรแกรมนี้เข้ามาช่วยแก้อย่างไร | 45 วินาที |
| **3** | **Software Architecture** | โครงสร้าง 4 Layers ตามหลัก Separation of Concerns & OOP Diagram | 1 นาที |
| **4** | **Key Features** | ฟีเจอร์เด่น: Tags, Multi-criteria Filter, Case-insensitive Search, Polymorphic Sort | 1 นาที |
| **5** | **Live Demonstration** | สาธิตการรันโปรแกรมจริง 4 Scenarios ผ่าน Terminal | 2 นาที |
| **6** | **Technical Challenges & Solutions** | ปัญหาที่ท้าทาย (Polymorphic Sorting, Backward Compatibility) และวิธีแก้ | 1 นาที |
| **7** | **Lessons Learned & Future Work** | สิ่งที่ได้เรียนรู้, การพัฒนาต่อยอดในอนาคต และช่วงถาม-ตอบ (Q&A) | 30 วินาที |

---

## 🗣️ บทพูดนำเสนอ (Script) ภาษาไทย พร้อมกำกับเวลา

### Slide 1: Introduction (แนะนำตัว & วัตถุประสงค์) — 30 วินาที
> *"กราบเรียนอาจารย์และสวัสดีเพื่อนๆ ทุกคนครับ ผมนายพิสิษฐ์ ทรัพย์อุดมโชติ รหัสนักศึกษา 673380285-2 กลุ่มเรียน Section 1 วันนี้ขอมานำเสนอโครงงานปลายภาค Enhanced Task Manager CLI Application ครับ*  
> *โปรเจกต์นี้มีวัตถุประสงค์เพื่อพัฒนาเครื่องมือบริหารจัดการงานผ่าน Command-Line Interface ที่มีความยืดหยุ่น โดยนำหลักการ Object-Oriented Programming ขั้นสูง การแยกสัดส่วนซอฟต์แวร์ และการทดสอบระบบอัตโนมัติมาประยุกต์ใช้งานจริงครับ"*

---

### Slide 2: Problem Solved (ปัญหาและการแก้ปัญหา) — 45 วินาที
> *"ในชีวิตประจำวัน เรามักเจองานหลายรูปแบบ ทั้งงานทั่วไป งานที่ต้องส่งตามกำหนดเวลา (Due Date) และงานด่วนที่มีความสำคัญสูง (Priority) การจดบันทึกแบบเดิมมักขาดความยืดหยุ่นในการจัดหมวดหมู่และค้นหา*  
> *โปรแกรม Enhanced Task Manager จึงถูกออกแบบมาเพื่อแก้ปัญหานี้ โดยรองรับงานทั้ง 3 รูปแบบอย่างเป็นระบบ มีระบบ Tags ช่วยจัดกลุ่มข้ามหมวดหมู่ พร้อมทั้งระบบค้นหา กรองข้อมูลขั้นสูง และจัดเรียงลำดับได้อย่างแม่นยำครับ"*

---

### Slide 3: Software Architecture & OOP Design — 1 นาที
> *"ในด้านสถาปัตยกรรม เราออกแบบตามหลัก Separation of Concerns (SoC) โดยแบ่งออกเป็น 4 ชั้นอย่างชัดเจน:*
> 1. **Presentation Layer (`cli_interface.py`)**: รับและตรวจสอบความถูกต้องของ Input และแสดงผลลัพธ์
> 2. **Business Logic Layer (`task_manager.py`)**: จัดการ CRUD, การค้นหา กรอง และจัดเรียง
> 3. **Data Access Layer (`data_persistence.py`)**: บันทึกและโหลดไฟล์ JSON อัตโนมัติ
> 4. **Domain Model (`task.py`)**: ใช้หลักการ **Inheritance** โดยมี `Task` เป็นคลาสแม่ และแตกเป็น `DueDateTask` กับ `PriorityTask`
> *นอกจากนี้ยังใช้หลัก **Polymorphism** ในการเรียก `to_dict()` และ `__str__()` ทำให้แต่ละคลาสสามารถแสดงผลและแปลงข้อมูลเฉพาะตัวได้โดยโค้ดส่วนอื่นไม่ต้องแก้ไขครับ"*

---

### Slide 4: Key Features & Capabilities — 1 นาที
> *"ฟีเจอร์เด่นของระบบประกอบด้วย 4 จุดสำคัญครับ:*
> * **1. Categorization with Tags**: ติดป้ายกำกับได้หลายป้าย มีระบบตัดช่องว่างส่วนเกินและแปลงเป็นพิมพ์เล็กเพื่อกันแท็กซ้ำ
> * **2. Partial & Case-Insensitive Search**: ค้นหาคำสั้นๆ ได้ทั้งในรายละเอียดและในรายชื่อแท็ก
> * **3. Multi-Criteria Filter**: สามารถกรองเงื่อนไขแบบผสมผสานได้ ทั้งสถานะงาน, วันส่งก่อน/หลัง, ลำดับความสำคัญ และแท็กพร้อมๆ กัน
> * **4. Polymorphic Sorting**: สามารถจัดเรียงตามวันส่งหรือระดับความสำคัญ โดยระบบจะผลักงานที่ไม่มีคุณสมบัตินั้นไปอยู่ท้ายรายการอย่างเป็นระเบียบ ไม่เกิด Error ครับ"*

---

### Slide 5: Live Demonstration (สาธิตการทำงานจริง) — 2 นาที
*(เปิด Terminal แล้วรัน `python main.py`)*

#### ลำดับขั้นตอนการสาธิต (Demo Script):
1. **แสดงรายการงานทั้งหมด (List Tasks)**
   * กด `4`
   * *อธิบาย*: *"ระบบโหลดข้อมูลตัวอย่างจาก `data/tasks.json` มาแสดงผลอัตโนมัติ แสดง ID, รายละเอียด, สถานะ, วันส่ง/ระดับความสำคัญ และแท็กอย่างชัดเจน"*
2. **เพิ่มงานที่มี Due Date พร้อม Tags (Add Due Date Task)**
   * กด `2`
   * Description: `Prepare presentation slides`
   * Due date: `2026-10-20`
   * Tags: `study, urgent, final`
   * *อธิบาย*: *"จะเห็นว่าระบบทำการตรวจสอบรูปแบบวันที่ และตัดแต่งแท็กให้เป็นพิมพ์เล็กอัตโนมัติ"*
3. **ค้นหางานด้วยคีย์เวิร์ด (Search Tasks)**
   * กด `7`
   * Keyword: `urgent`
   * *อธิบาย*: *"ระบบจะค้นหาคำว่า urgent ทั้งจาก Description และจาก Tags มาแสดงผล"*
4. **กรองงานขั้นสูง (Filter Tasks)**
   * กด `8`
   * Status: กด `Enter` (ข้าม)
   * Due date before: `2026-10-01`
   * Due date after: กด `Enter` (ข้าม)
   * Priority: กด `Enter` (ข้าม)
   * Tags: `study`
   * *อธิบาย*: *"แสดงเฉพาะงานที่ต้องส่งก่อน 1 ต.ค. 2026 และมีแท็ก study ครบถ้วน"*
5. **จัดเรียงตามระดับความสำคัญ (Sort by Priority)**
   * กด `9`
   * Criterion: `priority`
   * Reverse: `no`
   * *อธิบาย*: *"งานระดับ High จะขึ้นก่อน ตามด้วย Medium, Low และงานทั่วไปจะอยู่ท้ายสุด"*
6. **ออกจากโปรแกรม**
   * กด `0`

---

### Slide 6: Technical Challenges & Solutions — 1 นาที
> *"ความท้าทายทางเทคนิคที่พบในโปรเจกต์นี้และวิธีแก้ปัญหาคือ:*
> * **1. ปัญหา Polymorphic Sort**: ในรายการมีทั้ง Task ทั่วไปและ DueDateTask/PriorityTask เมื่อสั่งเรียงตามวันส่ง Task ทั่วไปจะไม่มี attribute `due_date`
>   * *วิธีแก้*: ใช้ Tuple Key กำหนดค่าสำรองเป็น `datetime.date.max` ทำให้งานทั่วไปถูกส่งไปท้ายตาราง และใช้ Priority Mapping `{'High': 1, 'Medium': 2, 'Low': 3}` ร่วมกับค่า `99` สำหรับงานที่ไม่มีความสำคัญ
> * **2. Backward Compatibility ของไฟล์ข้อมูล**: ไฟล์ JSON เดิมไม่มีฟิลด์ `tags`
>   * *วิธีแก้*: ใช้ `t_dict.setdefault('tags', [])` ในขั้นตอน Deserialization เพื่อให้สามารถโหลดไฟล์เก่าได้โดยไม่เกิด `KeyError`"*

---

### Slide 7: Lessons Learned, Future Work & Q&A — 30 วินาที
> *"บทเรียนสำคัญคือ การออกแบบที่ดีตามหลัก Separation of Concerns และการเขียน Automated Unit Test ช่วยให้การเพิ่มฟีเจอร์ใหม่ทำได้อย่างรวดเร็วและปลอดภัย ไม่กระทบส่วนเดิม*  
> *สำหรับแผนพัฒนาต่อยอด เราวางแผนเพิ่ม Graphic User Interface (GUI), เชื่อมต่อฐานข้อมูล SQLite และระบบแจ้งเตือนผ่าน LINE Notify หรือ Discord Webhook ครับ*  
> *ผมขอจบการนำเสนอเพียงเท่านี้ ขอบพระคุณอาจารย์และเพื่อนๆ ครับ มีข้อเสนอแนะหรือคำถามเพิ่มเติมไหมครับ"*

---

## 💡 แนวทางการตอบคำถาม Q&A ที่พบบ่อย

1. **ถาม: ทำไมถึงเลือกใช้ CLI แทน GUI?**
   * **ตอบ**: มุ่งเน้นการฝึกฝนหลักการ Software Architecture, OOP และ Data Structures ให้แม่นยำก่อน และการแยกสัดส่วนแบบ SoC ทำให้ในอนาคตสามารถนำ `TaskManager` ไปต่อกับ GUI (เช่น PyQt) หรือ REST API (FastAPI) ได้ทันทีโดยไม่ต้องแก้โค้ด Business Logic เดิม

2. **ถาม: การทดสอบครอบคลุมแค่ไหน?**
   * **ตอบ**: มีชุดทดสอบ Automated Unit Test ใน `tests/test_task_manager.py` ทั้งหมด 8 Test Cases ครอบคลุมทั้ง Model Validation, CRUD, Tag Normalization, Search, Multi-criteria Filter, Sort และ Persistence Reloading ซึ่งรันผ่าน 100% ครับ
