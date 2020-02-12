# import xmlrpc bagian client
import xmlrpc.client

# buat stub proxy client
proxy = xmlrpc.client.ServerProxy("http://172.20.10.4:5000")

# # buat stub proxy client pada local host
# proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:5000")

# buka file yang akan diupload
with open("file_diupload.txt", 'rb') as handle:
    # baca file dan ubah menjadi biner dengan xmlrpc.client.Binary
    data = xmlrpc.client.Binary(handle.read())

# panggil fungsi untuk upload yang ada di server
proxy.file(data)
