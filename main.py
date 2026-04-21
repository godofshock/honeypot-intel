import threading
from services.ssh_honeypot import start_ssh_honeypot
from services.http_honeypot import start_http_honeypot
from dashboard.dashboard import show_dashboard

def run():
    t1 = threading.Thread(target=start_ssh_honeypot)
    t2 = threading.Thread(target=start_http_honeypot)

    t1.start()
    t2.start()

    while True:
        cmd = input("Enter 'stats' to view attacks: ")
        if cmd == "stats":
            show_dashboard()

if __name__ == "__main__":
    run()
