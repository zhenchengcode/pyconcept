# https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

# non singleton
class normal:
	def __init__(self, val):
		self.val = val
normal1 = normal(1)
normal2 = normal(1)
print(normal1==normal2)

# Method 1 use decorator
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class MyClass(): # can inherit from some other classes
    pass

newChild1 = MyClass()
newChild2 = MyClass()
print(newChild1==newChild2)
print(type(newChild1))

# Method 2 use inheritance
class Singleton(object):
	_instance = None
	def __new__(class_, *args, **kargs):
		if not isinstance(class_._instance, class_):
			class_._instance = object.__new__(class_, *args, **kargs)
		return class_._instance
class MyClass(Singleton, BaseClass):
	pass


# catalogenrich implementation
class Singleton:

    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.klass(*args, **kwds)
        return self.instance

@Singleton
class onlyOne(object):
	# cursor = None
	def __init__(self, dbconfig):
		print(dbconfig)
		self.cursor = dbconfig


obj1 = onlyOne('my config1')
obj2 = onlyOne('my config2')
print(obj1==obj2)
print(type(obj1))
print(obj1.cursor)
print(obj2.cursor)


