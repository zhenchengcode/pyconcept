import logging

LOG = logging.getLogger('mylog')
HDLR = logging.FileHandler("model.log")
FORMATTER = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
HDLR.setFormatter(FORMATTER)

LOG.addHandler(HDLR)
LOG.setLevel(logging.INFO)


def write2log():
	LOG.error('in logtest')