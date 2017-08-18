guest_names = ["Zhang Yi","Zhang Shaohua","Wang Lihui"]
print("My Guest List\n" + guest_names[0].title() + "\n" + guest_names[1].title() + "\n" + guest_names[2].title())
print(guest_names[1].title() + " cannot to come the party")
del guest_names[1]
print("My Guest List\n" + str(guest_names))
print('I find a bigger table than before,so I can invite more friend to join the party')
guest_names.insert(0,"aaa")
guest_names.insert(2,"bbb")
guest_names.append("ccc")
print("Dear friend " + guest_names[0] + " Welcome to join my party")
print("Dear friend " + guest_names[2] + " Welcome to join my party")
print("Dear friend " + guest_names[4] + " Welcome to join my party")
print("My big table cannot reach my home so I can only invite 2 friend to my home")
unlike_people
