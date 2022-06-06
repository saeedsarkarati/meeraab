class TAgent:
	def __init__(self):
		# ~ username = ""
		self.id = 0
class TWaterman:
	def __init__(self):
		self.id = 0
		# ~ self.firstname = ""
		# ~ self.lastname = ""
		# ~ self.phonenumber = "09121234567"
		# ~ self.idnumber = "0041234567"
class TWell:		
	def __init__(self):
		self.id = 0
		self.cap = 0
		self.watermanid = 0
class TTransaction:
	def __init__(self):
		self.id = 0
		self.sellerid = 0 #waterman
		self.buyerid = 0 #waterman
Agent = []

