from json import loads

def solve(json):
    json_object = loads(json)
    
    def count(obj):
        if isinstance(obj, int):
            return obj
        if isinstance(obj, str):
            return int(obj) if obj[-1].isdigit() else 0
        if isinstance(obj, list):
            return sum([count(o) for o in obj])

        if 'red' in obj.values():
            return 0
        
        return sum([count(val) for val in obj.values()])
    
    return count(json_object)

with open('input_12.txt', 'r') as f:
    print(solve(f.read().strip()))