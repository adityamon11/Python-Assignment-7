class Numbers:

	def __init__(self,val1):
		self.value=val1;

	def ChkPrime(self):
		var1 =0;
		for i in range (2,int(self.value)):
			if(self.value%i==0):
				var1 = 1;
		if var1==0:
			print("Prime");
		else:
			print("Not Prime");


	def ChkPerfect(self):
		sum = 0;
		for i in range(1,self.value):
			if(self.value%i==0):
				sum = sum + i;
		if(sum==self.value):
			print("Perfect");
		else:
			print("Not Perfect");

	def SumFactors(self):
		sum = 0;
		for i in range(1,int(self.value)):
			if(self.value%i==0):
				sum = sum + i;
		print("Sum of factors is ",sum)

	def Factors(self):
		for i in range(1,int(self.value)):
			if(self.value%i==0):
				print(i,end=" ");

def main():
	
	y=int(input("Enter a number"));
	n = Numbers(y);
	n.ChkPrime();
	n.ChkPerfect();
	n.SumFactors();
	print("Factors are",end = " ");
	n.Factors();

if __name__ == '__main__':
	main();