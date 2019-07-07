def simple_deco(func):
	print("Before Fun")
	func()
	print("Afters Fun")
	return 5,func()

def child():
	print("this is Child Function")

obj = simple_deco(child)
print(obj)	