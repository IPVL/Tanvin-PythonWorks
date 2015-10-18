import abc
from abstract_base import PluginBase

class SubclassImplementation(PluginBase):
    
    def load(self):
        print "load overridden"
    
    def save(self):
        print "save overridden"

if __name__ == '__main__':
    print 'Subclass checked:', issubclass(SubclassImplementation, PluginBase)
    print 'Instance checked:', isinstance(SubclassImplementation(), PluginBase)
    obj = SubclassImplementation()
    obj.load()

