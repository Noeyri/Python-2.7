#

print("Enter age:")
edad = int(raw_input())

if(edad <= 4):
    print("Is in the infancy.")

elif(edad <= 10):
    print("It's in childhood.")

elif(edad <= 14):
    print("Is in puberty.")

elif(edad <= 18):
    print("Is in adolescence.")

else:
    print("It is in other stages of life.")