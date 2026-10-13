# 🏛️ Class Activity 2: OOP Fundamentals & Refactoring CLI Task Manager

> **Week 8: Object-Oriented Programming (OOP) Fundamentals & Refactoring the CLI Task Manager**

---

## 📌 สรุปภาพรวมโปรเจกต์ (Project Overview)
โปรเจกต์นี้เป็นการนำระบบจัดการงาน (CLI Task Manager) จากสัปดาห์ก่อนหน้ามารีแฟกเตอร์ (Refactoring) ใหม่ทั้งหมด จากเดิมที่เขียนแบบ Procedural Programming (ใช้ Dictionary และฟังก์ชันแยกส่วน) มาสู่การเขียนโปรแกรมเชิงวัตถุ (**Object-Oriented Programming: OOP**):
- **Classes & Objects:** ออกแบบคลาส `Task` เป็นพิมพ์เขียวแทนข้อมูลงานแต่ละรายการ และคลาส `TaskManager` ทำหน้าที่จัดการคอลเลกชันงานทั้งหมด
- **หลักการ OOP สำคัญ:** ใช้งาน Constructor (`__init__`), พารามิเตอร์ `self`, และ Encapsulation (การห่อหุ้ม Attributes และ Methods เข้าไว้ด้วยกัน)
- **Data Persistence & Automated Tests:** จัดเก็บข้อมูลลงไฟล์ JSON พร้อมชุดทดสอบอัตโนมัติ (Automated Unit Tests ด้วย `pytest` / `unittest`) สำหรับตรวจทานความถูกต้องของคลาส
- **โครงสร้างคลังโค้ด:** ประกอบด้วยชุดฝึกปฏิบัติสำหรับนักศึกษา (`starter_code`), โค้ดเฉลยฉบับสมบูรณ์ (`solution`), และสมุดงานสำหรับ Google Colab (`colab`)

---

## ⚠️ ตำแหน่งโฟลเดอร์โปรเจกต์ (Project Directory Navigation)
> **หมายเหตุสำคัญ:** โฟลเดอร์นี้เป็นเพียงหน้ารวมระดับบน (Root of Activity) **ตัวโค้ดโปรเจกต์จริง คู่มือ และผลลัพธ์จะต้องเข้าโฟลเดอร์ย่อยไปอีก 1 ขั้น**

```text
Class_activity_2/
├── README.md                  # 📄 ไฟล์นี้ (Overview สรุปภาพรวม)
├── classActivity2_Result/     # 📸 รูปภาพผลการรันและผลการทดสอบ
└── my-oop-task-manager/       # 📁 โฟลเดอร์โปรเจกต์ (ต้องเข้าโฟลเดอร์นี้)
    ├── starter_code/          # 🧑‍💻 โค้ดสำหรับฝึกทำแล็บ (มี TODOs & Unit Tests)
    ├── solution/              # 👨‍🏫 โค้ดเฉลยฉบับสมบูรณ์
    ├── colab/                 # ☁️ สมุดงาน Jupyter Notebook สำหรับ Google Colab
    └── README.md              # 📖 คู่มือการเรียนรู้และเอกสารโปรเจกต์ฉบับเต็ม
```

---

## 🚀 วิธีเข้าสู่โฟลเดอร์โปรเจกต์และรันโปรแกรม
ใช้คำสั่งด้านล่างเพื่อเข้าสู่โฟลเดอร์โปรเจกต์และเริ่มรันโปรแกรม:

```bash
# 1. เข้าสู่โฟลเดอร์โปรเจกต์
cd my-oop-task-manager/solution    # หรือ cd my-oop-task-manager/starter_code

# 2. รันโปรแกรม
python main.py

# (ทางเลือก) รันการทดสอบ Unit Tests
pytest tests/
```
