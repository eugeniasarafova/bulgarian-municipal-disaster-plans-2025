# Example code for text extraction from municipalplan.pdf as 
# Libraries used for the script and the paper - pdfminer.six and python-docx

from pdfminer.high_level import extract_text
from docx import Document
import os

# Example PDF file
pdf_file = "municipalplan.pdf"
output_txt = "municipalplan_extracted.txt"

# Extracting text from a PDF
try:
    text = extract_text(pdf_file)
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ Text extracted from {pdf_file} and saved to {output_txt}")
except Exception as e:
    print(f"Error extracting text from {pdf_file}: {e}")

# Example DOCX file (if available at the municipality's website)
docx_file = "municipalplan.docx"
if os.path.exists(docx_file):
    try:
        doc = Document(docx_file)
        doc_text = "\n".join([p.text for p in doc.paragraphs])
        with open("municipalplan_docx_extracted.txt", "w", encoding="utf-8") as f:
            f.write(doc_text)
        print(f"Text extracted from {docx_file} and saved.")
    except Exception as e:
        print(f"Error extracting text from {docx_file}: {e}")
