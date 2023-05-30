picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for sublist in picture:
    for item in sublist:
        if (item == 1):
            print("*",end = "")    
        else:
            print(" ",end ="")
    print('',sep='\n')