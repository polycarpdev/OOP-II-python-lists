'''Ordered and mutable/changeable collection
SYNTAX: listname = [item1,item2,item3]
Takes all data types
'''
        #CREATING A LIST

        #1. Directly
shoes = ['fila', 'air force' , 'Airmax' ]
print(shoes)

        #2. using the list() constructor
shoes = list(('fila', 'air force' , 'Airmax' ))
print(shoes)

#CREATING A LIST WITHIN A LIST

datatypes = ['string', ['int', 'float'], 1, 2.1, [True, False]]
print(datatypes)


'''ACCESING LIST ITEMS
Positive indexing starts from 0
negative starts from -1


'''

datatypes = ['string', ['int', 'float'], 1, 2.1, [True, False]]
print(datatypes[0])#prints the forst item
print(datatypes[1:])#prints from the second items to the last 
print(datatypes[3:6])#prints third to sixth since the last oneis not included
print(datatypes[-1])#prints the last item
print(datatypes[:-2])#prints from the start to the second last

#CHECKING IF AN ITEM IS IN A LIST(using membership operator 'in')


datatypes = ['string', ['int', 'float'], 1, 2.1, [True, False]]
if 'string' in datatypes:
     print('The item "string" is in the list')
else:
    print('The item "string" is NOT in the list')

if 'laptop' in datatypes:
     print('The item "Laptop" is in the list')
else:
    print('The item "Laptop" is NOT in the list')



###CHANGING ITEMS IN A LIST
brands = ['coke', 'fanta', 'krest', 'Gilbeys']
brands[1] = 'konyagi' #changes the second item from 'fanta' to 'konyagi'
print(brands)



brands.insert(3,'Guarana')###inserts the item to index3
print(brands)

brands[3] = ['Non-alcoholic']
print(brands)


#ADDING items to alist append()

colors = ['cyan', 'magenta', 'gray', 'purple']
print(colors)

colors.append('TRANSPARENT') ##adds the item at the end of the list
print(colors)

'''
Other methods:
len() - length
extend()
insert()
remove()
del()
pop()
sort() - arranges alphabetically
clear() - deletes everything from the list

'''



colors.pop(4)###deletes item in index 4
print(colors)

colors.sort()##alphabetically arranges items in the list
print(colors)

colors.clear()##deletes all items in the list
print(colors)


###LOOPING THROUGH A LIST - using for loop

colors = ['cyan', 'magenta', 'gray', 'purple']

for x in colors:
    print(x) ###prints all items in the list one by one

for i in range(len(colors)):
    print(colors[i])