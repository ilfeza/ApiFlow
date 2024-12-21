import logging
import os
from pathlib import Path

log_dir = Path(__file__).parent

LOG_FILE = log_dir / "py_log.log"

logging.basicConfig(
    level=logging.INFO,
    filename=LOG_FILE,
    # filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("application_logger")
