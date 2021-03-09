a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
            }
        }
    }


def print_depth(data,level=1, dicto=None):
    """
    Traverse through the input dictionary and prints
    the depth of it's nested elements (dict)
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

    return dicto
