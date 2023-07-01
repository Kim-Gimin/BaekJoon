a, b, c = map(int, input().split())
d = 0
result = 0
list = [a, b, c]
if a == b and a == c:
        result = sum(list)
        print(result)        
        
elif max(list) > (sum(list) - max(list)):
    d = (sum(list) - max(list)) - 1
    result = sum(list) - max(list) + d
    print(result)
    
elif max(list) == (sum(list) - max(list)):
    result = sum(list) - 1
    print(result)
    
elif max(list) < (sum(list) - max(list)):
    result = sum(list)
    print(result)