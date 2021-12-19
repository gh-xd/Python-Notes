import weakref

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()
    
    def __call__(self, name, *args, **kwargs):
        if name in self.__cache:
            return self.__cache[name]
        else:
            obj = super().__call__(name)
            self.__cache[name] = obj
            return obj
        
class Spam(metaclass=Cached):
    def __init__(self, name, **kwargs):
        print('Creating Spam({!r})'.format(name))
        self.name = name
        self.properties = kwargs


a = Spam('Guido', {'age':3})
b = Spam('Diana', {'age':18})
c = Spam('Guido', {'age':3})

assert a is not b

print(a is c)
        