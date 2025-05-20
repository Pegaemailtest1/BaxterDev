from collections import defaultdict
import json

# This will store all categories dynamically
dict_data = defaultdict(list)

def add_input(input_type, input_list, index):
    for item in input_list:
        found = False
        # Check if item already exists under this type
        for entry in dict_data[input_type]:
            if entry["name"] == item:
                entry["columns"].append(index)
                found = True
                break

        if not found:
            new_entry = {
                "name": item,
                "columns": [index]
            }
            dict_data[input_type].append(new_entry)

    return dict_data

# Example usage:
add_input("warning", ["test1", "test2", "test3"], 1)
add_input("warning", ["test2", "test1"], 2)
# add_input("caution", ["abc", "test2"], 2)
# add_input("claim", ["reusable", "reusable"], 3)


# Pretty print
#print(json.dumps(dict_data, indent=2))

print(dict_data)