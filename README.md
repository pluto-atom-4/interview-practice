# 🧠 Python Interview Practice Monorepo

Welcome to your all-in-one monorepo for practicing coding interview questions in Python! This project is designed to help you master algorithms, data structures, system design, and object-oriented design — all in one place.

---

## 📁 Project Structure

```
interview-practice/
 ├── algorithms/ # Sorting, searching, recursion, etc.
 ├── data_structures/ # Arrays, linked lists, trees, graphs
 ├── system_design/ # Notes and mock designs
 ├── ood/ # Object-oriented design and patterns
 ├── leetcode/ # Individual LeetCode problems
 ├── utils/ # Helper functions and utilities
 ├── tests/ # Pytest-based unit tests
 ├── requirements.txt # Dependencies
 └── README.md # You're here!
```
---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```
   git clone https://github.com/your-username/interview-practice.git
   cd interview-practice
   ```
2. **Create and activate a virtual environment**
   ```
   python -m venv venv
   venv\Scripts\activate  # Windows
   # OR
   source venv/bin/activate  # macOS/Linux

   ```
3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Run tests**
   ```
   pytest
   ```

## 🧹 Code Quality
This project uses **Black** and **isort** for formatting. Pre-commit hooks are configured to run automatically before each commit.
To run manually:
```
pre-commit run --all-files
```

## 🧪 How to Contribute
- Add new problems under `leetcode/` or `algorithms/`
- Write clean, well-documented code
- Add corresponding tests in `tests/`
- Format with `black` and `isort` before committing

## 📚 Resources
- (LeetCode)[https://leetcode.com/]
- (System Design Primer)[https://github.com/donnemartin/system-design-primer]
- (Grokking the System Design Interview)[https://www.educative.io/courses/grokking-the-system-design-interview]

## 🚀 Goals
- Build a strong foundation in problem-solving
- Prepare for technical interviews at top tech companies
- Track progress and improve coding fluency

Happy coding!
