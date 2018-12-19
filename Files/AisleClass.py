import random

class Store:
    """ Creates a store object
    """
    
    StoreID = 0
    def __init__(self, Name, ZipCode, x, y, Position =None, Content= None, RL=None ):
        #print("hello")
        self.Name = Name 
        self.ZipCode = ZipCode
        self.x = range(1,x) ##x cord in matrix Asile
        self.y = range(1,y) #y cord in matrix Postion
        self.Position = Position
        self.Content = Content
        self.RL = RL
        Store.StoreID +=1
        #print("Hello")
        RL = []
        
        if self.Position is None:
            self.Position = x,y

        if self.RL is None:
            self.RL = []

        if self.Content is None:
            with open ("food.txt") as f:
                ReadFoodData = f.readlines()
                self.Content = [x.strip() for x in ReadFoodData]
        


        for i in self.x:
            self.RL.append([])
            print (RL)
            print(i)
            for j in self.y:
                print(j)
                Store.r = random.randint(0,len(self.Content))
                if self.Content[Store.r-1] == "":
                    print("This is Store.r:", Store.r)
                    Store.r = random.randint(0,len(self.Content))
                    
                try:
                    self.RL[i-1].append(self.Content[Store.r])
                except IndexError:
                    print(self.RL)
                    print(i, Store.r)
                    self.RL[i-2].append(self.Content[Store.r-1])

                
                print(self.RL)

    #def NextTO(self, x,y):
    def Asile(self):
        return len(self.y)+1  

    def AsilePosition(self):
        return len(self.x)+1 

    def Coordinates(self):
        xy = len(self.x)+1, len(self.y)+1
        print(xy)
        return xy

    #def NextTo

    def PrintAll(self):
        for i in self.x:
            for j in self.y:
                print(j,i, " ",self.RL[i-1][j-1])
    #('Rice', '1', '3', '6','Middle','It''s Below The Dishwashing Liquid');
    def INSERT(self, storenum):
        #print(self.Name)
        listi = list()
        for i in self.x:
            for j in self.y:
                #print("'",self.RL[i-1][j-1],"'", "'",storenum, "'", "'",i,"'","'", j, "In the Middle", "Next to thingy")
                try:
                    x = "INSERT INTO POSITION (ITEM, StoreID, Aisle_Number, Shelf_Number, PIA, Comment) Values ('{}','{}', '{}', '{}', '{}','{}')".format(self.RL[i-1][j-1],storenum,i,j,"In the Middle", "Next to thingy")
                    #print("INSERT INTO POSITION (ITEM, StoreID, Aisle_Number, Shelf_Number, PIA, Comment) Values ('{}','{}', '{}', '{}', '{}','{}')".format(self.RL[i-1][j-1],storenum,i,j,"In the Middle", "Next to thingy"))
                    listi.append(x)
                except IndexError:
                    try:
                        print(i,j)
                        #print("INSERT INTO POSITION (ITEM, StoreID, Aisle_Number, Shelf_Number, PIA, Comment) Values ('{}','{}', '{}', '{}', '{}','{}')".format(self.RL[0][0],storenum,i,j,"In the Middle", "Next to thingy"))
                        x= "INSERT INTO POSITION (ITEM, StoreID, Aisle_Number, Shelf_Number, PIA, Comment) Values ('{}','{}', '{}', '{}', '{}','{}')".format(self.RL[0][0],storenum,i,j,"In the Middle", "Next to thingy")
                        listi.append(x)
                    finally:
                        print("error:\n", i,j)
        return listi

                



        
        


    
'''
Store1 =Store("Isayah", 11225, 4, 6)
Store2 =Store("ZayWorld", 6606, 6, 7)
StoresID = []
StoresID.append(Store1)
StoresID.append(Store2)
print(Store1.Asile())
print(Store1.AsilePosition())
Store1.Coordinates()
Store1.PrintAll()
#Store1.INSERT(1)
#Store2.INSERT(2)
#Store1.PrintAisle()
print(StoresID[:])




    

Store1 =Store("Isayah", 11225, 4, 6)
Store2 =Store("Isayer", 11213, 3, 4)
x =Store1
y =Store2
x.PrintAisle()
y.PrintAisle()
print(x.StoreID)
#print(y.StoreID)
'''