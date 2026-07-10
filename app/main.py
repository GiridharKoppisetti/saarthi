from time import time

from fastapi import FastAPI, HTTPException, Request
from fastapi.concurrency import asynccontextmanager
from app.config import settings
from app.error import global_exception_handler
from app.logger import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    logger.info("Starting up the application...")
    yield
    # Shutdown code
    logger.info("Shutting down the application...")

app = FastAPI(
    #debug=settings.logging_level == "DEBUG",
    title="My first configuration of fastapi",
    lifespan=lifespan
)
app.add_exception_handler(Exception, global_exception_handler)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time()
    
    # 1. Capture incoming activity details
    client_host = request.client.host if request.client else "unknown"
    logger.info(f"Incoming: {request.method} {request.url.path} | Client: {client_host}")
    
    # Process the request to get the response
    response = await call_next(request)
    
    # 2. Capture outgoing response metrics
    process_time = (time() - start_time) * 1000
    logger.info(
        f"Completed: {request.method} {request.url.path} "
        f"| Status: {response.status_code} | Duration: {process_time:.2f}ms"
    )
    
    return response

@app.get("/")
def read_config():
    logger.info("Reading configuration values.")                      
    return {"app_name": settings.app_name,
            "version": settings.version,
            "Environment": settings.environment,
            "Logging_Level": settings.logging_level}

@app.get("/health")
def health_check():
    logger.info("Performing health check.")
    return {"status": settings.status}

