# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading

# Batasi hanya pada path /RPC2 saja supaya tidak bisa mengakses path lainnya


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Buat server
with SimpleXMLRPCServer(("192.168.43.63", 8008),
                            requestHandler=RequestHandler, allow_none=True) as server:
        server.register_introspection_functions()

    # with SimpleXMLRPCServer(("192.168.1.16", 6000),
    #                         requestHandler=RequestHandler, allow_none=True) as server:
    #     server.register_introspection_functions()

    # buat data struktur dictionary untuk menampung nama_kandidat dan hasil voting
    # kandidat = {'candidate_1': 0, 'candidate_2': 0}
    kandidat = {'candidate_1': 0,
                'candidate_2': 0
                }
    
    # kode setelah ini adalah critical section, menambahkan vote tidak boleh terjadi race condition
    # siapkan lock
    lock = threading.Lock()
    
    #  buat fungsi bernama vote_candidate()
    def vote_candidate(nama):
        
        # critical section dimulai harus dilock
        lock.acquire()
        # jika kandidat ada dalam dictionary maka tambahkan  nilai votenya
        if kandidat.get(nama) != None:
            kandidat[nama] = kandidat[nama] + 1
            msg = "anda telah memilih " + nama
            lock.release()
            return msg
        else:
            lock.release()
            msg = "Anda memilih kandidat yang tidak terdapat dalam list"
            return msg

        # critical section berakhir, harus diunlock
        lock.release()
        
    
    # register fungsi vote_candidate() sebagai vote
    server.register_function(vote_candidate, 'vote_candidate')



# buat fungsi bernama querry_result
    def querry_result():
        # critical section dimulai
        lock.acquire()
        
        # hitung total vote yang ada
        total = 0
        for i in kandidat:
            total = total + kandidat[i]
        if total == 0:
            lock.release()
            return "nama yang anda pilih tidak terdaftar"

        # hitung hasil persentase masing-masing kandidat
        presentase = []
        msg = ""
        for i in kandidat:
            hasil_vote = (kandidat[i] / total) * 100
            msg = msg + i + "memperoleh " + str(hasil_vote) + "%\n"

        # critical section berakhir
        lock.release()
        return msg
        
    # register querry_result sebagai querry
    server.register_function(querry_result, 'lihat')

    print ("Server voting berjalan...")
    # Jalankan server
    server.serve_forever()
