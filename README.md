# Distributed Honeypot & Attack Intelligence System

A multi-service honeypot system designed to simulate vulnerable services, capture attacker interactions, and generate actionable threat intelligence.

## Features

* SSH and HTTP honeypot services
* Real-time logging of attacker interactions
* Centralized logging system
* Attack pattern analysis and summary dashboard
* Multi-threaded service execution

## Architecture

* services/ → simulated vulnerable services
* logger/ → centralized logging
* analyzer/ → attack pattern analysis
* dashboard/ → CLI-based reporting

## Use Case

This system helps in understanding real-world attack behavior by capturing and analyzing malicious interactions across different services.


## Tech Stack

* Python
* Socket Programming
* HTTP Server
* Multi-threading

## Run

```bash
python main.py
```

## Future Improvements

* GeoIP attack mapping
* Machine learning-based attack classification
* Web dashboard
* Additional services (FTP, Telnet)
