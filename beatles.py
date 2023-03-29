beatles=["Paul McCartney", "John Lennon", "George Harrison"]
print(beatles, "-lineup 1")
beatles.append(str(input("Enter name of first entrant: ")))
beatles.append(str(input("Enter name of second entrant: ")))
print(beatles, "-lineup 2")
del beatles[3]
del beatles[3]
beatles.insert(0, "Ringo Starr")
print(beatles, "-final lineup")