# Week 8: Lab Basic - การจัดการข้อมูล CSV และ JSON ด้วย Python

โปรเจกต์นี้เน้นการเรียนรู้การประมวลผลไฟล์ข้อมูลโครงสร้างแบบข้อความ (Plaintext Data) สองรูปแบบหลัก ได้แก่ **CSV (Comma Separated Values)** และ **JSON (JavaScript Object Notation)** โดยใช้โมดูลมาตรฐานของ Python ได้แก่ `csv` และ `json` ในการอ่าน เขียน และจัดการข้อมูลอย่างเป็นระบบ

---

## หัวข้อและแนวคิดหลัก (Key Concepts Demonstrated)

* **การอ่านไฟล์ CSV ด้วย `DictReader`**: การอ่านข้อมูลจากไฟล์ CSV โดยใช้แถวแรกเป็น Header เพื่อเข้าถึงข้อมูลในรูปแบบ Dictionary (Key-Value)
* **การเขียนไฟล์ CSV ด้วย `DictWriter`**: การนำข้อมูล List of Dictionaries เขียนกลับลงไฟล์ CSV พร้อมสร้าง Header และจัดรูปแบบที่ถูกต้อง
* **การประมวลผลข้อมูล CSV**: การคำนวณรวบรวมข้อมูลเบื้องต้น (ผลรวม, ค่าเฉลี่ย) และการคัดกรองแถวข้อมูลตามเงื่อนไขที่กำหนด
* **การอ่านไฟล์ JSON ด้วย `json.load`**: การแปลงข้อมูลจากไฟล์ JSON ให้อยู่ในรูป Dictionary หรือ List ของ Python
* **การเขียนไฟล์ JSON ด้วย `json.dump`**: การแปลงวัตถุ Python กลับเป็นไฟล์ JSON พร้อมการใช้ตัวเลือกตกแต่งรูปแบบ (Pretty-printing) เพื่อให้อ่านง่าย
* **การจัดการโครงสร้างข้อมูล JSON**: การเข้าถึงข้อมูลแบบซ้อนกัน (Nested data) การอัปเดตข้อมูลที่มีอยู่ และการเพิ่มชุดข้อมูลใหม่
* **การออกแบบโปรแกรมแบบโมดูลาร์ (Modular Design)**: การแยก Logic การทำงานของ CSV และ JSON ออกเป็นโมดูลย่อยเพื่อความเป็นระเบียบ (`csv_handler.py`, `json_handler.py`)
* **ความเสถียรของโปรแกรม (Robustness)**: การจัดการข้อผิดพลาดเบื้องต้น (Error Handling) สำหรับการเปิด/อ่านไฟล์และการประมวลผลข้อมูล

---

## การตั้งค่าและการใช้งาน (Setup & How to Run)

1. **Clone Repository:**
   ```bash
   git clone https://github.com/phisit10/673380285-2_Sec1_Script_Programming.git
   cd 673380285-2_Sec1_Script_Programming/week8/week8_LabBasic
   ```

2. **เตรียมสภาพแวดล้อมสำหรับรัน (Virtual Environment):**
   *โปรเจกต์นี้ใช้โมดูลมาตรฐานของ Python (`csv`, `json`) จึงไม่จำเป็นต้องใช้ `pip install` เพิ่มเติม แต่แนะนำให้สร้าง Virtual Environment:*
   ```bash
   python -m venv venv
   source venv/bin/activate  # สำหรับ Windows: venv\Scripts\activate
   ```

3. **เตรียมไฟล์ข้อมูลนำเข้า (Data Files):**
   * สร้างโฟลเดอร์ชื่อ `data` ในไดเรกทอรีหลัก: `mkdir data`
   * **`data/input_sales.csv`**: สร้างไฟล์ CSV สำหรับเก็บข้อมูลยอดขายตัวอย่าง (แถวแรกต้องเป็น Header)
   * **`data/input_inventory.json`**: สร้างไฟล์ JSON สำหรับเก็บข้อมูลสินค้าคงคลังตัวอย่าง

4. **รันโปรแกรม:**
   ```bash
   python main.py
   ```

   **ขั้นตอนการทำงานของโปรแกรม:**
   * อ่านไฟล์ `data/input_sales.csv`
   * ประมวลผลและคัดกรองข้อมูลยอดขายเฉพาะรายการที่มียอด 'Amount' >= 100 พร้อมคำนวณผลรวมและค่าเฉลี่ย
   * บันทึกข้อมูลยอดขายที่คัดกรองแล้ว (พร้อมแถวสรุปผล) ลงใน `data/output_filtered_sales.csv`
   * อ่านไฟล์ `data/input_inventory.json`
   * อัปเดตจำนวนสินค้าคงคลังสำหรับ รหัสสินค้า `PROD001` และ `PROD003`
   * เพิ่มรายการสินค้าใหม่ (`PROD004`)
   * บันทึกข้อมูลสินค้าคงคลังที่อัปเดตแล้วลงใน `data/output_updated_inventory.json`

