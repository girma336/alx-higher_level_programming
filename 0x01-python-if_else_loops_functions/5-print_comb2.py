for i in range(0, 100):
    if i < 10:
        print("0{}".format(i), end= ", ")
    else:
        if i != 99:
            print(i, end= ", ")
        else:
            print(i, end= "")
            
            
print()