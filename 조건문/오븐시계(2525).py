A, B = map(int, input().split())
C = int(input())

if (B + C) >= 60:
    if(A + ((B + C) // 60)) >= 24:
        print((A + ((B + C) // 60)) - 24, (B + C) % 60)
    else:
        print(A + ((B + C) // 60), (B + C) % 60)
else:
    print(A, (B+C))




# if (B + C) >= 120:
#     if A >= 23:
#         print(1, (B+C-120))
#     else:
#         print(A+2, (B+C-120))
# elif (B + C) >= 60 and (B + C) < 120:        
#     if A >= 23:
#         print(0, (B+C-60))
#     else:
#         print(A+1, (B+C-60))
# else:
#     print(A, B+C)