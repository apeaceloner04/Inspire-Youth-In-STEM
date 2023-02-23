#Advanced data tyPES

#Mutables vs immutable
#mutable-data types that can be editted during program life cycle
#       -add/remove elements
#Immutable-data types that cannot be editted during program life cycle
#         -cannot add/remove elements
#1)Lists(Mutable)
#2)Tuples(Immutable)
#3)Dictionaries aka Dict()

friends=("Anita","Hope","Isaac")
# Or friends = [] for
#add ---> append (), extend()
#remove--->pop(), delete()

students =["Marie","Klein","Sophia"]

friends.extend("students")
friends.append("James")
friends.sort()
friends.reverse()

#Tuples
stationary=("pens","ink","pencils")

#replace the whole tuple
stationaries = ("ruler","sharpener","clipboard")
for stationary in stationaries:
    print(stationary)

#3)Dictionaries 
#uses key and value pair to store data

student= {"Name" : "Loreen", "Age" : "18", "Gender" : "Female"}
print(student["Name"])
print(student["Age"])
print(student["Gender"])

#name is the key --->Loreen is the value

friend= {"fav_color" : "Blue", "Hobby" : "swimming", "course" : "accounting", "height" : "5,2","food" : "beef"}
print(friend["fav_color"])
print(friend["hobby"])
print(friend["course"])
print(friend["height"])
print(friend["food"])