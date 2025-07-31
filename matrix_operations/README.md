
# 🧮 Matrix Operations Tool

A simple web application built with **Gradio**, **NumPy**, and **Pandas** for performing common matrix operations such as addition, subtraction, multiplication, transpose, determinant, and inverse. It also supports exporting results to **Excel** and **PDF** formats.

---

## 🚀 Features

- Input matrices manually or upload `.csv` files
- Supported operations:
  - Add
  - Subtract
  - Multiply
  - Transpose (A)
  - Determinant (A)
  - Inverse (A)
- Displays:
  - Formatted matrix result
  - Table result
  - Resultant matrix dimensions
- Downloads:
  - Excel (.xlsx) file
  - PDF (.pdf) file
- Reset functionality to clear inputs

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

**requirements.txt**:

```
gradio
numpy
pandas
reportlab
```

---

## ▶️ How to Run

Make sure you're in a virtual environment, then run:

```bash
python matrix_calculator.py
```

Gradio will launch a local server with a web UI in your browser.

---

## 📂 Input Formats

- **Manual Input**:
  - Space-separated numbers
  - Newline for each row  
  - Example:  
    ```
    1 2  
    3 4
    ```

- **File Upload**:
  - Upload `.csv` file (no header)

---

## 📤 Output Formats

- Excel: Download the resulting matrix as `.xlsx`
- PDF: Download a formatted matrix view as `.pdf`

---

## 🛠 Tech Stack

- **Frontend**: Gradio (Python-based UI)
- **Backend**: NumPy & Pandas for matrix logic
- **Export**: ReportLab (PDF), Pandas (Excel)

---

## 📄 License

This project is licensed under the MIT License.
