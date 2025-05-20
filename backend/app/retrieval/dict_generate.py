data = {
    "warning": {
        "sentence": [
            {
                "Name": "String",
                "Column": []
            }
        ]
    }
}

# Create a new dictionary to append
new_entry = {
    "Name": "abcd",
    "Column": ["C1"]
}

# Append to the 'sentence' list
data["warning"]["sentence"].append(new_entry)

# Print the contents
for key, value in data.items():
    print(f"Key: {key}, Value: {value}")

print(data)