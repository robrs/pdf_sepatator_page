from flask import Flask, request, jsonify, send_file
from app.pdf_separator.pdf_separador import PdfSeparator
import importlib

app = Flask(__name__)

@app.route("/")
def run():
    return "<p>Hello, World!</p>"

@app.route("/execute/<cliente>")
def execute_process(cliente):
     modulo = importlib.import_module('app.clientes.'+cliente)
     PdfSeparator.pdf_sep(modulo.pdf_file, modulo.out_dir, modulo.pdf_get_name )
     return 'Dados Gerados'


@app.route('/visualizar-pdf', methods=['GET'])
def visualizar_pdf():
    nome_do_arquivo = request.args.get('arquivo')
    cliente = request.args.get('cliente')
    # Se o nome do arquivo não foi fornecido, retorna uma mensagem de erro
    if not nome_do_arquivo:
        return jsonify({'error': 'O parâmetro "arquivo" é obrigatório.'}), 400

    # Se o nome do arquivo for local, tenta abrir localmente
    path_file = "holerites/"+cliente+"/"+nome_do_arquivo
    try:
        pdf_bytesio = open(path_file, 'rb')
    except FileNotFoundError:
        return jsonify({'error': 'Arquivo não encontrado.'}), 404

    # Retorna o arquivo PDF para o usuário (visualização no navegador)
    return send_file(pdf_bytesio, download_name=f"{nome_do_arquivo}", as_attachment=True)