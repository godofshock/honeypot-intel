import socket
from logger.logger import log_event

def start_ssh_honeypot(port=2222):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)

    print(f"[SSH Honeypot] Listening on port {port}")

    while True:
        client, addr = server.accept()
        ip = addr[0]

        client.send(b"SSH-2.0-OpenSSH_7.4\n")
        data = client.recv(1024)

        log_event("SSH", ip, data.decode(errors="ignore"))

        client.close()
