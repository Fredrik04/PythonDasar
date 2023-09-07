import gc
class MyClass:
    def __init__ (self, name):
        self.name = nameprint(f'(self.name) created')
    def __del__ (self):
        pritn(f'(self.name) deleted')

gc.disable() #Menonaktifkan garbage collection

a = MyClass('Object 1')
b = MyClass('Object 2')
c = MyClass('Object 3')

del a
del b
del c

gc.enable() #Mengaktif garbage collection
gc.collect() #Memanggil proses garbage collection secara manual