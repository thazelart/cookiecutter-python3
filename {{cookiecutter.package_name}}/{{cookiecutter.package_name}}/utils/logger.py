from datetime import datetime
import logging
import os


class Logger:
    writer = logger = logging.getLogger("{{cookiecutter.package_name}}")

    def __init__(self, log_dir: set = "/tmp/", log_level: str = logging.INFO):
        self.writer = self.setupLogger(log_dir, log_level)

    def setupLogger(self, log_dir: str, log_level: int):
        """Setup the logger.
    
        :Arguments:
          log_dir : str
            The directory where the logfile will be put
          log_level : int
            The level of the logger
    
        :Return:
          logger : logging.logger
            The logger that was setup by the function
        """
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        log_file = os.path.join(log_dir, "{{cookiecutter.package_name}}-" + now + ".log")

        # Ensure we can write in log_file
        try:
            formatter = logging.Formatter("%(asctime)s -- %(levelname)s -- %(message)s")

            handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
            handler.setFormatter(formatter)
            handler.setLevel(log_level)

            logger = logging.getLogger("{{cookiecutter.package_name}}")
            logger.setLevel(log_level)
            logger.addHandler(handler)

            return logger
        except Exception as e:
            print(e)
            exit(1)
