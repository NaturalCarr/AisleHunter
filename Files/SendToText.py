import random
import AisleClass

#Creates a list with the format ITEM, StoreID, Aisle_Number, Shelf_Number, PIA, Comment
#input = empty list
#output = a random string for item, a random numder for store ID, Aisle_Number, PIA, Comment


AllStores = []
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


loop = range(len(AllStores))
finallist = []
for l in loop:
        finallist.append(AisleClass.Store.INSERT(AllStores[l],l))


    



