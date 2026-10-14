# 📋 Enhanced Task Manager CLI Application
> **Week 12 Final Project - CP352301 Script Programming**  
> **ผู้จัดทำ:** นายพิสิษฐ์ ทรัพย์อุดมโชติ (รหัสนักศึกษา: 673380285-2) | Section 1  
> **GitHub Repository:** [https://github.com/phisit10/673380285-2_Sec1_Script_Programming](https://github.com/phisit10/673380285-2_Sec1_Script_Programming)

---

## 📌 ภาพรวมของโปรเจกต์ (Project Overview)

**Enhanced Task Manager** คือโปรแกรมบริหารจัดการรายการงานผ่าน Command-Line Interface (CLI) ที่ถูกพัฒนาขึ้นโดยใช้หลักการ **Object-Oriented Programming (OOP)** ขั้นสูง และการแยกส่วนประกอบตามสถาปัตยกรรม **Separation of Concerns (SoC)**

### 🌟 ฟีเจอร์หลัก (Key Features)
1. **รองรับประเภทงาน 3 รูปแบบ**:
   * `Task`: งานทั่วไป
   * `DueDateTask`: งานที่มีกำหนดวันส่ง (ตรวจสอบรูปแบบ `YYYY-MM-DD`)
   * `PriorityTask`: งานที่มีระดับความสำคัญ (`High`, `Medium`, `Low`)
2. **ระบบ Tags (ป้ายกำกับ)**: ติดแท็กหลายป้ายต่องาน 1 ชิ้น ป้องกันแท็กซ้ำ และปรับเป็นพิมพ์เล็กอัตโนมัติ
3. **การค้นหาขั้นสูง (Search)**: ค้นหาคำแบบ Partial Match ทั้งใน Description และ Tags แบบไม่สนตัวพิมพ์เล็ก-ใหญ่
4. **การกรองหลายมิติ (Multi-criteria Filter)**: กรองตามสถานะ, วันส่ง (ก่อน/หลัง), ระดับความสำคัญ และชุดของ Tags พร้อมกันได้
5. **การจัดเรียงเชิงพหุสัณฐาน (Polymorphic Sort)**: เรียงตาม ID, Description, Completed, Due Date (ผลักงานที่ไม่มีวันส่งไปท้ายสุด) และ Priority (`High` -> `Medium` -> `Low`)
6. **Data Persistence**: บันทึกและโหลดไฟล์ `data/tasks.json` อัตโนมัติ พร้อมรองรับความเข้ากันได้ย้อนหลัง (Backward Compatibility)
7. **Automated Unit Testing**: มีชุดทดสอบอัตโนมัติ 8 Test Cases ผ่าน 100%

---

## 🗂️ โครงสร้างโปรเจกต์ (Project Structure)

```text
final_task_manager_project/
├── src/                            # ซอร์สโค้ดหลักของระบบ
│   ├── __init__.py                 # กำหนดให้ src เป็น Python package
│   ├── task.py                     # Data Models: Task, DueDateTask, PriorityTask
│   ├── data_persistence.py         # Data Layer: จัดการอ่าน/เขียนไฟล์ JSON
│   ├── task_manager.py             # Business Logic Layer: CRUD, Search, Filter, Sort
│   └── cli_interface.py            # Presentation Layer: เมนู CLI และ Input Validation
├── data/
│   └── tasks.json                  # ไฟล์เก็บข้อมูลงาน (ตัวอย่าง Demo 7 รายการ)
├── tests/
│   ├── __init__.py
│   └── test_task_manager.py        # ชุดทดสอบ Unit Test อัตโนมัติ (8 เคส)
├── main.py                         # Application Entry Point
├── run.bat                         # สคริปต์รันโปรแกรมบน Windows
├── test.bat                        # สคริปต์รัน Unit Test บน Windows
├── README.md                       # คู่มือการใช้งานไฟล์นี้
└── .gitignore                      # กรองไฟล์ที่ไม่ต้องการขึ้น Git
```

---

## 🚀 วิธีการรันโปรแกรมและชุดทดสอบ (How to Run)

### 1. การรันโปรแกรมหลัก (Run CLI)
* **บน Windows (แนะนำ):**
  ```powershell
  .\run.bat
  ```
* **หรือผ่านคำสั่งมาตรฐาน:**
  ```powershell
  python main.py
  ```

> [!TIP]
> หากพบข้อความ `Python was not found...` บน Windows ให้พิมพ์คำสั่งด้านล่างนี้ใน PowerShell ก่อน 1 ครั้ง:
> ```powershell
> $env:Path = "C:\Users\acer\AppData\Local\Programs\Python\Python310;C:\Users\acer\AppData\Local\Programs\Python\Python310\Scripts;" + $env:Path
> python main.py
> ```

### 2. การรันชุดทดสอบอัตโนมัติ (Automated Unit Tests)
* **บน Windows:**
  ```powershell
  .\test.bat
  ```
* **หรือคำสั่ง unittest:**
  ```powershell
  python -m unittest discover tests
  ```
*ผลลัพธ์ที่ถูกต้อง:*
```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.034s

OK
```

---

## 📄 เอกสารประกอบเพิ่มเติม (Documentation Links)
* [README.md (เอกสารสรุปภาพรวม Week 12)](../README.md)
* [PLAN.md (เอกสารการออกแบบและสรุปปัญหาทางเทคนิค)](../PLAN.md)
* [SUBMISSION_CHECKLIST.md (เช็กลิสต์ความพร้อมก่อนส่งงาน)](../SUBMISSION_CHECKLIST.md)
* [PRESENTATION_GUIDE.md (สคริปต์และขั้นตอนการนำเสนอ 5-7 นาที)](../PRESENTATION_GUIDE.md)
