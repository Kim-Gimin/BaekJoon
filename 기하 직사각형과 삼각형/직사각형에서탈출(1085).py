x, y, w, h = map(int, input().split())

if (w-x) >= x:
    if(h-y) >= y:
        if x >= y:
            print(y)
        elif y > x:
            print(x)
    else:
        if x >= (h-y):
            print(h-y)
        elif (h-y) > x:
            print(x)
elif x > (w-x):
    if(h-y) >= y:
        if (w-x) >= y:
            print(y)
        elif y > (w-x):
            print(w-x)
    elif y > (h-y):
        if (w-x) >= (h-y):
            print(h-y)
        elif (h-y) > (w-x):
            print(w-x)
        
            