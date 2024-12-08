RATE_LIMITER_TEMPLATE = """from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from time import time
from collections import defaultdict
import os
from dotenv import load_dotenv

load_dotenv()

MAX_REQUESTS = int(os.getenv("RATE_LIMIT_MAX_REQUESTS", 5))
PERIOD = int(os.getenv("RATE_LIMIT_PERIOD", 60))


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.max_requests = MAX_REQUESTS
        self.period = PERIOD
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time()

        self.requests[client_ip] = [
            timestamp for timestamp in self.requests[client_ip]
            if timestamp > current_time - self.period
        ]

        if len(self.requests[client_ip]) >= self.max_requests:
            return JSONResponse(status_code=429, content={"detail": "Too Many Requests"})

        self.requests[client_ip].append(current_time)
        response = await call_next(request)
        return response
"""
