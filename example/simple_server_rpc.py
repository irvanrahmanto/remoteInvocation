# gunakan xmlrpc bagian server
# import SimpleXMLRPCServer dan SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# buat kelas requesthandler
# batasi pada path /RPC2 saja


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# buat server serta register fungsi register_introspection_functions()
with SimpleXMLRPCServer(("127.0.0.1", 8008),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # cara 1 untuk memasukkan fungsi dalam server adalah dengan langsung memasukkan namanya
    # fungsi pow() merupakan fungsi build in pada pyhton, tinggal dipanggil saja
    server.register_function(pow)

    # cara 2 untuk register fungsi: buat fungsinya kemudian register
    # a. buat fungsi
    def adder_function(x, y):
        return x + y
    # b. register fungsinya
    server.register_function(adder_function, 'add')

    # cara 3: tidak hanya fungsi, class juga bisa diregisterkan
    class MyFuncs:
        def mul(self, x, y):
            return x * y

    server.register_instance(MyFuncs())

    # jalankan server
    server.serve_forever()
