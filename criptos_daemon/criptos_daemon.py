from criptos_api import BitsoApi

from apscheduler.schedulers.blocking import BlockingScheduler

class CriptosDaemon:
	"""Overall class for criptocoin query daemon"""


	def __init__(self):
		"""Initialize daemon and create resources"""
		self.api = BitsoApi()

		# File to store data.
		self.real_time_data = 'data/real_time_data.txt'


	def export_record(self):
		"""Export single record to specified text file."""
		with open(self.real_time_data, 'a') as file_object:
			file_object.write(f"\n{self.api.full_record()}")
			#Close text file.
			file_object.close()


	def start_daemon(self):
		"""Start daemon for eternal data acquisition."""
		scheduler = BlockingScheduler()
		scheduler.add_job(self.export_record, 'interval', minutes=10)
		scheduler.start()


if __name__ == '__main__':
	# Iniciar el programa cuando se ejecute desde terminal.
	cc_daemon = CriptosDaemon()
	cc_daemon.start_daemon()