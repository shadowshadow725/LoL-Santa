import requests
import os
import subprocess
import re
import base64


def getRiotClientEndpoint():
    command = 'wmic PROCESS WHERE name="' + "'RiotClientUx.exe'" + '" GET commandline;'
    args = str(subprocess.run(["powershell", "-Command", command], capture_output=True))
    port = re.findall(r"--app-port=\d\d\d\d\d", args)
    if len(port) > 1:
        exit(1)
    port = port[0].replace("--app-port=", "")

    auth_token = re.findall(r"--remoting-auth-token=[\w-]*", args)
    if len(auth_token) > 1:
        exit(1)
    auth_token = auth_token[0].replace("--remoting-auth-token=", "")
    # print(port, auth_token)

    message = "riot:" + auth_token
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes).decode('ascii')

    # print(port, base64_bytes)
    return port, base64_bytes


def getEndpoint():
    command = 'wmic PROCESS WHERE name="' + "'LeagueClientUx.exe'" + '" GET commandline;'
    args = str(subprocess.run(["powershell", "-Command", command], capture_output=True))
    port = re.findall(r"--app-port=\d\d\d\d\d", args)
    if len(port) > 1:
        exit(1)
    port = port[0].replace("--app-port=", "")
    pid = re.findall(r"--app-pid=[\w-]*", args)
    if len(pid) > 1:
        exit(1)
    pid = pid[0].replace("--app-pid=", "")
    auth_token = re.findall(r"--remoting-auth-token=[\w-]*", args)
    if len(auth_token) > 1:
        exit(1)
    auth_token = auth_token[0].replace("--remoting-auth-token=", "")
    # print(port, auth_token)

    message = "riot:" + auth_token
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes).decode('ascii')

    # print(port, base64_bytes)
    return port, base64_bytes, pid



