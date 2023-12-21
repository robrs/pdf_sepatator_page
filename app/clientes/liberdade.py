import pdfplumber
from pathlib import Path
import shutil


pdf_file = './uploads/Liberdade.pdf'
out_dir = Path('./holerites/liberdade')

if shutil.os.path.exists(out_dir):
    shutil.rmtree(out_dir)

if not out_dir.exists():
    out_dir.mkdir(parents=True, exist_ok=True)

def pdf_get_name(page, pdf_file):
    pdf_content = pdfplumber.open(pdf_file)
    pdf_page = pdf_content.pages[page]
    pdf_text = pdf_page.extract_text().split('\n')
    name = pdf_text[8]
    name = name.replace(' ','_')
    return name