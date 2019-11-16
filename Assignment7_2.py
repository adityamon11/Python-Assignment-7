class BankAccount:
	ROI = 4.5
	Years = 4
	def __init__(self,val1,val2):
		self.name=val1;
		self.amount=val2;

	def Display(self):
		print("Name is: ",self.name,", Amount is ",self.amount)

	def Deposit(self,val):
		self.amount+=val;

	def Withdraw(self,val):
		self.amount-=val;

	def CalculateInterest(self):
		amt = self.amount * BankAccount.ROI * BankAccount.Years;
		return amt;

def main():
	
	x=input("Enter a name ");
	y=int(input("Enter initial amount "));
	b = BankAccount(x,y);
	z1=int(input("Enter a amount to deposit "));
	b.Deposit(z1);
	b.Display();
	z2 = int(input("Enter a amount to withdraw "));
	b.Withdraw(z2);
	b.Display();
	p = b.CalculateInterest();
	print("Interest will be ",p);

if __name__ == '__main__':
	main();