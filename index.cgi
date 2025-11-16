#!/usr/bin/env python3
import socket
import cgitb
cgitb.enable()

def header():
    print("Content-Type: text/html; charset=utf-8")
    print()

def get_container_ip():
    """
    Returns the container’s own IP address by checking the
    default route using a dummy UDP connection.
    Works in Podman, Docker, LXC, Kubernetes.
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "unknown"

header()

ip = get_container_ip()

print(f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Container IP</title></head>
<body style="font-family: sans-serif">
<h1>IP Address of This Container</h1>
<p><b>{ip}</b></p>
</body>
</html>""")

