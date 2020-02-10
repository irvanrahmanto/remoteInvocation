# import library socket karena akan digunakan request reply protocol sederhana
import socket

# definisikan IP dan port dari webserver yang akan kita gunakan. Port HTTP adalah 80
IP = '127.0.0.1'
PORT = 5004

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# lakukan binding
s.bind((IP, PORT))

# buffersize
BUFFER_SIZE = 1024

# socket mendengarkan
s.listen(1)

# tampilkan dengan print () "Server berjalan dan melayani HTTP pada port xx"
print("Server berjalan dan melayani HTTP pada port : ", PORT)

# loop forever
while True:
    # socket menerima koneksi
    conn, addr = s.accept()
    # socket menerima data
    request = conn.recv(BUFFER_SIZE)
    # print data hasil koneksi
    print("Data diterima :", str(data))
    # buat response sesuai spesifikasi HTTP untuk diberikan kepada client
    http_response = """\HTTP/1.1 200 OK

<html>
<head>
<title>Web Server Sederhana</title>
</head>
<body>

<h1>Heading 1</h1>
<p>Ini adalah contoh paragraf.</p>
<img src="https://www.surfertoday.com/images/stories/surfetiquette.jpg">

</body>
</html>
"""
    # kirim response kepada client dengan sendall() jangan lupa diencode response dengan utf-8
    conn.sendall(http_response.encode())
    # tutup koneksi
s.close()

# Selamat! Kamu telah berhasil membuat web server sederhana.
