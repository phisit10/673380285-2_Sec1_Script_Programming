# 🚀 Class Activity 4: Project Planning & Design — Enhanced Task Manager

> **Week 11: Project Planning & Design: Building an Enhanced Task Manager**

---

## 📌 สรุปภาพรวมโปรเจกต์ (Project Overview)
โปรเจกต์นี้เป็นการฝึกกระบวนการออกแบบและวางแผนสถาปัตยกรรมซอฟต์แวร์อย่างเป็นระบบ (**Design Before Code**) ก่อนเริ่มต้นลงมือเขียนโค้ด เพื่อสร้างระบบจัดการงานขั้นสูง (**Enhanced Task Manager CLI**):
- **Software Architecture & Planning:** เริ่มต้นจากการกำหนดสเปกและบันทึกข้อกำหนดในเอกสาร `PLAN.md` พร้อมแบ่งโครงสร้างเป็น Multi-layer Architecture (UI, Business Logic, Domain Models, Data Persistence)
- **Advanced OOP (Inheritance & Polymorphism):** ออกแบบคลาสแม่ `Task` และต่อยอดเป็นคลาสลูกเฉพาะทาง ได้แก่ `DueDateTask` (รองรับวันกำหนดส่ง) และ `PriorityTask` (จัดการระดับความสำคัญ Low/Medium/High)
- **Enhanced Features:** รองรับการค้นหางาน (Search), การกรองงานตามเงื่อนไข (Filter), การจัดเรียงตามวันที่หรือลำดับความสำคัญ (Sorting), และระบบจัดการแท็ก (Tags)
- **Data Persistence:** จัดเก็บข้อมูลงานทุกประเภทลงในไฟล์ JSON พร้อมระบบแปลงข้อมูลคืนรูปวัตถุ (Serialization & Deserialization)

---

## ⚠️ ตำแหน่งโฟลเดอร์โปรเจกต์ (Project Directory Navigation)
> **หมายเหตุสำคัญ:** โฟลเดอร์นี้เป็นเพียงหน้ารวมระดับบน (Root of Activity) **ตัวโค้ดโปรเจกต์จริง เอกสารวางแผน และผลลัพธ์จะต้องเข้าโฟลเดอร์ย่อยไปอีก 1 ขั้น**

```text
Class_activity_4/
├── README.md                      # 📄 ไฟล์นี้ (Overview สรุปภาพรวม)
├── classActivity4_Result/         # 📸 รูปภาพผลการรันและผลการทดสอบ
└── enhanced-task-manager-design/  # 📁 โฟลเดอร์โปรเจกต์ (ต้องเข้าโฟลเดอร์นี้)
    ├── PLAN.md                    # 📐 เอกสารวางแผนและการออกแบบสถาปัตยกรรมระบบ
    ├── src/                       # 🚀 ซอร์สโค้ดโปรเจกต์ (task, task_manager, cli, persistence)
    │   ├── task.py
    │   ├── task_manager.py
    │   ├── cli_interface.py
    │   └── data_persistence.py
    ├── data/                      # 💾 โฟลเดอร์เก็บข้อมูลไฟล์ JSON
    ├── main.py                    # 💻 สคริปต์หลักสำหรับเปิดใช้งานระบบ
    └── README.md                  # 📖 คู่มือโปรเจกต์และข้อกำหนดการส่งงานฉบับเต็ม
```

---

## 🚀 วิธีเข้าสู่โฟลเดอร์โปรเจกต์และรันโปรแกรม
ใช้คำสั่งด้านล่างเพื่อเข้าสู่โฟลเดอร์โปรเจกต์และเริ่มรันโปรแกรม:

```bash
# 1. เข้าสู่โฟลเดอร์โปรเจกต์
cd enhanced-task-manager-design

# 2. รันโปรแกรม
python main.py
```
