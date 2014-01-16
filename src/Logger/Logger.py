import os
import sys
import time

class Logger(object):
	'''
	Logger class to maintain utilities for logging.
	Supports logging to files and to stdout/stderr.

	Keyword Arguments:
		output_file: Path the file to write output to.
					 If no path is given, no output will
					 be written. (default = None)
		console:     Print to console. (default = False)
		timer:       Add time since the start to the logs.
					 (default=False)
		clock:       Add absolute times to the logs.
					 If clock = True, time is printed as
					 '%H:%M:%S' using time.strftime. Clock
					 can be set to any other string. For 
					 formating see http://docs.python.org/2/library/time.html#time.strftime
					 (default=False)
		prefix:      Character string to prepend to every
					 line. (default="#")
	'''
	def __init__(self,output_file=None,console=False,timer=False,clock=False,prefix="#"):
		self.console = console
		if output_file:
			self.output_file = file(os.path.abspath(output_file),'w')
		else:
			self.output_file = None
		self.console=console
		if clock:
			if type(clock) is bool:
				s = '%H:%M:%S'
			else:
				s = clock
			self.clock = clock.strftime(s)
		else:
			self.clock=False
		if timer:
			self.timer = int(time.time())

	def __get_time_str(self):
		diff = int(time.time) - self.timer

	def log(self,message):
		self.log_stdout(message)
	
	def log_stdout(self,message):
		msg = ""
		if self.timer:
			msg += self.__get_time_str()

