
class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        return 'static method called'
    

obj = MyClass()
obj.method()
# ('instance method called', <MyClass instance at 0x10205d190>)

MyClass.method(obj)
# ('instance method called', <MyClass instance at 0x10205d190>)

obj.classmethod()
# ('class method called', <class MyClass at 0x101a2f4c8>)

obj.staticmethod()
'static method called'