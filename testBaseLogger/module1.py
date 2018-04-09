import sys
sys.path.append("../log_service")
import baseLogger
from baseLogger import BaseLogger
import module2
	
logger1 = BaseLogger('logger1', 'logfile.log').log

logger1.info('log from module1')
def callModule2():
	module2.callLog()

callModule2()
# call module1 module2 separately won't cause any trouble, 
# trouble comes when you call one script from another, as 
# both loggers are alive