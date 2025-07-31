import gradio as gr
import numpy as np
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import tempfile

# Parsing and matrix logic remains the same
def parse_text_matrix(text):
    try:
        lines = text.strip().split("\n")
        matrix = [list(map(float, line.strip().split())) for line in lines]
        return np.array(matrix)
    except:
        raise ValueError("Invalid matrix format. Use space-separated numbers.")

def get_matrix(text, file):
    if file is not None:
        return pd.read_csv(file.name, header=None).values
    elif text.strip():
        return parse_text_matrix(text)
    else:
        raise ValueError("Please provide either a matrix input or upload a file.")

def matrix_operations(text_a, file_a, text_b, file_b, operation):
    try:
        A = get_matrix(text_a, file_a)
        A_shape = f"{A.shape[0]} × {A.shape[1]}"

        B = get_matrix(text_b, file_b) if operation in ["Add", "Subtract", "Multiply"] else None
        B_shape = f"{B.shape[0]} × {B.shape[1]}" if B is not None else "N/A"

        if operation == "Add":
            if A.shape != B.shape:
                return "Addition Error: Matrices must be same shape.", None, None, None, A_shape, B_shape, ""
            result = A + B
        elif operation == "Subtract":
            if A.shape != B.shape:
                return "Subtraction Error: Matrices must be same shape.", None, None, None, A_shape, B_shape, ""
            result = A - B
        elif operation == "Multiply":
            if A.shape[1] != B.shape[0]:
                return "Multiplication Error: A's cols must match B's rows.", None, None, None, A_shape, B_shape, ""
            result = A @ B
        elif operation == "Transpose A":
            result = A.T
        elif operation == "Determinant A":
            if A.shape[0] != A.shape[1]:
                return "Determinant Error: A must be square.", None, None, None, A_shape, "N/A", ""
            result = np.array([[np.linalg.det(A)]])
        elif operation == "Inverse A":
            if A.shape[0] != A.shape[1]:
                return "Inverse Error: A must be square.", None, None, None, A_shape, "N/A", ""
            if np.linalg.det(A) == 0:
                return "Inverse Error: A is singular (non-invertible).", None, None, None, A_shape, "N/A", ""
            result = np.linalg.inv(A)
        else:
            return "Invalid operation selected.", None, None, None, A_shape, B_shape, ""

        rounded = np.round(result, 2)
        text_result = "\n".join(["\t".join([f"{val:.2f}" for val in row]) for row in rounded])
        result_shape = f"{rounded.shape[0]} × {rounded.shape[1]}"

        excel_path = tempfile.NamedTemporaryFile(delete=False, suffix=".xlsx").name
        pd.DataFrame(rounded).to_excel(excel_path, index=False, header=False)

        pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
        c = canvas.Canvas(pdf_path, pagesize=letter)
        y = letter[1] - 40
        for row in rounded:
            line = "  ".join([f"{val:.2f}" for val in row])
            c.drawString(40, y, line)
            y -= 20
        c.save()

        return text_result, pd.DataFrame(rounded), excel_path, pdf_path, A_shape, B_shape, result_shape

    except Exception as e:
        return f"Error: {str(e)}", None, None, None, "", "", ""

def reset_all():
    return "", None, "", None, "Add", "", None, None, None, "", "", ""

# Gradio UI Layout
with gr.Blocks(theme=gr.themes.Base()) as demo:
    gr.Markdown("## 🧲 Matrix Operations Tool")

    with gr.Row(equal_height=True):
        text_a = gr.Textbox(label="Matrix A Manual Input", lines=4, placeholder="1 2\n3 4")
        file_a = gr.File(label="Upload Matrix A (.csv)")
        text_b = gr.Textbox(label="Matrix B Manual Input", lines=4, placeholder="5 6\n7 8")
        file_b = gr.File(label="Upload Matrix B (.csv)")

    with gr.Row(equal_height=True):
        dim_a = gr.Textbox(label="Matrix A Dimensions", interactive=False)
        dim_b = gr.Textbox(label="Matrix B Dimensions", interactive=False)

    with gr.Row(equal_height=True):
        operation = gr.Dropdown(
            ["Add", "Subtract", "Multiply", "Transpose A", "Determinant A", "Inverse A"],
            label="Select Operation",
            value="Add"
        )
        run_btn = gr.Button("Calculate")
        reset_btn = gr.Button("Reset")

    with gr.Row(equal_height=True):
        result_text = gr.Textbox(label="Formatted Result", lines=6)
        result_table = gr.Dataframe(label="Structured Table")

    with gr.Row(equal_height=True):
        result_shape = gr.Textbox(label="Resultant Matrix Dimensions", interactive=False)
        excel_out = gr.File(label="Download Excel")
        pdf_out = gr.File(label="Download PDF")

    run_btn.click(
        matrix_operations,
        inputs=[text_a, file_a, text_b, file_b, operation],
        outputs=[result_text, result_table, excel_out, pdf_out, dim_a, dim_b, result_shape]
    )

    reset_btn.click(
        reset_all,
        outputs=[text_a, file_a, text_b, file_b, operation, result_text, result_table, excel_out, pdf_out, dim_a, dim_b, result_shape]
    )

demo.launch()