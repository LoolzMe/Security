import socket
import threading

HOST = "127.0.0.1"
PORT = 10000




def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        def listening(conn):
            data = conn.recv(1024)
            print (data.decode('utf-8'))

        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print("We got ya")
            thread = threading.Thread(target=listening, args=(conn,))
            thread.daemon = True
            thread.start()
            while True:
                try:
                    data = str(input())
                    conn.sendall(data.encode(encoding = 'UTF-8'))
                except:
                    break

            conn.close()

if __name__ == "__main__":
    
    main()