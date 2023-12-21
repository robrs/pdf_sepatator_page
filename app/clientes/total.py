#app/clentes/total.py
import pdfplumber
from pathlib import Path
import shutil


pdf_file = Path('./uploads/Total.pdf')
out_dir = Path('./holerites/total')

if shutil.os.path.exists(out_dir):
 shutil.rmtree(out_dir)

if not out_dir.exists():
 out_dir.mkdir(parents=True, exist_ok=True)

def pdf_get_name(page, pdf_file):

 pdf_content = pdfplumber.open(pdf_file)
 pdf_page = pdf_content.pages[page]
 pdf_text = pdf_page.extract_text().split('\n')


 name = pdf_text[2]
 name1 = list(filter(lambda c: c in '0123456789(', name))
 name2 = list(filter(lambda c: c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ', name))

 name1 = ''.join(name1).strip()
 name_arr_1 = name1.split('(')

 name2 = ''.join(name2).strip()
 name2 = name2.replace(' ', '_')
 
 name1 = name_arr_1[0]

 return name1+"_"+name2