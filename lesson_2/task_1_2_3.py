# task 1
var1 = var2 = var3 = 1
assert var1 == var2 == var3
assert id(var1) == id(var2) == id(var3)

# task 2
var4, var5 = 3, 3.0
assert var4 == var5
assert id(var4) != id(var5)

# task 3
var2 = float(var2)
var3 = bool(var3)
assert var1 == var2 == var3
assert id(var1) != id(var2) != id(var3)

var5 = int(var5)
assert var4 == var5
assert id(var4) == id(var5)
