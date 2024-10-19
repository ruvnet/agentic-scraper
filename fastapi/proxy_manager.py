proxy_address = None

def set_proxy(address: str):
    global proxy_address
    proxy_address = address

def get_proxy():
    return proxy_address
