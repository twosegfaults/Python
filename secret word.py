word= str(input("Enter the code word: "))
while word!="chupacabra":
    print("Incorrect. Try Again.")
    word=str(input("Enter next try: "))
    if word=="chupacabra":
        break
print("Correct answer.", "You've successfully left the loop")