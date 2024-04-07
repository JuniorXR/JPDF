import json

class DataBase():
	def __init__(self,db_name):
		self.db="db/"+db_name+".db"
		self.db_path=self.db
		self.name=db_name
	
	def writeToDb(self,data:dict):
		with open(self.db,"w") as db:
			json.dump(data,db)
	
	'''
	def writeToDb(self,data:str):
		with open(self.db,"w") as db:
			db.write(data)
	'''
	
	def readFromDb(self):
		with open(self.db,"r") as db:
			return db.read()
	
	def readFromDbAsJsonOBJ(self)->dict:
		with open(self.db,"r") as db:
			return json.load(db)
	def getKeys(self):
		with open(self.db,"r") as db:
			return json.load(db).keys()

	def getValues(self):
		with open(self.db,"r") as db:
			return json.load(db).values()
	
	def readByKey(self,key):
		with open(self.db,"r") as db:
			keyVal=json.load(db)
			return keyVal[key]

	@staticmethod
	def appendWithKey(db_name,key, value):
		with open("db/"+db_name+".db", "r+") as db:
			try:
				data = json.load(db)
			except json.JSONDecodeError:
				data = {}
			data[key] = value
			db.seek(0)
			json.dump(data, db)
	
'''
@classmethod
def appendWithKey_(cls,key, value):
	with open(, "r+") as db:
		try:
			data = json.load(db)
		except json.JSONDecodeError:
			data = {}
		data[key] = value
		db.seek(0)
		json.dump(data, db)
'''