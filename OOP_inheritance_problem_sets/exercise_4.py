# The method resolution order (MRO) is the order in which Python traverses 
# the class hierarchy to look for methods. For example, suppose you have a 
# Bulldog object called bud and you call: bud.drool. Python first looks for a 
# Bulldog.drool method. If it finds the method, it invokes the method and stops 
# searching. If it doesn't find Bulldog.drool, it next looks for Dog.drool, 
# then Pet.drool, and, finally, object.drool. If it finds any of these methods, 
# it invokes that method and stops searching. If it doesn't find the method anywhere, 
# it raises an AttributeError.

# In our simple class hierarchy, the MRO is pretty straightforward. Things can 
# quickly get complicated in larger libraries or frameworks. To see the MRO, 
# we can use the mro class method.

# Copy Code
# print(Bulldog.mro())
# # [<class '__main__.Bulldog'>, <class '__main__.Dog'>, <class
# #'__main__.Pet'>, <class 'object'>]
# Using mro like that is often not very pretty. Instead, you can use a 
# list comprehension to make the output more readable:

# Copy Code
# print([ cls.__name__ for cls in Bulldog.mro() ])
# # ['Bulldog', 'Dog', 'Pet', 'object']
# Note that mro returns a list. Additionally, it's important to remember 
# that all classes in Python are subclasses of the object class by default.