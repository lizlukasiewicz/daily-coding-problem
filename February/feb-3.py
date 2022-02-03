"""
This problem was asked by Microsoft.

Implement the singleton pattern with a twist. 
First, instead of storing one instance, store two instances. 
And in every even call of getInstance(), return the first instance 
and in every odd call of getInstance(), return the second instance.
"""

class SingletonClass(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
    return cls.instance

#class SingletonChild(SingletonClass):
    #pass

#singleton = SingletonClass()
#child = SingletonChild()
 
#print(child is singleton)
 
#singleton.singl_variable = "Singleton Variable"
#print(child.singl_variable)



class BorgSingleton(object):
  _shared_borg_state = {}
   
  def __new__(cls, *args, **kwargs):
    obj = super(BorgSingleton, cls).__new__(cls, *args, **kwargs)
    obj.__dict__ = cls._shared_borg_state
    return obj
   
borg = BorgSingleton()
borg.shared_variable = 1
 
class ChildBorg(BorgSingleton):
  borg.shared_variable += 1
 
childBorg = ChildBorg()
#print(childBorg is borg)
print(childBorg.shared_variable)