import json

# Sample JSON data
json_data = '''
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
'''

# Parse the JSON data into a Python dictionary
data = json.loads(json_data)

# Choose the key you want to print
chosen_key = "age"

# Check if the chosen key exists in the dictionary
if chosen_key in data:
    value = data[chosen_key]
    print(f"{chosen_key}: {value}")
else:
    print(f"The key '{chosen_key}' does not exist in the JSON data.")