import logging

class Log:

    @staticmethod
    def Loggie():
        logging.basicConfig(filename=r".\\env\\Logs\\Auto.log",
        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.ERROR)
        return logger



