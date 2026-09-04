# KHUNG NỘI DUNG LÝ THUYẾT & HƯỚNG DẪN NGHIÊN CỨU
## THUẬT TOÁN DI TRUYỀN (GENETIC ALGORITHM - GA)

---

## 1. TỔNG QUAN KHUNG NỘI DUNG LÝ THUYẾT

Dưới đây là khung nội dung lý thuyết hoàn chỉnh, chuẩn hóa theo cấu trúc đồ án / luận văn tốt nghiệp ngành Khoa học Máy tính, Công nghệ Thông tin, và Các ngành Kỹ thuật Tối ưu hóa.

```
CHƯƠNG: CƠ SỞ LÝ THUYẾT VỀ THUẬT TOÁN DI TRUYỀN (GENETIC ALGORITHM)
│
├── 1. TỔNG QUAN VỀ BÀI TOÁN TỐI ƯU VÀ HỌ THUẬT TOÁN TIẾN HÓA
│   ├── 1.1. Bài toán Tối ưu hóa và Không gian Tìm kiếm
│   └── 1.2. Họ Thuật toán Tiến hóa (Evolutionary Computation)
│
├── 2. CƠ SỞ KHOA HỌC VÀ NGUYÊN LÝ HOẠT ĐỘNG CỦA GA
│   ├── 2.1. Nguồn gốc Lịch sử và Nguyên lý Sinh học
│   └── 2.2. Phương pháp Mã hóa Giải pháp (Encoding / Chromosome Representation)
│
├── 3. CÁC THÀNH PHẦN VÀ PHÉP TOÁN CỐT LÕI
│   ├── 3.1. Hàm độ thích nghi (Fitness Function) và Ràng buộc
│   ├── 3.2. Phép chọn lọc (Selection Operators)
│   ├── 3.3. Phép lai ghép (Crossover Operators)
│   ├── 3.4. Phép đột biến (Mutation Operators)
│   └── 3.5. Chiến lược giữ lại Cá thể Ưu tú (Elitism)
│
└── 4. QUY TRÌNH THUẬT TOÁN VÀ ĐIỀU KIỆN DỪNG
    ├── 4.1. Sơ đồ khối và Giả mã (Pseudocode)
    └── 4.2. Tiêu chuẩn dừng và Đánh giá sự Hội tụ
```

---

## 2. KHUNG NỘI DUNG ỨNG DỤNG

Song song với phần cơ sở lý thuyết, phần ứng dụng triển khai GA trên các nhóm bài toán cụ thể, đi từ tối ưu hàm số đến bài toán tổ hợp và Machine Learning.

```
CHƯƠNG: ỨNG DỤNG THUẬT TOÁN DI TRUYỀN (GENETIC ALGORITHM)
│
├── 1. Ứng dụng GA trong tối ưu không ràng buộc (Ackley function)
│
├── 2. Ứng dụng GA trong tối ưu có ràng buộc (ràng buộc tuyến tính và ràng buộc phi tuyến)
│
├── 3. Ứng dụng GA trong bài toán TSP
│
└── 4. Ứng dụng GA trong Machine Learning (Feature Selection và Hyperparameter Tuning)
```

---

## 3. CHI TIẾT NỘI DUNG TỪNG PHẦN TRONG LUẬN VĂN

### 3.1. Tổng quan về Bài toán Tối ưu và Họ Thuật toán Tiến hóa
*   **1.1. Bài toán Tối ưu hóa và Không gian Tìm kiếm (Search Space):**
    *   Định nghĩa toán học của bài toán tối ưu cực tiểu / cực đại:
        $$\min_{x \in \Omega} f(x) \quad \text{hoặc} \quad \max_{x \in \Omega} f(x)$$
    *   Thách thức trong tối ưu hóa: Cực trị cục bộ (Local Optima), cực trị toàn cục (Global Optima), bài toán NP-hard và sự bùng nổ tổ hợp.
*   **1.2. Họ Thuật toán Tiến hóa (Evolutionary Algorithms - EA):**
    *   Khái niệm Metaheuristic và các thuật toán tìm kiếm dựa trên quần thể.
    *   Phân loại họ EA: Thuật toán Di truyền (GA), Lập trình Tiến hóa (EP), Chiến lược Tiến hóa (ES), Lập trình Di truyền (GP).

### 3.2. Cơ sở Khoa học và Nguyên lý Hoạt động của GA
*   **2.1. Nguồn gốc Lịch sử & Nguyên lý Sinh học:**
    *   Lịch sử phát triển: Được giới thiệu bởi John Holland (1975) tại Đại học Michigan.
    *   Nguyên lý Darwin: Chọn lọc tự nhiên ("Survival of the Fittest"), di truyền, biến dị.
    *   Bảng đối chiếu thuật ngữ Sinh học và Tin học trong GA:
        | Sinh học | Thuật toán Di truyền (GA) |
        | :--- | :--- |
        | Nhiễm sắc thể (Chromosome) | Mã hóa giải pháp (Solution Encoding) |
        | Gen (Gene) | Một biến / giá trị thành phần trong giải pháp |
        | Cá thể (Individual) | Một giải pháp ứng viên |
        | Quần thể (Population) | Tập hợp các giải pháp tại một thế hệ |
        | Sức sống / Độ thích nghi | Giá trị Hàm độ thích nghi (Fitness Score) |
        | Thế hệ (Generation) | Một vòng lặp tiến hóa |

