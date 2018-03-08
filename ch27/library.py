import datetime
class LibraryItem:
    def __init__(self, t, a, i):
        self.Title = t
        self.AuthorArtist = a
        self.ItemID = i
        self.OnLoan = False
        self.DueDate = datetime.date.today()

    def GetTitle (self):
        return (self. Title)

    def Borrowing(self):
        self.OnLoan = True
        self.DueDate = self.DueDate + datetime.timedelta(weeks=3)

    def Returning(self):
        self.OnLoan = False

    def PrintDetails(self):
        print(self.Title, '; ',self.AuthorArtist,";",end= "")
        print(self.ItemID, '; ', self.OnLoan, '; ', self.DueDate)

class Book(LibraryItem):
    def __init__(self, t, a, i):
        LibraryItem.__init__(self, t, a, i )
        self.IsRequested = False
        self.RequestedBy = 0

    def GetisRequested(self):
        return (self. IsRequested)

    def SetisRequested(self):
        self.IsRequested = True

    def PrintDetails(self):
        print("Book Deatails")
        LibraryItem.PrintDetails(self)
        print(self.IsRequested)

class CD(LibraryItem):
    def __init__(self, t, a, i): # i n i t i aliser method
        LibraryItem.__init__(self, t, a, i)
        self. Genre= ""

    def GetGenre (self ):
        return (self.Genre)

    def SetGenre (self, g):
        self.Genre= g

    def PrintDetails(self):
        print("CD Deatails")
        LibraryItem.PrintDetails(self)
        print(self.Genre)

a=CD("And justice for all","metallica",1)
b=CD("dark side of moon","pink floyd",2)
c=CD("Black sabbath","Black Sabbath",3)
d=Book("12 Rules for Life","Jordan Peterson",4)
e=Book("white Fang","Jack Londn",5)
d.PrintDetails()


class Borrower():
    def __init__(self, n,a,id):
        self.Name = n
        self.Emailaddress = a
        self.BorrowerID = id
        self.OnLoan = 0

    def GetBorrowerName(self):
        return (self.Name)

    def GetEmailAddress(self):
        return (self.Emailaddress)

    def GetBorrowerID(self):
        return (self.BorrowerID)

    def GetItemsOnLoan(self):
        return (self.OnLoan)

    def UpdateItemsOnLoan(self, n):
        self.OnLoan += n

    def PrintDetails(self):
        print("Borrower : ", self.Name)
        print("ID : ", self.BorrowerID)
        print("email : ", self.Emailaddress)  
        print("Items on loan: ", self.OnLoan)

