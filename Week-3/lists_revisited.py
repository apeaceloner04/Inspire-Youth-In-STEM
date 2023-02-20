#!git/user/bin/env python 3


friends=["Phoebe","Nora","Max","Lincoln","Rose"]
print(friends)
friends[0]="Mary"
print(friends)
print("--------------------------")
new_friends= friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)