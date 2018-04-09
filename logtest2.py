import logtest
import logging

LOG = logging.getLogger('mylog')
HDLR = logging.FileHandler("model.log")
FORMATTER = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
HDLR.setFormatter(FORMATTER)

LOG.addHandler(HDLR)
LOG.setLevel(logging.INFO)


LOG3 = logging.getLogger('mylog')
HDLR = logging.FileHandler("model.log")
FORMATTER = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
HDLR.setFormatter(FORMATTER)

LOG3.addHandler(HDLR)
LOG3.setLevel(logging.INFO)

def write2log2():
	logtest.write2log()
	LOG.error('in logtest2')
	LOG3.error('in logtest2.3')

write2log2()