import datetime

LOG_FILE = "logs/attacks.log"

def log_event(service, source_ip, data):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} | {service} | {source_ip} | {data}\n")
