import random

class Store:
    """ Creates a store object
    """
    
    StoreID = 0

    def __doc__(self):
        """ The Purpose of this class is to input the information and formatr it based on the 
        InsertTemplate.txt file. Store takes the arguments and puts it all into a 2D array.
        The x value corresponds to the number of the Aisle. The y value corresponds to the 
        position in the nth asile. This is put together and store into the list object RL
        """
    def __init__(self, Name, ZipCode, x, y, Position =None, Content= None, RL=None ):
        self.Name = Name 
        self.ZipCode = ZipCode
        self.x = range(1,x) ##x cord in matrix Aisle
        self.y = range(1,y) #y cord in matrix Postion
        self.Position = Position #x,y
        self.Content = Content
        self.RL = RL 
        Store.StoreID +=1
        RL = []
        
        #creates a tuple object that holds the value for x,y
        if self.Position is None:
            self.Position = x,y

        if self.RL is None:
            self.RL = []

        #turns the data from food.txt into a list of string objects
        if self.Content is None:
            with open ("food.txt") as f:
                ReadFoodData = f.readlines()
                self.Content = [x.strip() for x in ReadFoodData]
        
        for i in self.x:
            self.RL.append([])

            for j in self.y:
                print(j)
                Store.r = random.randint(0,len(self.Content))
                if self.Content[Store.r-1] == "":
                    Store.r = random.randint(0,len(self.Content))                    
                try:
                    self.RL[i-1].append(self.Content[Store.r])
                except IndexError:
                    self.RL[i-2].append(self.Content[Store.r-1])

    def Asile(self):
        return len(self.y)+1  

    def AsilePosition(self):
        return len(self.x)+1 

    def Coordinates(self):
        xy = len(self.x)+1, len(self.y)+1
        print(xy)
        return xy

    def PrintAll(self):
        for i in self.x:
            for j in self.y:
                print(j,i, " ",self.RL[i-1][j-1])

    def INSERT(self, storenum):
        listi = list()
        for i in self.x:
            for j in self.y:
                try:
                    x = "INSERT INTO POSITION (ITEM, StoreID, Aisle_Number, Shelf_Number, PIA, Comment) Values ('{}','{}', '{}', '{}', '{}','{}')".format(self.RL[i-1][j-1],storenum,i,j,"In the Middle", "Next to thingy")                  
                    listi.append(x)
                except IndexError:
                    try:
                        x= "INSERT INTO POSITION (ITEM, StoreID, Aisle_Number, Shelf_Number, PIA, Comment) Values ('{}','{}', '{}', '{}', '{}','{}')".format(self.RL[0][0],storenum,i,j,"In the Middle", "Next to thingy")
                        listi.append(x)
                    finally:
                        print("error:\n", i,j)
        return listi