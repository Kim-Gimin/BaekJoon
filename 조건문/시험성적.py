Score = int(input())

if Score >= 90 and Score <= 100:
    print("A")
elif Score >= 80 and Score < 90:
    print("B")
elif Score >= 70 and Score < 80:
    print("C")
elif Score >= 60 and Score < 70:
    print("D")
else:
    print("F")