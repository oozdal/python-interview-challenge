# Problem
# Write a function to flatten a json object with
# nested keys into a single level


def flatten_json(obj):
    
    ret = {}

    def flatten(x, flattened_key=""):

        if type(x) is dict:
            for current_key in x:
                flatten(x[current_key], flattened_key + current_key + '_')        
        elif type(x) is list:
            i=0
            for elem in x:
                flatten(elem, flattened_key + str(i) + '_')
                i+=1
        else:
            # x === string, integer, etc
            ret[flattened_key[:-1]] = x

    flatten(obj)

    return ret



if __name__ == "__main__":

    nested_obj = {
        "United States": {
            "New Jersey": {
                "Newark": ["Jeremy", "Stacey"]
            },
        "New York": {
            "Brooklyn": "David",
            "Manhattan": "Dan"
            }
        },
        "Canada": {
            "Montreal": "Sarah",
            "Toronto": {
                "Yorkville": "Jessica",
                "Liberty Village": "Sam"
            }
        },
        "Mexico": {
            "Tulum": "Elisabeth"
        }
    } 

    print(flatten_json(nested_obj))


