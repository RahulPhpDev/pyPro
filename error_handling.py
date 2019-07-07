#The try block will generate a NameError, because x is not defined:

try:
  print(x)
except NameError as e:
  print(e)
  print("Variable x is not defined")
  print("""Hello
Hi""")
except:
  print("Something else went wrong")
