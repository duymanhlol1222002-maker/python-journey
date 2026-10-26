# Tuần 14 — Lập trình hướng đối tượng (OOP) trong Python

> **Mục tiêu:** hiểu class và object, biết gom dữ liệu với hành động liên quan, thay đổi hành vi của Bot bằng composition và biết khi nào nên dùng inheritance.

## 1. Tuần này học gì?

Khi chương trình có nhiều biến và hàm, việc gom dữ liệu cùng những hành động liên quan vào một đối tượng sẽ giúp code dễ đọc, sửa và mở rộng hơn.

Tuần này tập trung vào bốn khái niệm:

1. **Class và object:** class là bản thiết kế; object là một đối tượng cụ thể được tạo từ bản thiết kế.
2. **Attributes và methods:** attributes lưu dữ liệu; methods là các hàm mô tả object có thể làm gì.
3. **Composition:** một object có thể nhận hành vi từ bên ngoài, nhờ đó thay đổi cách hoạt động mà không phải sửa class chính.
4. **Inheritance:** một class có thể kế thừa từ class khác khi quan hệ “là một loại của” (is-a) thật sự hợp lý.

## 2. Bài 1 — Class, object và __str__

**File cần làm:** [ex01_classes.py](exercises/ex01_classes.py)

### Yêu cầu

Tạo class Progress để biểu diễn tiến độ công việc. Class nhận hai giá trị:

- completed: số phần đã hoàn thành.
- total: tổng số phần cần hoàn thành.

Class cần có ba thành phần:

- __init__(self, completed, total): lưu hai giá trị vào object.
- percentage(): tính phần trăm theo công thức completed / total * 100.
- __str__(): trả về chuỗi dễ đọc khi in object bằng print().

### Ví dụ

~~~python
progress = Progress(3, 4)
print(progress.percentage())
print(progress)
~~~

Kết quả mong đợi:

~~~text
75.0
Progress: 3/4 (75%)
~~~

### Giải thích

- Progress là class — bản thiết kế cho một tiến độ.
- progress là object — một tiến độ cụ thể.
- completed và total là dữ liệu của object.
- percentage() dùng dữ liệu để tính phần trăm.
- __str__() quyết định object được hiển thị thành văn bản như thế nào.

Cần bảo đảm total hợp lệ để phép tính không chia cho 0.

## 3. Bài 2 — Composition và chiến lược của Bot

**File cần làm:** [ex02_composition.py](exercises/ex02_composition.py)

### Yêu cầu

Tạo class Bot nhận một strategy khi khởi tạo. Bot có method choose_action(state), chuyển state cho strategy và trả về hành động mà strategy lựa chọn.

Tạo ba chiến lược:

- **defensive:** ưu tiên an toàn; có thể chờ nếu đối thủ ở quá gần.
- **balanced:** lựa chọn cân bằng, hướng về mục tiêu.
- **aggressive:** ưu tiên tiến về mục tiêu.

Các strategy phải trả về hành động theo quy ước của bài tập, chẳng hạn left, right hoặc wait khi phù hợp.

### Bot phải hướng về mục tiêu

Không được mặc định Bot luôn đi sang phải. Hành động cần dựa vào vị trí hiện tại và mục tiêu:

- Nếu Bot ở vị trí 1 và mục tiêu là 4, Bot cần đi sang phải.
- Nếu Bot ở vị trí 3 và mục tiêu là 0, Bot cần đi sang trái.

Với defensive, nếu đối thủ ở quá gần thì Bot có thể chọn wait. Nếu không, Bot vẫn cần xét hướng đi tới mục tiêu.

### Composition là gì?

Composition là cách một object sử dụng một object hoặc hành vi khác để làm việc. Trong bài này, Bot nhận strategy từ bên ngoài thay vì cố định tất cả chiến lược bên trong class.

~~~python
bot = Bot(balanced)
action = bot.choose_action(state)
~~~

Có thể tạo Bot với defensive, balanced hoặc aggressive mà không cần viết lại class Bot.

