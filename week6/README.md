# 🧩 Week 6: Functions, Modular Programming & Python Standard Library

> **รายวิชา:** Script Programming (Sec 1)  
> **ผู้จัดทำ:** นายพิสิษฐ์ ทรัพย์อุดมโชติ (รหัสนักศึกษา: 673380285-2)

---

## 📌 สรุปภาพรวมประจำสัปดาห์ (Week Overview)
สัปดาห์ที่ 6 มุ่งเน้นการเขียนโปรแกรมเชิงโครงสร้างแบบแยกส่วน (Modular Programming) และการนำโค้ดกลับมาใช้ซ้ำ (Code Reusability) โดยการใช้ฟังก์ชันและโมดูลในภาษา Python:
- **Function Definition & Calls:** การสร้างฟังก์ชันด้วย `def`, การส่งผ่านพารามิเตอร์ (Parameters), การกำหนดค่าเริ่มต้น (Default Arguments), การคืนค่าผลลัพธ์ด้วย `return` และการเขียน Docstrings
- **Defensive Function Logic:** การจัดการกรณีผิดพลาดภายในฟังก์ชัน เช่น การป้องกันการหารด้วยศูนย์ (Division by zero)
- **Custom Modules:** การสร้างโมดูลของตนเอง (`my_utils.py`) และนำเข้า (`import`) ไปใช้ในโปรแกรมอื่น (`main_program.py`)
- **Python Standard Library:** การเรียกใช้งานโมดูลมาตรฐานที่มาพร้อมกับ Python เช่น `math`, `random`, `datetime`, `os`, และ `json`
- **Code Refactoring:** การปรับปรุงโครงสร้างโค้ดเดิม (Refactoring) โดยดึงส่วนโค้ดที่ซ้ำซ้อนมาเป็นฟังก์ชันย่อย เพื่อให้อ่านง่ายและบำรุงรักษาสะดวก

---

## 📂 โครงสร้างไฟล์ภายในโฟลเดอร์ (Directory Structure)

```text
week6/
├── README.md                      # 📄 ไฟล์นี้ (สรุปภาพรวมประจำสัปดาห์)
├── Lab/                           # 🧪 โฟลเดอร์งานปฏิบัติการ (Labs)
│   ├── 6.1/
│   │   └── lab6_1.py              # 🧮 เครื่องคิดเลขแยกฟังก์ชัน (Calculator Functions)
│   └── 6.2/
│       ├── my_utils.py            # 📦 โมดูลกำหนดเอง (greet, is_prime)
│       └── main_program.py        # 🚀 โปรแกรมหลักที่ import โมดูลมาใช้งาน
└── Activity/                      # 🎯 โฟลเดอร์กิจกรรมการเรียนรู้ (Activities)
    ├── 6.1/
    │   └── activity_6.1.py        # 🔄 โค้ดรีแฟกเตอร์ฟังก์ชันจำแนกตัวเลขจาก Week 2
    └── 6.2/
        └── Activity_6.2.md        # 📘 เอกสารสรุปประโยชน์ของ Modular Programming & Standard Library
```

---

## 📝 รายละเอียดการทดลองและกิจกรรม (Labs & Activities)

### 1. Lab 6.1: Simple Calculator Functions (`Lab/6.1/lab6_1.py`)
- รวมฟังก์ชันการคำนวณพื้นฐาน: `add()`, `subtract()`, `multiply()`, `divide()` (มีระบบดักจับการหารด้วย 0)
- **Challenge Function:** ฟังก์ชันยกกำลัง `power(base, exponent=2)` ที่ใช้ Default Argument เป็นการยกกำลังสองหากไม่ระบุเลขชี้กำลัง
- มีเมนูแบบโต้ตอบ (`main()`) ให้ผู้ใช้เลือกทำรายการได้ต่อเนื่อง

### 2. Lab 6.2: Custom Module & Standard Library (`Lab/6.2/`)
- **Part 1 (`my_utils.py`):** สร้างโมดูลอรรถประโยชน์ที่มีฟังก์ชัน `greet(name)` และ `is_prime(number)` สำหรับตรวจสอบจำนวนเฉพาะ
- **Part 2 (`main_program.py`):** นำเข้าโมดูล `my_utils` และโมดูลมาตรฐาน `math` (เช่น `math.sqrt()`), `random` (เช่น `random.randint()`) เพื่อทดสอบการทำงาน

### 3. Activity 6.1: Refactoring a Previous Lab (`Activity/6.1/activity_6.1.py`)
- นำโค้ดจำแนกตัวเลขจากสัปดาห์ที่ 2 มารีแฟกเตอร์ใหม่ โดยแยกเป็นฟังก์ชันอิสระ:
  - `is_positive_negative_zero(num)`
  - `is_even_odd(num)`
  - `classify_sign_and_parity(num)`

### 4. Activity 6.2: Modular Programming & Standard Library (`Activity/6.2/Activity_6.2.md`)
- สรุปประโยชน์ 4 ข้อของการเขียนโค้ดแบบแยกส่วน: การทำงานเป็นทีม, การดีบักง่ายขึ้น, การทำ Unit Testing, และการนำโค้ดกลับมาใช้ซ้ำ
- สำรวจโมดูลมาตรฐาน 3 ตัว: `datetime` (จัดการวันเวลา), `os` (จัดการระบบไฟล์และ OS), และ `json` (จัดการข้อมูล JSON)

---

## 💻 วิธีการรันโปรแกรม

```bash
# 1. รันเครื่องคิดเลข (Lab 6.1)
cd Lab/6.1
python lab6_1.py

# 2. รันโปรแกรมทดสอบโมดูล (Lab 6.2)
cd ../6.2
python main_program.py

# 3. รันโค้ดรีแฟกเตอร์ (Activity 6.1)
cd ../../Activity/6.1
python activity_6.1.py
```
