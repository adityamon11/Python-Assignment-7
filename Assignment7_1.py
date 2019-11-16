class BookStore:

	NoOfBooks = 0;

	def __init__(self,bookName,bookAuthor):
		BookStore.NoOfBooks += 1;
		self.name = bookName;
		self.author = bookAuthor;

	def Display(self):
		print(self.name,"by",self.author,".","No. of books:",self.NoOfBooks );

def main():
	Obj1 = BookStore("Linux System Programming", "Robert Love");
	Obj1.Display();
	Obj2 = BookStore("C Programming", "Dennis Ritchie");
	Obj2.Display();
	Obj3 = BookStore("Java Concurrency", "Brian Goetz");
	Obj3.Display();
	Obj4 = BookStore("Effective Python", "Brett Slatkin");
	Obj4.Display();

if __name__ == '__main__':
	main();