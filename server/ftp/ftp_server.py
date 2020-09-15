import os
 
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

FTP_HOST = '0.0.0.0'
FTP_PORT = 9021
#FTP_DIRECTORY = os.path.join(os.getcwd(), 'D:/project/python/')
FTP_DIRECTORY = 'D:/project/python/communities/crawl_community/files'
#FTP_DIRECTORY = os.getcwd()
 
def main():
    authorizer = DummyAuthorizer()
    
    authorizer.add_anonymous(FTP_DIRECTORY)
 
    handler = FTPHandler
    handler.banner = "Dochi's FTP Server."
 
    handler.authorizer = authorizer
    handler.passive_ports = range(60000, 65535)
    
    address = (FTP_HOST, FTP_PORT)
    server = FTPServer(address, handler)
    
    server.max_cons = 256
    server.max_cons_per_ip = 50
 
    server.serve_forever()

if __name__ == '__main__':
    main()
