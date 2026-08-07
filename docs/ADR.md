# TrainBuilder
## Architecture Decision Records (ADR)

Version: Alpha 1.0

---

# Giới thiệu

Tài liệu này ghi lại toàn bộ các quyết định kiến trúc của dự án TrainBuilder.

Mọi thay đổi kiến trúc phải được cập nhật tại đây trước khi chỉnh sửa mã nguồn.

Quy tắc:

- Không thay đổi kiến trúc nếu chưa có ADR mới.
- Không đổi tên class, file hoặc thư mục nếu chưa cập nhật ADR.
- Mọi module mới phải tuân thủ ADR hiện hành.

---

# ARCH-001
## Game Engine

Status: Accepted

### Decision

TrainBuilder sử dụng **Python + pygame-ce**.

### Reason

- Thuần Python.
- Dễ phát triển.
- Dễ bảo trì.
- Phù hợp game 2D.
- Tương thích với FingerMath Generator.

---

# ARCH-002
## Project Structure

Status: Accepted

### Decision

Project sử dụng cấu trúc:

```
TrainBuilder/

assets/
config/
data/
docs/
src/
tests/

main.py
requirements.txt
```

Không được thay đổi cấu trúc thư mục khi chưa có ADR mới.

---

# ARCH-003
## Gameplay Architecture

Status: Accepted

Gameplay được chia thành:

```
Scene
↓
Controller
↓
Engine
↓
Model
```

Scene không chứa business logic.

---

# ARCH-004
## Event Driven

Status: Accepted

Các module giao tiếp thông qua EventBus.

Không gọi trực tiếp giữa các Scene.

---

# ARCH-005
## Scene

Status: Accepted

Các Scene được phép tồn tại:

- Menu
- Config
- Gameplay
- Result

Không tạo thêm Scene khi chưa có ADR.

---

# ARCH-006
## Game State

Status: Accepted

Gameplay sử dụng State Machine.

Danh sách State:

- INTRO
- SHOW_BUILDING
- COUNTDOWN
- QUESTION
- BUILD
- RESULT

Không sử dụng chuỗi if/elif dài để điều khiển gameplay.

---

# ARCH-007
## Question Engine

Status: Accepted

Question Engine là module độc lập.

Gameplay không được sinh câu hỏi.

Question Engine chịu trách nhiệm:

- Sinh câu hỏi
- Kiểm tra quy tắc
- Trả về Question

---

# ARCH-008
## FingerMath Generator

Status: Accepted

Thuật toán sinh câu hỏi sử dụng bộ sinh FingerMath.

Gameplay không được phép can thiệp vào thuật toán sinh đề.

Mọi thay đổi quy tắc phải thực hiện bên trong Question Engine.

---

# ARCH-009
## Assets

Status: Accepted

Không hard-code đường dẫn asset.

Toàn bộ asset được quản lý bởi AssetManager.

Gameplay chỉ yêu cầu asset thông qua AssetManager.

---

# ARCH-010
## Building

Status: Accepted

Mỗi Building phải khai báo:

- id
- name
- materials
- image

Số lượng toa hàng được xác định bằng:

```
building.wagon_count
```

Không sử dụng hằng số cố định để xác định số toa.

---

# ARCH-011
## Material

Status: Accepted

Mỗi câu hỏi tương ứng với đúng một loại vật liệu.

Một câu hỏi chỉ hiển thị:

- một loại vật liệu
- các số tương ứng

Không hiển thị nhiều loại vật liệu trong cùng một câu.

---

# ARCH-012
## Code Style

Status: Accepted

Quy tắc:

- Một class chỉ có một nhiệm vụ.
- Không viết hàm quá dài.
- Không hard-code dữ liệu.
- Ưu tiên đọc dữ liệu từ JSON.
- Ưu tiên tái sử dụng module.

---

# ARCH-013
## Naming Convention

Status: Accepted

Tên class:

PascalCase

Ví dụ:

```
SceneManager
QuestionEngine
Building
Material
```

Tên file:

snake_case

Ví dụ:

```
scene_manager.py
question_engine.py
building.py
```

Tên biến:

snake_case

Ví dụ:

```
building_id

current_question

selected_material
```

Hằng số:

UPPER_CASE

Ví dụ:

```
FPS

WINDOW_WIDTH

TRAIN_SPEED
```

---

# ARCH-014
## Asset Strategy

Status: Accepted

Asset chỉ lưu hình gốc.

Các số trên vật liệu được render bằng code.

Không tạo:

brick0.png

brick1.png

...

brick9.png

Chỉ sử dụng:

brick.png

Sau đó render số bằng pygame.

---

# ARCH-015
## Architecture Freeze

Status: Accepted

Kể từ phiên bản Alpha 1:

- Không thay đổi kiến trúc nếu chưa có ADR mới.
- Không đổi tên module giữa chừng.
- Không refactor khi chưa thật sự cần thiết.

Mọi thay đổi lớn phải được ghi thành ARCH-016, ARCH-017...
