import logging
import os
from datetime import datetime

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

# Set the log directory and file path
log_dir = os.path.join(os.getcwd(), "logs")
log_path = os.path.join(log_dir, LOG_FILE)

# Create the logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Set up logging with the correct file path
logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging started")
