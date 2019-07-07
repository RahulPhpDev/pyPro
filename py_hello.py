def parent():
	print("Parent Function")

	def child1():
	   print("child1 1 function")

	def child2():
	   print("Child2 function ")

	child1()
	child2()

parent()    


def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child()
    else:
        return second_child

first = parent(1)        
print(first)