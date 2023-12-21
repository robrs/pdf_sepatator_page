#app/pdf_separator/pdf_separator.py

import os
from PyPDF2 import PdfWriter, PdfReader

class PdfSeparator:

    def pdf_sep(pdf_file, out_dir, rename_func):

       with open(pdf_file, 'rb') as pdf:
        pdf_content = PdfReader(pdf_file)
        num_pages = len(pdf_content.pages)

        for page in range(3):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_content.pages[page])

  
            pdf_name = rename_func(page, pdf_file)

            pdf_out = os.path.join(out_dir, pdf_name + '.pdf')

            with open(pdf_out, 'wb') as pdf_named:
                pdf_writer.write(pdf_named)    