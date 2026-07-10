import traceback
from fastapi import Request
from fastapi.responses import JSONResponse
from app.logger import logger

async def global_exception_handler(request: Request, exc: Exception):
    # 1. Capture and format the complete error traceback
    error_trace = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
    
    # 2. Log the critical error payload internally
    logger.error(
        f"Unhandled Exception: {request.method} {request.url.path}\n"
        f"Error Details: {str(exc)}\n"
        f"Traceback:\n{error_trace}"
    )
    
    # 3. Return a clean, safe response to the public client
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred. Please try again later."}
    )
