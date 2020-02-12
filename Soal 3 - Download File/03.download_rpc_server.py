# import library SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import xmlrpc bagian client
import xmlrpc.client

# buatlah fungsi bernama download()


def file_download():

    # buka file bernama "file_didownload.txt"
    with open("file_didownload.txt", 'rb') as handle:
        # kirimkan file tersebut dalam bentuk xml dengan cara memanggil xmlrpc.client.Binary()
        return xmlrpc.client.Binary(handle.read())


# buat server pada IP dan port yang telah ditentukan
server = SimpleXMLRPCServer(('127.0.0.1', 5003))
# server = SimpleXMLRPCServer(('192.168.43.34', 6000))

# print bahwa "server mendengarkan pada port xxx"
print("Listening on port 8001")

# register fungsi download pada server
server.register_function(file_download, 'file_download')

# jalankan server
server.serve_forever()
