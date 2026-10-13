# 📋 Class Activity 1: Building a Simple CLI Application

> **Week 7: Building a Simple CLI Application, Error Handling & Project Structure**

---

## 📌 สรุปภาพรวมโปรเจกต์ (Project Overview)
โปรเจกต์นี้เป็นการพัฒนาระบบจัดการงานบนคอมมานด์ไลน์ (**CLI Task Manager**) ด้วยภาษา Python โดยเน้นการเปลี่ยนผ่านจากการเขียนสคริปต์ไฟล์เดียวสู่โครงสร้างมาตรฐานวิศวกรรมซอฟต์แวร์:
- **สถาปัตยกรรมแบบแยกส่วน (Modular Architecture):** แยกหน้าที่ของโค้ดตามหลัก Separation of Concerns (SoC) ออกเป็น Presentation Layer (`main.py`), Business Logic Layer (`task_logic.py`) และ Data Access Layer (`task_data.py`)
- **การจัดเก็บข้อมูลถาวร (Data Persistence):** บันทึกและอ่านข้อมูลรายการงานอย่างถาวรในรูปแบบไฟล์ JSON (`tasks.json`)
- **การเขียนโปรแกรมเชิงป้องกัน (Defensive Programming):** จัดการและดักจับข้อผิดพลาด (Exception Handling) ด้วย `try...except` เพื่อป้องกันโปรแกรมขัดข้องจากการป้อนข้อมูลผิดพลาด
- **ฟังก์ชันการทำงานหลัก:** เพิ่มงาน (Add Task), แสดงรายการงาน (List Tasks), ทำเครื่องหมายงานเสร็จสิ้น (Complete Task), ลบงาน (Delete Task), และค้นหางาน (Search Tasks)

---

## ⚠️ ตำแหน่งโฟลเดอร์โปรเจกต์ (Project Directory Navigation)
> **หมายเหตุสำคัญ:** โฟลเดอร์นี้เป็นเพียงหน้ารวมระดับบน (Root of Activity) **ตัวโค้ดโปรเจกต์จริง คู่มือการทดลอง และผลลัพธ์จะต้องเข้าโฟลเดอร์ย่อยไปอีก 1 ขั้น**

```text
Class_activity_1/
├── README.md                                                     # 📄 ไฟล์นี้ (Overview สรุปภาพรวม)
└── Class_activity_1_Building-a-Simple-CLI-Application-main/     # 📁 โฟลเดอร์โปรเจกต์ (ต้องเข้าโฟลเดอร์นี้)
    ├── my-task-manager/                                          # 🚀 โฟลเดอร์ซอร์สโค้ดโปรเจกต์จริง
    │   ├── src/
    │   ├── data/
    │   └── main.py
    ├── classActivity1_Result/                                    # 📸 รูปภาพผลการรันและผลการทดสอบ
    ├── LAB_GUIDE_WEEK7.md                                        # 📘 คู่มือปฏิบัติการฉบับเต็ม
    └── README.md                                                 # 📖 เอกสารอธิบายการใช้งานโปรเจกต์
```

---

## 🚀 วิธีเข้าสู่โฟลเดอร์โปรเจกต์และรันโปรแกรม
ใช้คำสั่งด้านล่างเพื่อเข้าสู่โฟลเดอร์โปรเจกต์จริงและเริ่มรันโปรแกรม:

```bash
# 1. เข้าสู่โฟลเดอร์โปรเจกต์
cd Class_activity_1_Building-a-Simple-CLI-Application-main/my-task-manager

# 2. รันโปรแกรม
python main.py
```
