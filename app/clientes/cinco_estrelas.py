import pdfplumber
from pathlib import Path
import shutil

pdf_file = './uploads/5SS.pdf'
out_dir = Path('./holerites/5ss')

if shutil.os.path.exists(out_dir):
    shutil.rmtree(out_dir)

if not out_dir.exists():
    out_dir.mkdir(parents=True, exist_ok=True)

def pdf_get_name(page, pdf_file):
    pdf_content = pdfplumber.open(pdf_file)
    pdf_page = pdf_content.pages[page]
    pdf_text = pdf_page.extract_text().split('\n')
    name = pdf_text[4]
    name_arr = list(filter(lambda c: c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ', name))
    chapa_arr = list(filter(lambda c: c in '0123456789(', name))
    name = ''.join(name_arr).strip()
    chapa = ''.join(chapa_arr).strip();
    return chapa+'_'+name.replace(' ','_')