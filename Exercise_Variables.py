"""
exercise Var
"""
a, b, c = 5, 10, 100
fl_1, fl_2, fl_3 = 10.8, 100.555, 33.99999
boolean_Var = True
boolean_Var2 = False
string_A = "string AAA"
string_B = "string BBB"
print ("a = ", a, "\nb = ", b, "\n", c)
print ("fl_1 = ", fl_1, "  fl_2 & fl_3 are ", fl_2, "and ", fl_3)
print ("boo_Var = ", boolean_Var, "\nboo_Var2 = ", boolean_Var2)
print (string_A, "   ", string_B, "\n")

fruits = ["Aple", "Orange", "Peach"]
fruits_2 = {"Aple", "Orange", "Peach"}
a, b, c = fruits
print (fruits)
print (fruits_2)
print (a,"", b, "" , c, "\n")
print ("\n  a - ", type(a), ";    b - ", type(b), ";   c - ", type(c))
print ("\n  fruits - ",type(fruits), "\n  fruits_2 - ",type(fruits_2), "\n\n")

# a = boolean(True)
a = bool(False)
# b = fl(3.555)
b = float(5.333)
c = int(777)
d = str("RRRRR")
print (a, b, c, d, "\n")
print ("\n a - ", type(a), ";    b - ", type(b), ";   c - ", type(c), "\n d - ", type(d))

tuppp = 3, 5, "aaa", "rrr"
print (tuppp)
print ("tuppp -  ", type(tuppp))
print ("\n a - " f- (a), ";    b - ", type(b), ";   c - ", type(c), "\n d - ", type(d))
