from attributeaccess import A 

x = A()
print(x.pub)

print(x._prot)

# Should never be used, its violates the rules
print(x._A__priv)
# print(x.__priv)

