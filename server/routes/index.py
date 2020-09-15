from flask import render_template, send_file
from server import app
from ftplib import FTP
from io import BytesIO


images_ext = ['jpeg', 'jpg', 'png', 'gif']
viedo_ext = ['mp4']

@app.route('/data/<path:path>/<string:endpoint>')
def download(path=None, endpoint=None):
    print( path, endpoint )

    ftp = FTP()
    ftp.encoding='utf-8'
    ftp.connect(host=app.config['FTP_HOST'], port=app.config['FTP_PORT'])
    ftp.login()

    b = BytesIO()
    ftp.retrbinary("RETR " + path + '/' + endpoint, b.write)
    b.seek(0)

    ftp.quit()

    return send_file( b, attachment_filename=endpoint )

@app.route('/', methods=[ 'GET', 'POST' ])
@app.route('/<path:path>', methods=[ 'GET', 'POST' ])
@app.route('/<path:path>/<string:endpoint>', methods=[ 'GET', 'POST' ])
def index(path=None, endpoint=None):
    if path is not None:
        path += '/'
    else:
        path = ''

    if endpoint is not None:
        path += endpoint + '/'

    ftp = FTP()
    ftp.encoding='utf-8'
    ftp.connect(host=app.config['FTP_HOST'], port=app.config['FTP_PORT'])
    ftp.login()
    
    files = list()
    file_list = ftp.nlst( path )
    for filename in file_list:
        ext = filename.split('.')[-1]
        _type = 'normal'
        
        if ext in ( images_ext ):
            _type = 'image'
        elif ext in ( viedo_ext ):
            _type = 'video'

        files.append({ "name":filename, "type":_type })

    ftp.quit()
    return render_template('index.html', files=files, path=path)