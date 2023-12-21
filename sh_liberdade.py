#!/usr/bin/env python3
from app.pdf_separator.pdf_separador import PdfSeparator
from app.clientes import liberdade as modulo
#import importlib

def execute_process():
        PdfSeparator.pdf_sep(modulo.pdf_file, modulo.out_dir, modulo.pdf_get_name )
        print('Dados Gerados')

execute_process();