---

## โครงสร้างโปรเจกต์ (Project Structure)

```text
week8_LabBasic/
├── src/
│   ├── __init__.py             # บ่งบอกความเป็น Python Package
│   ├── csv_handler.py          # รวมฟังก์ชันการทำงานเกี่ยวกับ CSV
│   ├── json_handler.py         # รวมฟังก์ชันการทำงานเกี่ยวกับ JSON
│   └── utils.py                # ระบบบันทึก Log และการสร้างไดเรกทอรี
├── data/
│   ├── input_sales.csv         # ไฟล์ข้อมูล CSV ขาเข้า (ผู้ใช้สร้างขึ้น)
│   ├── output_filtered_sales.csv # ไฟล์ CSV ผลลัพธ์จากการคัดกรองและสรุปผล
│   ├── input_inventory.json    # ไฟล์ข้อมูล JSON ขาเข้า (ผู้ใช้สร้างขึ้น)
│   └── output_updated_inventory.json # ไฟล์ JSON ผลลัพธ์หลังการอัปเดต
├── main.py                     # ไฟล์หลักสำหรับรันโปรแกรม
├── .gitignore                  # กำหนดไฟล์/โฟลเดอร์ที่ไม่ต้องการให้ Git ติดตาม
└── README.md                   # เอกสารอธิบายโปรเจกต์
```

---

## การแก้ปัญหาและการตรวจสอบข้อผิดพลาด (Debugging)

* **`FileNotFoundError`**: ตรวจสอบว่าไฟล์ขาเข้า (`input_sales.csv`, `input_inventory.json`) ถูกวางไว้ในโฟลเดอร์ `data/` ถูกต้องแล้วหรือไม่
* **`KeyError` ในการประมวลผล CSV**:
  * มักเกิดจากชื่อ Header ใน `input_sales.csv` ไม่ตรงกับ Key ที่เรียกใช้ในโค้ด (เช่น `'Amount'`, `'Price'`) ให้ตรวจสอบการสะกดคำหรือช่องว่างเกิน (Space)
  * ตรวจสอบว่าระบุ `fieldnames` ใน `DictWriter` ตรงกับ Key ใน Dictionary
* **`json.JSONDecodeError`**:
  * เกิดจากไวยากรณ์ไฟล์ JSON ไม่ถูกต้อง ตรวจสอบเครื่องหมายสัญลักษณ์ เช่น เครื่องหมายจุลภาค (Comma) ที่ขาดหาย หรือการลืมใส่เครื่องหมายคำพูด (Quotes)
  * ตรวจสอบว่าบันทึกไฟล์ด้วย Encoding เป็น **UTF-8**
* **`ValueError` (เช่น `could not convert string to float`)**:
  * เกิดขึ้นเมื่อข้อมูลตัวเลขใน CSV มีสัญลักษณ์ที่ไม่ใช่ตัวเลข (เช่น '$', เครื่องหมายจุลภาค หรือค่าว่าง) ให้ทำการล้างข้อมูล (Clean string) ก่อนแปลงเป็น `float()`
* **ข้อมูลใน JSON ไม่ยอมอัปเดต**:
  * ตรวจสอบว่า `product_id` ที่ต้องการแก้ไขมีตัวตนจริงในไฟล์ `input_inventory.json`
  * ตรวจสอบว่าโครงสร้างข้อมูลของ `inventory_data` เป็น List of Dictionaries ตามที่ฟังก์ชันคาดหวังไว้

---

## แนวทางการพัฒนาต่อ (Extension Ideas)

* **ตัวแปลงไฟล์ CSV-to-JSON / JSON-to-CSV**: พัฒนาสคริปต์สำหรับการแปลงรูปแบบข้อมูลกลับไปกลับมาระหว่าง CSV และ JSON
* **การตรวจสอบความถูกต้องของข้อมูล (Data Validation)**: เพิ่มระบบตรวจสอบประเภทข้อมูลก่อนนำไปประมวลผล
* **การรองรับไฟล์ขนาดใหญ่ (Large File Processing)**: ปรับปรุงโค้ดให้อ่านข้อมูลทีละส่วน (Chunk processing) หรือใช้ไลบรารีเฉพาะทาง เช่น `pandas` หรือ `ijson`
* **การเชื่อมต่อกับ Web API**: ฝึกการส่งคำขอและรับข้อมูล JSON จาก Public API
* **การทำงานร่วมกับระบบฐานข้อมูล**: ใช้ไฟล์ CSV/JSON เป็นตัวกลางในการนำเข้าหรือส่งออกข้อมูลกับฐานข้อมูล (เช่น SQLite)

## แหล่งที่มา
1. https://github.com/MarshallDoyle/Patent 
2. https://github.com/MikeyBeez/RAGAgent 
3. https://automatetheboringstuff.com/2e/chapter16/

