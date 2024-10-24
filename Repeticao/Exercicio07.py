a = 1
b = 1

# for i in range(5):
#     c = a + b
#     a = b
#     b = c
#     print(c)
print(a)
c = 0
while c < 2000:
    print(c)
    c = a + b
    a = b
    b = c
    
