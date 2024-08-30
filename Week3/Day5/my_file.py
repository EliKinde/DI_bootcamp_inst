import json

my_familt = {
        "parents": ["Beth", "Jerry"],
        "children": ["SummeR", "Morty"]
        }

json_file = "my_file.json"

with open(json_file, 'w') as file_obj:
    json.dump(my_familt, file_obj)

