import sys
sys.path.append("../log_service")
import baseLogger
from baseLogger import BaseLogger
	
def callLog():
	logger1 = BaseLogger('logger2', 'logfile.log').log
	logger1.info('log from module2')