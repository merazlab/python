import mod1 as m1 
import spack.mod6 as m6 

print(m1.var1)
print(m1.mod1fun())

print(m6.var6)
print(m6.mod6fun())
print("-------------------")
from mod2 import var2
from spack.mod7 import var7, mod7fun

print(var2)
print(var7)
print(mod7fun())