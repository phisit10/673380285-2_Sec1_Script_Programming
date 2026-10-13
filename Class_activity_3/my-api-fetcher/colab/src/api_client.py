import requests
import json
from typing import Any, Dict, List, Optional

class APIClient:
    """
    คลาสสำหรับเชื่อมต่อกับ JSONPlaceholder REST API
    """
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def _make_request(self, endpoint: str, timeout: int = 10) -> Optional[Any]:
        url = f"{self.BASE_URL}{endpoint}"
        print(f"[INFO] กำลังส่งคำขอ (GET) ไปที่: {url}")
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()  # แจ้งเตือนเมื่อสถานะเป็น 4xx หรือ 5xx
            return response.json()
        except requests.exceptions.HTTPError as errh:
            print(f"[ERROR] HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"[ERROR] Connection Error: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"[ERROR] Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"[ERROR] Request Exception: {err}")
        except json.JSONDecodeError:
            print(f"[ERROR] ไม่สามารถแปลงข้อมูลเป็น JSON ได้: {response.text[:100]}...")
        return None

    def fetch_single_todo(self, todo_id: int) -> Optional[Dict[str, Any]]:
        return self._make_request(f"/todos/{todo_id}")

    def fetch_all_posts(self) -> Optional[List[Dict[str, Any]]]:
        return self._make_request("/posts")

    def fetch_user_todos(self, user_id: int) -> Optional[List[Dict[str, Any]]]:
        return self._make_request(f"/todos?userId={user_id}")
