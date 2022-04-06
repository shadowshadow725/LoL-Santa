def getHeader(port, token):
    header = {
        "Host": "127.0.0.1:" + str(port),
        "Connection": "keep-alive",
        "Authorization": "Basic " + str(token),
        "Accept": "application/json",
        "Access-Control-Allow-Credentials": 'true',
        "Access-Control-Allow-Origin": "127.0.0.1",
        "Content-Type": "application/json",
        "Origin": "https://127.0.0.1:" + str(port),
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) RiotClient/34.0.2 (CEF 74) Safari/537.36",
        "Referer": "https://127.0.0.1:" + str(port) + "/index.html",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9"
    }

    return header
