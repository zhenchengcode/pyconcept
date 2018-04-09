import logging
from logging.handlers import RotatingFileHandler

class BaseLogger:
	MB = 1000000
	logger_name_list = set()
	def __init__(self, logger_name, file_name):
		if logger_name in logger_name_list:
			raise AssertionError('use another logger name')
		else:
			logger_name_list.add(logger_name)

		self.log = logging.getLogger(logger_name)
		self.hdlr = RotatingFileHandler(file_name, maxBytes=10*MB, backupCount=10)
		self.formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
		self.hdlr.setFormatter(self.formatter)

		self.log.addHandler(self.hdlr)
		self.log.setLevel(logging.INFO)
		