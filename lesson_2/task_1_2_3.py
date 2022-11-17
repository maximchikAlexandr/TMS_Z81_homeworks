# task 1
var1 = var2 = var3 = 1
print(var1 == var2 == var3)
print(id(var1) == id(var2) == id(var3), end='\n\n')

# task 2
var4, var5 = 3, 3.0
print(var4 == var5)
print(id(var4) == id(var5), end='\n\n')

# task 3
var2 = float(var2)
var3 = bool(var3)
print(var1 == var2 == var3)
print(id(var1) == id(var2) == id(var3), end='\n\n')

var5 = int(var5)
print(var4 == var5)
print(id(var4) == id(var5))
