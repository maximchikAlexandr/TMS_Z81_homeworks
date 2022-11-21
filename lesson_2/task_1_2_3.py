# task 1
var1 = var2 = var3 = 2
assert var1 == var2 == var3
assert var1 is var2 is var3

# task 2
var4, var5 = 3, 3.0
assert var4 == var5
assert var4 is not var5

# task 3
var1, var2 = float(var1), float(var2)
assert var1 == var2 == var3
assert var1 is not var2 is not var3

var5 = int(var5)
assert var4 == var5
assert var4 is var5
