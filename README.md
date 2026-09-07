# Optimization Theory — Genetic Algorithm

Dự án học phần **Lý thuyết Tối ưu**: cài đặt Thuật toán Di truyền (Genetic Algorithm — GA) cho bài toán tối ưu có/không ràng buộc, đối chiếu kết quả với các phương pháp có sẵn (**PyGAD**, **SciPy SLSQP**) làm mốc so sánh.

## Cấu trúc thư mục

```
.
├── 01_unconstrained_optimization.ipynb  # GA vs PyGAD — tối ưu không ràng buộc (Easom, Rastrigin, Rosenbrock, Ackley, Schwefel...)
├── 02_A_constrained_optimization.ipynb  # GA vs SciPy SLSQP — tối ưu có ràng buộc, form nhập hàm mục tiêu + ràng buộc
├── 02_B_examples.ipynb                  # Các bài toán ứng dụng cố định: Entropy tối đa, điểm gần nhất, LP, QP, tối ưu lồi...
├── 03_TSP.ipynb                         # GA mã hóa hoán vị cho bài toán người du lịch, đối chiếu vét cạn
├── 04_symbolic_regression.ipynb         # Genetic Programming (cây biểu thức) cho Symbolic Regression, đối chiếu hồi quy đa thức
├── requirements.txt                 # Thư viện Python cần cài
├── TieuLuan.pdf
├── Deep Learning Report.pdf
├── report/                          # Mã nguồn LaTeX của báo cáo
│   ├── REPORT.tex
│   ├── REPORT.pdf
│   ├── logo.png
│   └── chapters/
│       ├── trang_bia.tex
│       ├── chuong1_co_so_ly_thuyet.tex
│       └── tai_lieu_tham_khao.tex
└── LICENSE
```

## Cài đặt

Yêu cầu Python >= 3.10.

```bash
pip install -r requirements.txt
```

## Cơ sở lý thuyết

GA được cài đặt dựa trên khung lý thuyết gồm 4 phần chính:

1. Tổng quan bài toán tối ưu và họ thuật toán tiến hóa (Evolutionary Computation)
2. Cơ sở khoa học & nguyên lý hoạt động của GA (mã hóa nhị phân, số thực, hoán vị...)
3. Các thành phần cốt lõi: hàm thích nghi, chọn lọc, lai ghép, đột biến, elitism
4. Quy trình thuật toán và điều kiện dừng

Nội dung đầy đủ (định nghĩa toán học, giả mã, bảng đối chiếu thuật ngữ sinh học — tin học...) xem tại [`report/REPORT.pdf`](report/REPORT.pdf).

## Ứng dụng

GA được áp dụng trên 4 nhóm bài toán:

- **Tối ưu không ràng buộc** (Easom, Rastrigin, Rosenbrock, Ackley, Schwefel)
- **Tối ưu có ràng buộc** (ràng buộc tuyến tính và phi tuyến; Entropy tối đa, LP, QP, tối ưu lồi...)
- **Bài toán người du lịch (TSP)** — mã hóa hoán vị, đối chiếu vét cạn
- **Genetic Programming (GP): Symbolic Regression** — cá thể là cây biểu thức, đối chiếu hồi quy đa thức

## Tài liệu tham khảo

1. Holland, J. H. (1975). *Adaptation in Natural and Artificial Systems*. University of Michigan Press.
2. Goldberg, D. E. (1989). *Genetic Algorithms in Search, Optimization, and Machine Learning*. Addison-Wesley.
3. Mitchell, M. (1998). *An Introduction to Genetic Algorithms*. MIT Press.
4. Deb, K., Pratap, A., Agarwal, S., & Meyarivan, T. (2002). A fast and elitist multiobjective genetic algorithm: NSGA-II. *IEEE Transactions on Evolutionary Computation*, 6(2), 182-197.
