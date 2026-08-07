# TrainBuilder - Architecture Decision Record (ADR)

## Mục tiêu

TrainBuilder là trò chơi giáo dục dành cho trẻ em, giúp luyện Finger Math thông qua việc xây dựng công trình bằng tàu hỏa.

---

# 1. Công nghệ

- Python 3.12+
- pygame-ce
- JSON để lưu dữ liệu
- Không sử dụng database

---

# 2. Cấu trúc Project

TrainBuilder/
│
├── assets/
├── config/
├── data/
├── docs/
├── src/
├── tests/
│
├── main.py
└── requirements.txt

---

# 3. Scene

Game chỉ có 4 Scene:

- Menu
- Config
- Gameplay
- Result

---

# 4. Gameplay Flow

Menu

↓

Config

↓

Gameplay

↓

Result

↓

Gameplay

---

# 5. Game State

Gameplay gồm:

- INTRO
- SHOW_BUILDING
- COUNTDOWN
- QUESTION
- BUILD
- RESULT

---

# 6. Question Engine

Question được sinh hoàn toàn bằng FingerMath Generator.

Gameplay không tự tạo câu hỏi.

---

# 7. Building

Mỗi Building gồm:

- id
- name
- image
- materials

Số toa hàng:

```python
building.wagon_count
```

Không dùng số cố định.

---

# 8. Material

Một câu hỏi chỉ hiển thị:

- một loại vật liệu
- các số trên vật liệu

Ví dụ:

Steel

0 1 2 3 4 5 6 7 8 9

---

# 9. Asset

Không tạo nhiều ảnh theo số.

Ví dụ:

✔ brick.png

❌ brick0.png

❌ brick1.png

❌ brick2.png

...

Số sẽ được render bằng code.

---

# 10. Code Style

- Không hard-code dữ liệu.
- Một class chỉ có một nhiệm vụ.
- Dữ liệu đọc từ JSON.
- Gameplay không chứa thuật toán sinh đề.

---

# 11. Quy tắc phát triển

- Không đổi tên class giữa chừng.
- Không đổi cấu trúc project.
- Không refactor nếu chưa thật sự cần.
- Mỗi PR phải chạy được trước khi sang PR tiếp theo.
