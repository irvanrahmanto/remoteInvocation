# import library xmlrpc client karena akan digunakan rpc
import xmlrpc.client

# buat stub/skeleton (proxy) pada client
s = xmlrpc.client.ServerProxy('http://127.0.0.1:8008')

# panggil fungsi pow() yang ada di komputer remote
print(s.pow(2, 3))  # Returns 2**3 = 8

# panggil fungsi add() yang ada di komputer remote
print(s.add(2, 3))  # Returns 5

# panggil fungsi mul() yang ada di komputer remote
print(s.mul(5, 3))  # Returns 5*2 = 10

# print semua fungsi yang ada di komputer remote (optional)
print(s.system.listMethods())
