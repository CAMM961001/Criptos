import bitso
import datetime as dt

class BitsoApi():
	"""A class to manage bitso API single connection and queries"""


	def __init__(self):
		"""Initialize the API's settings for MX City"""
		#Set time delta for Mexico City UTC-6.
		self.time_delta = dt.timedelta(hours=6)

		#Desired criptocoins tickers and bitso api object.
		self.ticker_list = ['btc_usd', 'eth_usd', 'mana_usd']
		self.api = bitso.Api()


	def single_query(self, ticker):
		"""Make query for single ticker"""
		self.ticker = ticker
		self.query = self.api.ticker(self.ticker)
		return self.query


	def full_record(self):
		"""Make query for all desired criptos and return
		   record in specified format"""
		self.record = []

		#Loop for tickers in ticker_list.
		for ticker in self.ticker_list:
			query = self.single_query(ticker)

			#Timestamp condition.
			if ticker == self.ticker_list[0]:
				#Timestamp adjusted for Mexico City.
				timestamp = query.created_at - self.time_delta
				#Formating timestamp
				timestamp = timestamp.strftime('%Y-%m-%d %H:%M')
				#Appending timestamp as record's 1st element.
				self.record.append(timestamp)

			self.record.append(str(query.last))

		#Convert data record list to string.
		self.record_str = ','.join(self.record)

		return self.record_str