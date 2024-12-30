import fitz  # PyMuPDF
from pymupdf4llm import pdf_to_markdown

pdf_document = "your_pdf_file.pdf"
markdown_text = pdf_to_markdown(pdf_document)

with open("output.md", "w") as f:
    f.write(markdown_text)
