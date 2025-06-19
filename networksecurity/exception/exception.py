import sys
import logging
import os
from datetime import datetime

# ========== Logging Setup ==========
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,  # You can set DEBUG for more detail
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# ===================================

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

        # Log the exception details
        logging.error(self.__str__())

    def __str__(self):
        return "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            self.file_name, self.lineno, str(self.error_message)
        )

if __name__ == '__main__':
    try:
        logging.info("Enter the try block")
        a = 1 / 0
        print("This will not be printed", a)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
