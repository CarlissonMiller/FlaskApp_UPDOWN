import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory, jsonify
from process_file import process_file

app = Flask(__name__)
UPLOAD_FOLDER = '.\input'
DOWNLOAD_FOLDER = '.\output'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["DOWNLOAD_FOLDER"] = DOWNLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        
        # verifique se a solicitacao de postagem tem a parte do arquivo
        if 'file' not in request.files:
            flash('Nao tem a parte do arquivo')
            return redirect(request.url)
        file = request.files['file']
        
        # Se o usuario nao selecionar um arquivo, o navegador envia um
        # arquivo vazio sem um nome de arquivo.
        
        if file.filename == '':
            flash('Nenhum arquivo selecionado')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # new_filename = f'{filename.split(".")[0]}_processed.csv'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            print(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print(filename)
            # return send_from_directory(DOWNLOAD_FOLDER, "product_data.csv")
            return redirect(url_for('download'))
    return render_template('upload.html')
    

@app.route('/download')
def download():
    return render_template('download.html', files=os.listdir('output'))
    
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config["DOWNLOAD_FOLDER"], filename)

if __name__ == '__main__':
    app.run(debug = True)