import json

student = {
    "name": "Rahim",
    "age": 20,
    "department": "CSE"
}

json_data = json.dumps(student, indent=4)

print("Student Information (JSON Format):")
print(json_data)
