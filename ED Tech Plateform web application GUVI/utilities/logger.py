import logging

class LogGenerator:

    @staticmethod
    def loggen():
        logging.basicConfig(
            filename='reports/test_execution.log',
            format='%(asctime)s : %(levelname)s : %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO
        )

        logger = logging.getLogger()
        return logger