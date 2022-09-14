"""
exercise Print
"""

fruits = ["Aple", "Orange", "Peach"]
fruits_2 = {"Aple_2", "Orange_2", "Peach_2"}
a, b, c = fruits
print (fruits)
print (fruits_2)
print ("\n  fruits - ",type(fruits), "\n  fruits_2 - ",type(fruits_2), "\n\n")

tuppp = 3, 5, "aaa", "rrr"
tuppp_1 = (3, 5, "aaa", "rrr")

print (tuppp)
print (tuppp_1)
print (type(tuppp), type(tuppp_1))


print (" F1 - %s; F2 - %s; F3 - %s" % (a, b, c))
# print (" F1 - %s; F2 - %s; F3 - %s" % fruits)

print ("rrr - %s" % a)
print ("rrr - %s, rrr - %s." % (a, b))

# d = 3.55
# print ("tuppp -  ", type(tuppp))
# print ("\n a - ", (a), ";    b - ", type(b), ";   c - ", type(c), "\n d - ",
#
print ("aaa - %s, bbb - %s, ccc - %s  \n" %(fruits, fruits, fruits))
print ("aaa - %s, bbb - %s, ccc - %s  \n\n" %(fruits_2, fruits_2, fruits_2))
#print (f")
print (f"fruits {fruits}")
print (f"fruits {fruits_2}")
print (f"fruits {tuppp}")
