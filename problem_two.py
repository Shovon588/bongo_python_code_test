class Person():
    """
    This is a class for a person's information.
    
    Attributes:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person.
        father (object/None): Father's information as a class object
    """
    def __init__(self,first_name,last_name,father):
        """
        Initiates the class with a first_name, last_name and father (class object)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)


a = {
    "key1":1,
    "key2":{
        "key3":1,
        "key4":{
            "key5":4,
            "user":person_b,
            }
        }
    }

b = {"user2": person_b}

def print_depth(data,level=1, dicto=None):
    """
    Traverse through the input dictionary and prints
    the depth of it's nested elements (dict/object)
    """
    if dicto is None:
        if not isinstance(data,dict):
            raise TypeError("Input must be dictionary")
        
        dicto = {}
        
    
    for key in data:
        dicto[key] = level
        print(key,level)

        if isinstance(data[key],dict):
            print_depth(data[key],level+1, dicto)
        else:
            try:
                # Get the name of attributes and it's value of the object as dictionary
                get_dict = data[key].__dict__
                print_depth(get_dict,level+1, dicto)
            except AttributeError:
                pass
            
    return dicto

