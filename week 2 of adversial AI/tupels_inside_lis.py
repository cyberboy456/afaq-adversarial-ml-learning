logs=[
    ("192.156.168","TCP",23),
    ("10.0.0.1","udp",53),
    ("172.16.19.10,","TCP",442)
]
for log in logs:
    ip,protocol,port=log
    print(f"{ip} used {protocol} on port {port}")