# encoding: utf-8
# module _random
# from (built-in)
# by generator 1.147
""" Module implements the Mersenne Twister random number generator. """
# no imports

# no functions
# classes

class Random(object):
    """ Random() -> create a random number generator with its own internal state. """
    def getrandbits(self, k): # real signature unknown; restored from __doc__
        """ getrandbits(k) -> x.  Generates an int with k random bits. """
        pass

    def getstate(self): # real signature unknown; restored from __doc__
        """ getstate() -> tuple containing the current state. """
        return ()

    def random(self): # real signature unknown; restored from __doc__
        """ random() -> x in the interval [0, 1). """
        pass

    def seed(self, n=None): # real signature unknown; restored from __doc__
        """
        seed([n]) -> None.
        
        Defaults to use urandom and falls back to a combination
        of the current time and the process identifier.
        """
        pass

    def setstate(self, state): # real signature unknown; restored from __doc__
        """ setstate(state) -> None.  Restores generator state. """
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod object at 0x0000025F617A6460>, 'find_spec': <classmethod object at 0x0000025F617A6490>, 'find_module': <classmethod object at 0x0000025F617A64C0>, 'create_module': <classmethod object at 0x0000025F617A64F0>, 'exec_module': <classmethod object at 0x0000025F617A6520>, 'get_code': <classmethod object at 0x0000025F617A65B0>, 'get_source': <classmethod object at 0x0000025F617A6640>, 'is_package': <classmethod object at 0x0000025F617A66D0>, 'load_module': <classmethod object at 0x0000025F617A6700>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_random', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

