num =input("Enter Anything:-  ")
Count=0
vowal=[]
for i in num:
    if (i== "A" or i=="a"):
        Count+=1
        vowal.append(i)
    elif (i== "E" or i=="e"):
        Count+=1
        vowal.append(i)
    elif (i== "I" or i=="i"):
        Count+=1
        vowal.append(i)
    elif (i== "O" or i=="o"):
        Count+=1
        vowal.append(i)
    elif (i== "U" or i=="u"):
        Count+=1
        vowal.append(i) 
print(vowal)
print(Count)
print(f"This are Vowals")
    
