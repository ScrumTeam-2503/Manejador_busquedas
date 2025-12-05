from slowapi import Limiter
from slowapi.util import get_remote_address
from fastapi import Request

def get_real_ip(request: Request):
    return request.headers.get("x-forwarded-for", request.client.host)

limiter = Limiter(key_func=get_real_ip)
