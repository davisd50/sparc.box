from zope.interface import implements
from zope.component import adapts
from zope.component.factory import IFactory

from sparc.cache import ICachableSource
from sparc.cache import ICachableItem

from sparc.box import IBoxConnector

class boxSource(object):
    """A source of data that can be cached as ICachableItem in a ICacheArea."""
    implements(ICachableSource)
    # Adapter contexts:
    # IBoxConnector: provides mechanism to connect to Box to pull JSON data
    # IFactory (1): generates ICachableItem marked with ICachableBoxFile
    # IFactory (2): generates ICachableItem marked with ICachableBoxFolder
    adapts(IBoxConnector, IFactory, IFactory)
    
    def __init__(self, connector, cachable_box_file_factory, cachable_box_folder_factory):
        self.connector = connector
        self.file_factory = cachable_box_file_factory
        self.folder_factory = cachable_box_folder_factory
        if not ICachableItem.providedBy(self.factory()):
            raise LookupError('Could not adapt, provided factory does not produce objects with ICachableItem interface')
    
    def key(self):
        """Returns string identifier key that marks unique item entries (e.g. primary key field name)"""
        return self.factory().key
    
    def items(self):
        """Returns an iterable of available ICachableItem in the ICachableSource
        """
        # ***Might want to figure a way to recursively work child folder parsing***
        # parent_attributes = Python Dict of parent folder attributes
        # parent = self.folder_factory(parent_attributes)
        # iterate through JSON:
        #  attributes = Python Dict based on JSON key->value pairs
        #  if Folder:
        #   yield self.folder_factory(attributes, parent)
        #  if File:
        #   yield self.file_factory(attributes, parent)
    
    def getById(self, Id):
        """Returns ICachableItem that matches Id or None if not found"""
    
    def first(self):
        """Returns the first ICachableItem available in the ICachableSource or None"""