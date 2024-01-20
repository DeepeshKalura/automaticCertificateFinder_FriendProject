import logging

# level: DEBUG, INFO, WARNING, ERROR, CRITICAL

log = logging.basicConfig(level=logging.DEBUG, filename='log/appFlow.log', filemode='w', format='%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def debugLog(message):
    logging.debug(message)

def infoLog(message):
    logging.info(message)

def warningLog(message):
    logging.warning(message)

def errorLog(message):
    logging.exception(message)

def criticalLog(message):
    logging.critical(message)
