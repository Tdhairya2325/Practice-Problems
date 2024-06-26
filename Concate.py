
# USING JOIN OPERATOR
var1 = "Geeks"
var2 = "for"
var3="Geeks"
# join() method is used to combine the strings
print("".join([var1, var2,var3]))
# join() method is used here to combine 
# the string with a separator Space(" ")
print(" ".join([var1, var2,var3]))


#USING + OPERATOR
# Defining strings
var1 = "Hello "
var2 = "Geek"
# + Operator is used to combine strings
var3 = var1 + var2
print(var3)


#USING % OPETRATOR
var1 = "Welcome"
var2 = "back"
var3="Geek"
# % Operator is used here to combine the string
print("%s %s %s"% (var1, var2,var3))

#USING COMMA(,)
print(var1,var2,var3)

#USING FORMAT{} FUNCTION
var1 = "Hello"
var2 = "Geeks"
var3="How are you"
# format function is used here to 
# combine the string
print("{} {} {}".format(var1, var2,var3))
# store the result in another variable 
var3 = "{} {} {}".format(var1, var2,var3)
print(var3)

#USING F-STRING
name = "GFG"
age = 25
College= "DDIT"
# String concatenation using f-string
greeting = f"Hello, my name is {name} and I am {age} years old. I'm studying in {College}"
print(greeting)






