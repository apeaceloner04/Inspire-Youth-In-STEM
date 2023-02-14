names =('loreen', 'clive', 'leon', 'mark', 'fiona')
print(names)
print(names[0])
print(names[-1])
print(names[2])
print(names[0:3])
#list of fruits
fruits=["apple","kiwi","passion","pawpaw","mango","orange","lime"]
print(fruits[0:-1])
print(fruits[3])
print("my favourite fruit is",fruits[4].upper())
#Adding two lists
#Adding two items use plus sign then print
vegetables=["kales","cabbages","spinach","managu","terere","brocolli"]
stationary=["pens","pencils","hilighter","office glue","stapler","scissors"]
shoppings=vegetables+stationary
print(shoppings)
print(shoppings[5])
#for looping
for vegetable in vegetables:
    print(vegetable)
    for shopping in shoppings:
        print(shopping)
print("My names is " + names[0] + " and my favourite fruit is " + fruits[3])