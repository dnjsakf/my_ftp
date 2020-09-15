BASE_URL = 'http://localhost:4000'
DEBUG = True
CORS = {
    r'*': { 'origin': '*' }
}

FTP_HOST = 'localhost'
FTP_PORT = 9021
FTP_BASE_URL = 'ftp://{}:{}'.format( FTP_HOST, FTP_PORT )