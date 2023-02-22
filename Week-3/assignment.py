#create a list of empty of favourite musicians
#using a for loop  add new musicians
#copy the list called celebs
#sort the list
#pop out two celebs
#count the remaining celebs in the list


favourite_musicians=["Jessie murph","sam smith","bruno mars","miley cyrus","dean lewis"]
for musician in favourite_musicians:
    print(musician)
favourite_musicians.append("rihanna")
favourite_musicians.append("drake")
favourite_musicians.append("meghan trainor")
favourite_musicians.append("cardi b")
for musician in favourite_musicians:
    print(musician)

celebs = favourite_musicians.copy()
print(celebs)

celebs.sort()
print(celebs)

celebs.pop()
print(celebs)

celebs.copy()
print(celebs)

print(len(celebs))