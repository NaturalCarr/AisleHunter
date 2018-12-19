import random
import AisleClass

#Creates a list with the format ITEM, StoreID, Aisle_Number, Shelf_Number, PIA, Comment
#input = empty list
#output = a random string for item, a random numder for store ID, Aisle_Number, PIA, Comment
'''
print("Hello")
def Position(asile, EmptyList= []):
    print("I work")

    #parses data from food.txt into a variable
    with open ("food.txt") as f:
        ReadFoodData = f.readlines()
        content = [x.strip() for x in ReadFoodData]

    #parses data from insert.sql

    Store1 =AisleClass.Store("Isayah", 11225, 4, 6)



with open ("food.txt") as f:
        ReadFoodData = f.readlines()
        content = [x.strip() for x in ReadFoodData]
'''

AllStores = []
Store1 =AisleClass.Store("Isayah", 11225, 4, 6)
AllStores.append(Store1)
'''Store2 =AisleClass.Store("Ibayah", 11225, 4, 6)
Store3 =AisleClass.Store("Idayah", 11225, 3, 7)
Store4 =AisleClass.Store("Ilayah", 11225, 8, 5)
Store5 =AisleClass.Store("Ikayah", 11225, 3, 6)'''


OneDLsit = range(5)
'''
for d in OneDLsit:
        AllStores.append(
        print(Store1)

#def NumofStores(num):
'''
def RandomZip():
        listsize = range(0,5)
        Zip = []
        for i in listsize:
                randi=random.randint(1,9)
                Zip.append(randi)
        return Zip

def RandomDump(StoreName):
        rand =random.randint(1,9)
        rand2 = random.randint(1,9)
        Object = AisleClass.Store(StoreName, RandomZip(), rand, rand2)
        AllStores.append(Object)


x = RandomZip()
RandomDump("Zack")
RandomDump ("Johnies Store of food")
RandomDump("Salee Sale")
RandomDump("James Food")
#print(x)
#print(AllStores[1].Name)

loop = range(len(AllStores))
finallist = []
for l in loop:
        finallist.append(AisleClass.Store.INSERT(AllStores[l],l))

#print(finallist[range(len(finallist)),])
        




    



