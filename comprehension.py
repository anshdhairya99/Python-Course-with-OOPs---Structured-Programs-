# Comprehensions In Python:---------------------

#ls = []
#for i in range(100):
#    if i%3==0:
#        ls.append(i)

#print(ls)

#ls = [i for i in range(100) if i%3==0]

#print(ls)

#dict1 = {i:f"item{i}" for i in range(1000) }
#print(dict1)


#dict1 = {i:f"item {i}"for i in range(1,10001) if i%100==0}
#dict2 = {i:f"Item{i}" for i in range(5)}
#print(dict1)

#dict2 = {value:key for key,value in dict1.items() }
#dict2 = {value.key for key,value in dict1.items()}
#print(dict1,"\n",dict2)

#Set Comprehension:---------------------------------------------------------------------

#dresses = {dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}

#print(type(dresses))

# Small Quiz:--------------------------------------------------- 

list = ["Ansh"], {"dhairya"}, ['Ansh']

for i in range(10):
    print(list)


