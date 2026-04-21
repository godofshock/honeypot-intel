from collections import defaultdict

def analyze_logs():
    counts = defaultdict(int)

    with open("logs/attacks.log", "r") as f:
        for line in f:
            parts = line.split("|")
            if len(parts) > 2:
                ip = parts[2].strip()
                counts[ip] += 1

    print("\n=== Attack Summary ===")
    for ip, count in counts.items():
        print(f"{ip} -> {count} attempts")
