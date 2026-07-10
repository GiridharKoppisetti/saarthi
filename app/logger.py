import logging
import sys
from pathlib import Path

LOG_FILE= Path(__file__).parent.parent / ".env.example"

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"    
logging.basicConfig(
    format=LOG_FORMAT,  
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_FILE)
    ]
)

logger = logging.getLogger("SaarthiApp_logger")
