from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
import joblib
import numpy as np
from collections import Counter
import math
import json
import asyncio
import websockets

model = joblib.load("packet_model.pkl")

WS_CLIENTS = set()

def entropy(data):
    if not data:
        return 0
    counter = Counter(data)
    total = len(data)
    ent = -sum(count/total * math.log2(count/total) for count in counter.values())
    return ent

def extract_features(pkt):
    if IP in pkt:
        payload = bytes(pkt[IP].payload)
        ent = entropy(payload)
        size = len(pkt)
        proto = pkt[IP].proto / 255  # normalize
        return np.array([[ent, size/1500, proto]])
    else:
        return None

async def send_to_dashboard(message):
    if WS_CLIENTS:
        await asyncio.wait([client.send(message) for client in WS_CLIENTS])

def process_packet(pkt):
    features = extract_features(pkt)
    if features is not None:
        pred = model.predict(features)[0]
        label = "MALICIOUS" if pred == 1 else "BENIGN"
        info = {
            "src": pkt[IP].src,
            "dst": pkt[IP].dst,
            "size": len(pkt),
            "label": label
        }
        print(info)
        asyncio.run(send_to_dashboard(json.dumps(info)))

def start_sniff():
    sniff(prn=process_packet, store=0)

if __name__ == "__main__":
    start_sniff()
