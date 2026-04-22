import logging
import time
from fastapi import Request

logger = logging.getLogger("movie_platform")

async def log_requests_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(f"{request.method} {request.url.path} | {response.status_code} | {process_time:.4f}s")
    return response