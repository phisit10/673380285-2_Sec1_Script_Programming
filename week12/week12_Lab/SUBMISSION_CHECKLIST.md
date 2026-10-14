# ✅ Submission Checklist: Week 12 Final Project & Presentation

เอกสารตรวจสอบความพร้อมก่อนส่งงานและนำเสนอผลงาน สำหรับนักศึกษาชั้นปีที่ 2  
ให้นักศึกษาตรวจสอบทุกข้อให้ครบถ้วนก่อนส่งลิงก์และขึ้นนำเสนอในชั้นเรียน

🔗 **GitHub Repository**: [https://github.com/phisit10/673380285-2_Sec1_Script_Programming](https://github.com/phisit10/673380285-2_Sec1_Script_Programming)

---

## 🗂️ 1. รายการตรวจสอบโครงสร้าง Repository & Git

- [x] **Git Initialization**: โฟลเดอร์โปรเจกต์มีการติดตั้ง Git และเชื่อมโยงกับ GitHub เรียบร้อย
- [x] **Commit History**: มีประวัติการ Commit อย่างสม่ำเสมอ (ไม่ส่งงานด้วย 1 Commit รวดเดียว) แสดงให้เห็นกระบวนการพัฒนาทีละ Phase
- [x] **Repository Visibility**: ตั้งค่า Repository เป็น Public หรือได้ทำการเพิ่มอีเมลของอาจารย์/TA เป็น Collaborator แล้ว
- [x] **`.gitignore`**: มีไฟล์ `.gitignore` ที่กรองไฟล์แคช `__pycache__/`, `.env`, `.vscode/` ไม่ให้หลุดขึ้น GitHub
- [x] **ไม่มี Dead Files**: ลบไฟล์ทดลองที่ไม่ได้ใช้งานออกเรียบร้อยแล้ว

---

## 💻 2. รายการตรวจสอบซอร์สโค้ด (Source Code & Functionality)

### `src/task.py`
- [x] คลาส `Task` มีแอตทริบิวต์ `tags` (list of strings)
- [x] เมธอด `add_tag(tag)` ตัดช่องว่างส่วนเกินและแปลงเป็นตัวพิมพ์เล็ก (Normalized) ป้องกันแท็กซ้ำ
- [x] เมธอด `remove_tag(tag)` สามารถลบแท็กได้อย่างถูกต้อง
- [x] คลาส `DueDateTask` สืบทอดจาก `Task`, ตรวจสอบรูปแบบวันที่ `YYYY-MM-DD`, และมีเมธอด `to_dict()` / `__str__()` ที่ถูกต้อง
- [x] คลาส `PriorityTask` สืบทอดจาก `Task`, ตรวจสอบระดับความสำคัญ (`High`, `Medium`, `Low`), และมีเมธอด `to_dict()` / `__str__()` ที่ถูกต้อง

### `src/data_persistence.py`
- [x] สามารถบันทึกงานลงไฟล์ `data/tasks.json` ด้วย `json.dump(..., indent=4)`
- [x] สามารถโหลดข้อมูลจากไฟล์ JSON และแปลงกลับเป็น Object ตาม Class จริง (`Task`, `DueDateTask`, `PriorityTask`) โดยดูจากฟิลด์ `_type`
- [x] มี `setdefault('tags', [])` เพื่อรองรับไฟล์ข้อมูลเก่าโดยไม่เกิด Error
- [x] มี Error Handling ดักจับไฟล์เสียหาย (`json.JSONDecodeError`) หรือไฟล์ไม่พบ

### `src/task_manager.py`
- [x] การสร้างงานใหม่ทุกประเภททำงานได้ถูกต้อง และกำหนด ID อัตโนมัติไม่ซ้ำกัน
- [x] ฟังก์ชัน `search_tasks(keyword)` ค้นหาคำค้นหาบางส่วน (Partial match) ทั้งใน Description และ Tags แบบไม่สนตัวพิมพ์เล็ก-ใหญ่
- [x] ฟังก์ชัน `filter_tasks(...)` กรองข้อมูลได้ถูกต้อง ทั้งแบบเงื่อนไขเดียวและรวมหลายเงื่อนไข (Status, Due Date Before/After, Priority, Tags)
- [x] ฟังก์ชัน `sort_tasks(...)` รองรับการจัดเรียงตาม ID, Description, Completed, Due Date (ผลักงานที่ไม่มีวันส่งไปท้ายสุด) และ Priority (High -> Medium -> Low)
- [x] รองรับทั้ง Ascending และ Descending (`reverse=True`)

### `src/cli_interface.py` & `main.py`
- [x] เมนูแสดงตัวเลือกครบถ้วน 0-9 
- [x] มีการตรวจสอบ Input ของผู้ใช้ (เช่น วันที่ต้องเป็น YYYY-MM-DD, Priority ต้องเป็น High/Medium/Low, ID ต้องเป็นตัวเลข)
- [x] โปรแกรมไม่ Crash เมื่อผู้ใช้กรอกข้อมูลผิดรูปแบบ
- [x] `main.py` สามารถรันได้ด้วยคำสั่ง `python main.py` โดยไม่มี Error

---

## 🧪 3. รายการตรวจสอบการทดสอบระบบ (Testing & Quality)

- [x] รันชุดทดสอบอัตโนมัติผ่านครบทุกเคส (OK) ด้วยคำสั่ง:
  ```bash
  python -m unittest discover tests
  ```
- [x] โค้ดทั้งหมดเขียนถูกต้องตามมาตรฐาน PEP 8 (เว้นวรรค, การตั้งชื่อตัวแปรและฟังก์ชัน)
- [x] มี Docstrings อธิบายคลาสและเมธอดสำคัญครบถ้วน

---

## 📄 4. รายการตรวจสอบเอกสารประกอบ (Documentation)

- [x] **`README.md`**:
  - [x] ใส่ชื่อ-นามสกุล และรหัสนักศึกษาครบถ้วน
  - [x] ตรวจสอบคำอธิบายสถาปัตยกรรมและขั้นตอนการรันโปรแกรม
- [x] **`PLAN.md`**:
  - [x] มีการบันทึกปัญหาทางเทคนิคที่พบ (Technical Challenges) และวิธีแก้ไข
  - [x] มีการบันทึกสิ่งที่ได้เรียนรู้ (Lessons Learned) และแนวทางพัฒนาต่อยอด (Future Work)
- [x] **`data/tasks.json`**:
  - [x] มีข้อมูลงานตัวอย่างอย่างน้อย 5-6 รายการ ครบทุกประเภทและมี Tags พร้อมสำหรับการสาธิต (Demo)

---

## 🎤 5. รายการตรวจสอบการนำเสนอผลงาน (Presentation Readiness)

- [x] **สไลด์การนำเสนอ**: เตรียมสไลด์ครบทั้ง 7 ส่วน:
  1. Introduction (แนะนำตัว & วัตถุประสงค์)
  2. Problem Solved (ปัญหาที่โปรแกรมแก้ไข)
  3. Live Demo (การสาธิตการทำงานจริง)
  4. Software Architecture (อธิบายโครงสร้าง OOP & Separation of Concerns)
  5. Technical Challenges & Solutions (ปัญหาที่พบ เช่น Polymorphic Sort และวิธีแก้)
  6. Lessons Learned (บทเรียนที่ได้จากการทำโปรเจกต์)
  7. Future Work & Q&A (แผนการพัฒนาต่อยอด)
- [x] **Live Demo Script**: ซ้อมลำดับขั้นตอนการกดเมนูใน Terminal ให้คล่องแคล่ว
- [x] **Time Management**: ควบคุมเวลาการนำเสนอให้อยู่ภายใน 5 - 7 นาที
- [x] **Backup Plan**: มีแผนสำรองกรณีโปรแกรมติดขัดระหว่าง Demo (เช่น เตรียมภาพจับหน้าจอ หรือไฟล์บันทึกสำรอง)
