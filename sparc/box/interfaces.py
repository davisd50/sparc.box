from zope.interface import Interface, Attribute

class IBoxConnector(Interface):
    """Box connector class
    
    I'll fill this in later, once I understand what's involved in getting a 
    GE box api connection in place
    """

class IBoxContent(Interface):
    """Box content items"""
    id = Attribute("The content's string Id")
    name = Attribute("The content's string name")
    created_at = Attribute("Datetime of content's creation")
    description = Attribute("String description of content")
    modified_at = Attribute("Datetime of content's last modification")
    tags = Attribute("Set of strings applied to content")

class IBoxFolder(IBoxContent):
    """A Box folder"""

class IBoxFile(IBoxContent):
    """A Box file"""
    sha1 = Attribute("Sha1 signature of content's data")

# Here's a full more helpers to identify the appropriate Plone content types
# for cachable data
class ICachableBoxFile(Interface):
    """Marker for ICachableItem that is intended to be a cached Box file"""
class ICachableBoxFolder(Interface):
    """Marker for ICachableItem that is intended to be a cached Box folder"""