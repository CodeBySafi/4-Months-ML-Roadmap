class Book:
    def __init__(self,author,name):
        self.name=name
        self.author=author
        self.__is_available=True

    def Borrow(self):
        if self.__is_available==True:
            print("Book is available")
            self.__is_available=False


        elif self.__is_available==False:
            print("Book is not Available")

    
class person:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show_info(self):
        print("Name is:",self.name)
        print("ID is:",self.id)

class student(person):

    def __init__(self,name,id):
        super().__init__(name,id)
        self.borrowed_Books=[]

    def borrow_Books(self,a):
        self.borrowed_Books.append(a)
        

    def Total_borrowed(self):
        self.show_info()
        for i in self.borrowed_Books:
            
            print("You Borrowed books ",i.name)

class library:
    def __init__(self):
        self.books=[]

    def add_books(self,b):
        self.books.append(b)

    def lend_book(self,b_name,student_object):
        book=False
        for i in self.books:
            
            if b_name==i.name:
                 i.Borrow()
                 book=True
                 student_object.borrow_Books(i)
                 break

        if not book:
                print("Book not available")
        
b1=Book("Safiullah","jhon")
b2=Book("Talha","safi")
s1=student("Abdullah",101)
l1=library()
l1.add_books(b1)
l1.add_books(b2)
l1.lend_book("safi",s1)
s1.show_info()