**Điều quan trọng:** muốn thay chiến lược thì truyền strategy khác vào; không cần sửa phần cốt lõi của Bot hoặc arena. Ý tưởng này là dạng đơn giản của Strategy Pattern.

## 4. Bài 3 — Inheritance: Animal và Dog

**File cần làm:** [ex03_inheritance.py](exercises/ex03_inheritance.py)

### Yêu cầu

Tạo class cha Animal:

- Nhận name khi khởi tạo.
- Lưu tên vào object.

Tạo class Dog kế thừa từ Animal:

- Dùng lại phần lưu tên từ class cha.
- Có method speak() trả về câu nói của chó đúng định dạng yêu cầu.

### Ví dụ

~~~python
dog = Dog("Milo")
print(dog.speak())
~~~

Kết quả mong đợi:

~~~text
Milo: woof
~~~

### Inheritance là gì?

Inheritance (kế thừa) cho phép class con sử dụng dữ liệu hoặc hành vi của class cha. Trong ví dụ này, chó là một loại động vật, nên Dog có thể kế thừa Animal.

Không nên dùng inheritance chỉ để tái sử dụng vài dòng code. Nếu mục tiêu là thay đổi một hành vi có thể hoán đổi, như chiến lược của Bot ở Bài 2, composition thường phù hợp hơn.

## 5. Cách làm bài

Nên thực hiện theo thứ tự:

1. Đọc [notes.md](notes.md) để hiểu khái niệm.
2. Mở từng file trong thư mục [exercises](exercises/).
3. Đọc yêu cầu và hoàn thành từng class/method.
4. Tự chạy file Python để xem kết quả.
5. Chạy lệnh kiểm tra của tuần.
6. Khi hiểu ba bài nhỏ, đọc [mini-project](mini-project/README.md) để xem cách áp dụng composition vào Bot.

### Chạy từng bài

Mở terminal tại thư mục gốc của repository và chạy:

~~~bash
python weeks/week-14-oop-essentials/exercises/ex01_classes.py
python weeks/week-14-oop-essentials/exercises/ex02_composition.py
python weeks/week-14-oop-essentials/exercises/ex03_inheritance.py
~~~

Nếu máy dùng lệnh python3, thay python bằng python3.

### Chạy machine check

~~~bash
python weeks/week-14-oop-essentials/checks/check_week.py
~~~

Xem thêm [hướng dẫn kiểm tra](checks/README.md).

> **Lưu ý:** hãy xem check script thực sự kiểm tra file nào. Nếu script kiểm tra module trong thư mục solutions, kết quả PASS chỉ xác nhận những phần mà script đó chạy; bạn vẫn nên tự chạy và kiểm tra các file trong exercises.

## 6. Lỗi thường gặp

- **Nhầm class với object:** class là bản thiết kế; object là một trường hợp cụ thể.
- **Quên self:** method của object thường dùng self để truy cập dữ liệu của chính object đó.
- **Tính phần trăm sai:** dùng completed / total * 100.
- **Không xử lý total bằng 0:** cần ngăn phép chia cho 0.
- **Bot luôn đi một hướng:** phải xét vị trí hiện tại so với goal.
- **Gắn cứng strategy vào Bot:** nếu đổi chiến lược mà phải sửa class Bot thì composition chưa được áp dụng đúng.
- **Kế thừa không cần thiết:** chỉ dùng inheritance khi quan hệ is-a thật sự hợp lý.

## 7. Sau khi hoàn thành, bạn nên hiểu được

- Cách tạo class và object bằng __init__.
- Sự khác nhau giữa attributes và methods.
- Cách dùng __str__ để hiển thị object thành văn bản dễ đọc.
- Cách object nhận hành vi từ bên ngoài bằng composition.
- Vì sao có thể đổi strategy mà không sửa class Bot.
- Khi nào quan hệ is-a phù hợp để dùng inheritance.

## Tài liệu trong tuần

- [Ghi chú bài học](notes.md)
- [Ví dụ minh họa](examples/)
- [Các bài tập](exercises/)
- [Gợi ý](hints.md)
- [Hướng dẫn kiểm tra](checks/README.md)
- [Mini-project: Strategy Composition](mini-project/README.md)
