bob = "person"
print("Bob is a " + bob)
bobLocation = "grocery store"
print("Bob is at the " + bobLocation + " and he has bought a cat and a lot of bacon!")
bobLocation = "Home"
print("Bob has gone " + bobLocation)
catAttitude = "scared"
print("The cat is " + catAttitude)
print("What do you want Bob to do with his new cat?")
print("Your Options Are:")
print("  play with it")
print("  chase it")
print("  feed it")
print("  give it bacon")
x = input("> ")
if x.lower() == "play with it":
    catAttitude = "happy"
elif x.lower() == "chase it":
    catAttitude = "very scared"
elif x.lower() == "feed it":
    catAttitude = "content"
elif x.lower() == "give it bacon":
    catAttitude = "BACON CRAZY!"
else:
    catAttitude = "confused"
print("The cat is " + catAttitude)
if catAttitude == "BACON CRAZY!":
    print("How do you tame it?")
    print("Your Options Are:")
    print("  leave it alone")
    print("  lock it up")
    print("  abandon it")
    print("  give it more bacon")
    y = input("> ")
    catAction = "is confused"
    if y.lower() == "leave it alone":
        catAction = "destroys the rug"
    elif y.lower() == "lock it up":
        catAction = "meows a lot"
    elif y.lower() == "abandon it":
        catAction = "emails you sad cat pictures"
    elif y.lower() == "give it more bacon":
        catAction = "regurgitates a flamethrower made of bacon and burns your house down"
    print("The cat " + catAction)
