# import xmlrpc bagian client saja
import xmlrpc.client

# buat stub (proxy) untuk client
s = xmlrpc.client.ServerProxy('http://192.168.43.63:8008')

# lakukan pemanggilan fungsi vote("nama_kandidat") yang ada di server
print(s.vote_candicate("candidate_1"))
print(s.vote_candidate("candidate_3"))

# lakukan pemanggilan fungsi querry() untuk mengetahui hasil persentase dari masing-masing kandidat
print(s.lihat())

# lakukan pemanggilan fungsi lain terserah Anda
