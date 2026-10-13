# 🌐 Class Activity 3: Interacting with Web APIs

> **Week 10: Interacting with Web APIs: Fetching and Processing JSON Data**

---

## 📌 สรุปภาพรวมโปรเจกต์ (Project Overview)
โปรเจกต์นี้เป็นการพัฒนาระบบเชื่อมต่อและประมวลผลข้อมูลผ่านเครือข่ายอินเทอร์เน็ต (**Web API Fetcher**) ด้วยภาษา Python:
- **HTTP Client & Requests:** เรียนรู้วิธีการส่งคำขอ HTTP GET Request ไปยัง REST API ภายนอก (เช่น JSONPlaceholder) ด้วยไลบรารี `requests`
- **JSON Processing:** แปลงข้อมูลตอบกลับในรูปแบบ JSON ให้อยู่ในโครงสร้างข้อมูลของภาษา Python (Dictionary, List) และการเข้าถึงข้อมูลที่ซ้อนกันหลายชั้น (Nested Data)
- **HTTP Status Codes:** ทำความเข้าใจและตรวจสอบสถานะการตอบกลับจากเซิร์ฟเวอร์ เช่น `200 OK`, `404 Not Found`, `500 Internal Server Error`
- **Robust Error Handling:** ออกแบบระบบดักจับข้อผิดพลาดของเครือข่าย เช่น `RequestException`, `Timeout`, `ConnectionError` เพื่อป้องกันไม่ให้โปรแกรมหยุดทำงานกะทันหัน

---

## ⚠️ ตำแหน่งโฟลเดอร์โปรเจกต์ (Project Directory Navigation)
> **หมายเหตุสำคัญ:** โฟลเดอร์นี้เป็นเพียงหน้ารวมระดับบน (Root of Activity) **ตัวโค้ดโปรเจกต์จริง การบ้าน และผลลัพธ์จะต้องเข้าโฟลเดอร์ย่อยไปอีก 1 ขั้น**

```text
Class_activity_3/
├── README.md                  # 📄 ไฟล์นี้ (Overview สรุปภาพรวม)
├── classActivity3_Result/     # 📸 รูปภาพผลการรันและผลการทดสอบ
└── my-api-fetcher/            # 📁 โฟลเดอร์โปรเจกต์ (ต้องเข้าโฟลเดอร์นี้)
    ├── src/                   # 🚀 ซอร์สโค้ดฟังก์ชันเรียก API และจัดการข้อมูล
    ├── assignments/           # 📝 โจทย์และการบ้านประจำสัปดาห์
    ├── colab/                 # ☁️ สมุดงาน Jupyter Notebook สำหรับ Google Colab
    ├── main.py                # 💻 สคริปต์หลักสำหรับเรียกทำงานโปรแกรม
    ├── requirements.txt       # 📦 รายการไลบรารีที่จำเป็น (requests)
    └── README.md              # 📖 คู่มือการเรียนรู้ฉบับละเอียด
```

---

## 🚀 วิธีเข้าสู่โฟลเดอร์โปรเจกต์และรันโปรแกรม
ใช้คำสั่งด้านล่างเพื่อเข้าสู่โฟลเดอร์โปรเจกต์จริง ติดตั้งแพ็กเกจ และรันโปรแกรม:

```bash
# 1. เข้าสู่โฟลเดอร์โปรเจกต์
cd my-api-fetcher

# 2. ติดตั้ง Dependencies
pip install -r requirements.txt

# 3. รันโปรแกรม
python main.py
```
