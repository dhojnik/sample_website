#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgitb
import socket

cgitb.enable()  # Show debugging info

print("Content-Type: text/html;charset=utf-8\n")

# Get the container's own IP address
container_ip = socket.gethostbyname(socket.gethostname())

print(f"""
<html>
<head>
    <title>Python CGI Example</title>
</head>
<body>
    <h1>Hello from Python CGI!</h1>

    <p>Container IP address: <strong>{container_ip}</strong></p>

    <p>This page is served from inside a Python CGI script.</p>

</body>
</html>
""")

