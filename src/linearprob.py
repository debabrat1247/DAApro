import math
class linearprob:
	def __init__(self,size=1000):
		self.len=size#length of tables
		self.hashtable=[None for _ in range(self.len)]
		self.population=0#to store number of elements in all tables combined

	def stringHashFunction(self,key):
		key = key.lower()
		p1=37#a prime number
		sum1,sum2,sum3=37,5381,0#assigning initial values to hashvalues
		for i in range(len(key)-1,-1,-1):
			sum1 = (sum1+ord(key[i]))*p1#calculated using Horner's rule
			sum2 = ((sum2 << 5) + sum2) + ord(key[i]) #djb2 algorithm
			sum3 = ord(key[i]) + (sum3 << 6) + (sum3 << 16) - sum3#sdbm algorithm
		sum1=sum1%self.len#using compression maps
		sum2=sum2%self.len
		sum3=sum3%self.len
		return sum1#return a tuple consisting of hashvalues

	def integerHashFunction(self,key): 

		print(key)
		return self.stringHashFunction(str(key))

	def insert(self,data,count=0,i=0):
		
		if(isinstance(data[0],int)):
			hashvalues=self.integerHashFunction(data[0])
			'''the return value of integer 
			hash function is assigned to hashvalues variable'''
		else:
			data[0] = data[0].lower()
			hashvalues=self.stringHashFunction(data[0])
			'''the return value of string
			hash function is assigned to hashvalues variable'''

		if(self.hashtable[hashvalues]==None):
			self.hashtable[hashvalues]=data
			'''if the slot to which key is hashed is empty,then we
			simply insert the data''' 
		else:
			flag=1
			for i in range(hashvalues,self.len):
				if self.hashtable[i]==None:
					self.hashtable[i]=data
					flag=0
					break

			if flag==1:
				for i in range(hashvalues):
					if self.hashtable[i]==None:
						self.hashtable[i]=data
						break

	def lookup(self,key):
		if(isinstance(key,int)):
			hashvalues=self.integerHashFunction(key)
		else:
			key = key.lower()
			hashvalues=self.stringHashFunction(key)

		for i in range(hashvalues,self.len):

			if self.hashtable[i]==None:
				return False
				break

			elif self.hashtable[i][0]==key:
				
				return True
				break

		for i in range(hashvalues):
			if self.hashtable[i]==None:
				return False
				break

			elif self.hashtable[i][0]==key:
				return True
				break

		
		
		


