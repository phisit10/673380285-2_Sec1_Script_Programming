# src/task.py

class Task:
    """
    คลาสสำหรับจำลองข้อมูลงานแต่ละรายการ (Single Task)
    
    Attributes:
        id (int): รหัสประจำงานที่ไม่ซ้ำกัน
        description (str): รายละเอียดข้อความของงาน
        completed (bool): สถานะการทำงาน (True = ทำเสร็จแล้ว, False = ยังไม่เสร็จ)
    """

    def __init__(self, id: int, description: str, completed: bool = False):
        """
        Constructor สำหรับสร้าง Instance ของ Task
        
        Args:
            id (int): รหัสของงาน
            description (str): คำอธิบายงาน
            completed (bool, optional): สถานะงาน เริ่มต้นเป็น False
        """
        self.id = id
        self.description = description
        self.completed = completed

    def mark_complete(self):
        """
        Method สำหรับเปลี่ยนสถานะของงานนี้ให้เป็นเสร็จสมบูรณ์ (completed = True)
        """
        self.completed = True

    def to_dict(self) -> dict:
        """
        แปลงข้อมูลจาก Task Object ให้อยู่ในรูป Dictionary
        เพื่อความสะดวกในการบันทึกลงไฟล์ JSON (Serialization)
        
        Returns:
            dict: เช่น {"id": 1, "description": "Buy milk", "completed": False}
        """
        return {
            "id": self.id,
            "description": self.description,
            "completed": self.completed,
        }

    def __str__(self) -> str:
        """
        Dunder method สำหรับส่งคืนข้อความที่อ่านง่ายเมื่อใช้ print(task) หรือ str(task)
        
        Returns:
            str: รูปแบบ "ID: <id> | Description: <desc> | Status: Completed/Pending"
        """
        status = "Completed" if self.completed else "Pending"
        return f"ID: {self.id} | Description: {self.description} | Status: {status}"

    def __repr__(self) -> str:
        """
        Dunder method สำหรับส่งคืน string เชิงเทคนิค สำหรับการ Debugging
        
        Returns:
            str: รูปแบบ "Task(id=<id>, description='<desc>', completed=<completed>)"
        """
        return (
            f"Task(id={self.id}, description={self.description!r}, "
            f"completed={self.completed})"
        )
