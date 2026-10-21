# First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.

# Dictionary of students (id -> details)
student_data = {
    "id1":{ "name": "Alice", "class": "10A", "subject_integration": "Math"},
    "id2":{ "name": "Bob", "class": "10B", "subject_integration": "Science"},
    "id3":{ "name": "Alice", "class": "10A", "subject_integration": "Math"},
    "id4":{ "name": "Charlie", "class": "10C", "subject_integration": "History"},
    "id5":{ "name": "Bob", "class": "10B", "subject_integration": "Science"},
}

result = {}
seen_keys = []  # using a list instead of set

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

# print output line by line
for k, v in result.items():
    print(k, ":", v)

