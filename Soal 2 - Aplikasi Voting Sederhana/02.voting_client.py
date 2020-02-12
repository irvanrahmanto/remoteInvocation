# import xmlrpc bagian client saja
import xmlrpc.client

# buat stub (proxy) untuk client
# s = xmlrpc.client.ServerProxy('http://172.20.10.4:5000')

# buat stub (proxy) untuk client local host
s = xmlrpc.client.ServerProxy('http://127.0.0.1:5000')

# lakukan pemanggilan fungsi vote("nama_kandidat") yang ada di server
print(s.vote_candidate("candidate_1"))
print(s.vote_candidate("candidate_2"))

# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
print(s.lihat())

# lakukan pemanggilan fungsi lain terserah Anda
