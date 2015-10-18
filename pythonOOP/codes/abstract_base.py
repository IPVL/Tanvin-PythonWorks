#! /usr/bin/env python
import abc

class PluginBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object."""
        print "loaded"
    
    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output."""
        pass

#p = PluginBase()
#p.load()
