# 📖 Week 5: Data Collections: Dictionaries & Sets

> **รายวิชา:** Script Programming (Sec 1)  
> **ผู้จัดทำ:** นายพิสิษฐ์ ทรัพย์อุดมโชติ (รหัสนักศึกษา: 673380285-2)

---

## 📌 สรุปภาพรวมประจำสัปดาห์ (Week Overview)
สัปดาห์ที่ 5 เรียนรู้โครงสร้างข้อมูลขั้นสูงที่มีประสิทธิภาพสูงสำหรับการค้นหาและจัดการความสัมพันธ์ของข้อมูล ได้แก่ Dictionary และ Set:
- **Dictionary (Key-Value Pairs):** การจับคู่ระหว่าง Key และ Value ช่วยให้ค้นหาข้อมูลได้อย่างรวดเร็วโดยไม่ต้องวนลูป เหมาะสำหรับข้อมูลระบุตัวตน เช่น ข้อมูลผู้ใช้, สต็อกสินค้า, หรือสมุดโทรศัพท์
- **Set (Unique Collections & Set Operations):** โครงสร้างข้อมูลที่เก็บเฉพาะสมาชิกที่ไม่ซ้ำกัน ไม่เรียงลำดับ รองรับการดำเนินการทางคณิตศาสตร์ของเซต เช่น Union (`|`), Intersection (`&`), Difference (`-`)
- **Text Processing & Frequency Counting:** การประยุกต์ใช้ Dictionary ในการนับความถี่ของคำในข้อความ ร่วมกับการทำความสะอาดสตริง (`.strip()`, `.lower()`, `.split()`)
- **Real-World Scenarios:** การวิเคราะห์การนำ Dictionary และ Set ไปใช้ในเกม, เว็บอีคอมเมิร์ซ, และระบบจัดการสิทธิ์ผู้ใช้

---

## 📂 โครงสร้างไฟล์ภายในโฟลเดอร์ (Directory Structure)

```text
week5/
├── README.md                      # 📄 ไฟล์นี้ (สรุปภาพรวมประจำสัปดาห์)
└── Sec1_Week5_673380285_2.ipynb   # 📓 สมุดงาน Jupyter Notebook (Lab & Activities)
```

---

## 📝 รายละเอียดการทดลองและกิจกรรม (Labs & Activities)

### 1. Lab 5.1: Simple Contact Book Manager (Dictionary Focus)
- สร้างโปรแกรมจัดการสมุดโทรศัพท์/รายชื่อติดต่อ
- รองรับการเพิ่มรายชื่อใหม่ (`contacts[name] = phone`), ค้นหาเบอร์โทรตามชื่อ, แก้ไขข้อมูลเบอร์โทร และลบรายชื่อติดต่อ

### 2. Lab 5.2: Course Enrollment & Collaboration (Set Focus)
- จัดการรายชื่อนักศึกษาที่ลงทะเบียนในวิชาต่างๆ
- ใช้ Set Operations ในการวิเคราะห์ข้อมูล:
  - **Union (`|`):** นักศึกษาทั้งหมดที่ลงเรียนอย่างน้อย 1 รายวิชา
  - **Intersection (`&`):** นักศึกษาที่ลงเรียนซ้ำกันทั้งสองวิชา
  - **Difference (`-`):** นักศึกษาที่ลงวิชาแรกแต่ไม่ได้ลงวิชาที่สอง

### 3. Activity 5.1: Real-World Applications Discussion
- อภิปรายและตอบคำถามเชิงวิเคราะห์:
  - *Dictionary ในเกม:* ใช้เก็บ Inventory (ชื่อไอเทม -> จำนวน), สถานะตัวละคร (HP/MP)
  - *Dictionary ใน E-commerce:* ใช้ Product ID เป็น Key เพื่อเข้าถึงราคาและจำนวนสต็อก
  - *Set ในระบบความปลอดภัย:* ตรวจสอบ Blacklist IP หรือสิทธิ์ใช้งานของผู้ใช้แบบไม่ซ้ำกันอย่างรวดเร็ว

### 4. Activity 5.2: Word Frequency Counter
- เขียนโปรแกรมนับความถี่ของแต่ละคำในประโยคที่ผู้ใช้ป้อน
- ประยุกต์ใช้การแปลงตัวพิมพ์เล็ก (`.lower()`), แยกคำ (`.split()`), ตัดเครื่องหมายวรรคตอน (`.strip()`), และนับสะสมใน Dictionary

---

## 💻 วิธีเปิดใช้งานและรันไฟล์
เปิดใช้งานไฟล์ Jupyter Notebook บน VS Code หรือ Jupyter Lab:

```bash
jupyter notebook Sec1_Week5_673380285_2.ipynb
```
