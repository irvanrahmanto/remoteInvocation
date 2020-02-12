# gunakan xmlrpc bagian server
from xmlrpc.server import SimpleXMLRPCServer
# import xmlrpc.client

# buat fungsi bernama file_upload()


def file_upload(filedata):

    # buka file
    with open("hasil_upload.txt", 'wb') as handle:
        # convert from byte to binary IMPORTANT!
        data1 = filedata.data

        # tulis file tersebut
        handle.write(data1)
        return True  # IMPORTANT

# must have return value
# else error messsage: "cannot marshal None unless allow_none is enabled"


# buat server
server = SimpleXMLRPCServer(('127.0.0.1', 5003))

# buat server serta register fungsi register_introspection_functions()
# with SimpleXMLRPCServer(("127.0.0.1", 5003), requestHandler=RequestHandler) as server:
#     server.register_introspection_functions()

# tulis pesan server telah berjalan
print("Listening on port 5003")

# register fungsi
server.register_function(file_upload, 'file')

# jalankan server
server.serve_forever()