*   **2.2. Các Phương pháp Mã hóa Giải pháp (Representation / Encoding):**
    *   **Mã hóa Nhị phân (Binary Encoding):** Chuỗi $0$ và $1$ (ví dụ: `10110010`). Phù hợp bài toán rời rạc/logic.
    *   **Mã hóa Số thực (Real-value Encoding):** Dãy số thực (ví dụ: `[3.14, -0.05, 12.8]`). Phù hợp tối ưu hóa liên tục.
    *   **Mã hóa Hoán vị (Permutation Encoding):** Thứ tự tập hợp (ví dụ: `[3, 1, 4, 2, 5]`). Phù hợp bài toán TSP, Lập lịch (Scheduling).
    *   **Mã hóa Dựa trên Cấu trúc (Tree/Graph Encoding):** Cây biểu thức (sử dụng trong Genetic Programming).

### 3.3. Các Thành phần và Phép toán Cốt lõi
*   **3.1. Hàm độ thích nghi (Fitness Function):**
    *   Vai trò: Đánh giá chất lượng của từng cá thể đối với mục tiêu cần tối ưu.
    *   Chuyển đổi từ Hàm mục tiêu (Objective Function) sang Hàm thích nghi (Fitness Function).
    *   Xử lý bài toán có ràng buộc (Constraint Handling): Sử dụng hàm phạt (Penalty Function):
        $$F(x) = f(x) \pm \sum \lambda_i \cdot g_i(x)$$

*   **3.2. Các Phép chọn lọc (Selection Operators):**
    *   **Vòng quay Roulette (Roulette Wheel Selection):** Xác suất chọn cá thể $i$ tỉ lệ thuận với fitness $f_i$:
        $$P_i = \frac{f_i}{\sum_{j=1}^{N} f_j}$$
    *   **Thách đấu (Tournament Selection):** Chọn ngẫu nhiên $k$ cá thể, chọn cá thể tốt nhất trong nhóm.
    *   **Xếp hạng (Rank-based Selection):** Dựa trên thứ hạng thay vì giá trị fitness tuyệt đối để tránh áp đảo của cá thể siêu việt.
    *   **Chiến lược Giữ lại Ưu tú (Elitism):** Bắt buộc giữ lại $k$ cá thể tốt nhất chuyển thẳng sang thế hệ sau mà không qua biến đổi.

*   **3.3. Các Phép lai ghép (Crossover Operators):**
    *   *Tần suất lai ghép ($P_c$):* Thường từ $0.6$ đến $0.95$.
    *   **Cho Mã hóa Nhị phân / Số thực:**
        *   Lai ghép đơn điểm (Single-point Crossover).
        *   Lai ghép đa điểm (Multi-point Crossover).
        *   Lai ghép đồng nhất (Uniform Crossover).
    *   **Cho Mã hóa Hoán vị (Bài toán định tuyến/lập lịch):**
        *   PMX (Partially Matched Crossover).
        *   OX (Order Crossover).
        *   CX (Cycle Crossover).

*   **3.4. Các Phép đột biến (Mutation Operators):**
    *   *Tần suất đột biến ($P_m$):* Thường nhỏ, từ $0.001$ đến $0.05$.
    *   Đột biến đảo bit (Bit-flip Mutation) cho chuỗi nhị phân.
    *   Đột biến Gauss / Uniform cho số thực.
    *   Đột biến hoán đổi (Swap), Đảo ngược (Inversion), Chèn (Insertion) cho mã hóa hoán vị.

### 3.4. Quy trình Thuật toán và Điều kiện Dừng
*   **4.1. Giả mã Thuật toán Di truyền (Pseudocode):**

```text
BEGIN
    t = 0
    Khởi tạo quần thể ban đầu P(t) ngẫu nhiên
    Đánh giá độ thích nghi của P(t)
    
    WHILE NOT (Điều kiện dừng thỏa mãn) DO
        t = t + 1
        Chọn lọc tập bố mẹ S(t) từ P(t-1)
        Thực hiện Lai ghép (Crossover) trên S(t) tạo tập con C(t)
        Thực hiện Đột biến (Mutation) trên C(t)
        Đánh giá độ thích nghi của C(t)
        P(t) = Cập nhật quần thể mới (áp dụng Elitism)
    END WHILE
    
    RETURN Cá thể tốt nhất tìm được
END
```

*   **4.2. Tiêu chuẩn Dừng (Termination Criteria):**
    *   Đạt số lượng thế hệ tối đa ($G_{max}$).
    *   Đạt giá trị fitness mục tiêu.
    *   Quần thể hội tụ (giá trị fitness không cải thiện sau $K$ thế hệ liên tiếp).

---

## 4. TÀI LIỆU THAM KHẢO KINH ĐIỂN ĐỀ XUẤT CẦN TRÍCH DẪN

1.  **Holland, J. H. (1975).** *Adaptation in Natural and Artificial Systems*. University of Michigan Press.
2.  **Goldberg, D. E. (1989).** *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley.
3.  **Mitchell, M. (1998).** *An Introduction to Genetic Algorithms*. MIT Press.
4.  **Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. (2002).** A fast and elitist multiobjective genetic algorithm: NSGA-II. *IEEE Transactions on Evolutionary Computation*, 6(2), 182-197.
