students = [
    {"name": "Jake", "City": "Manila", "Food": "Burger"},
    {"name": "Raph", "City": "New York", "Food": "Ham"},
    {"name": "Maki", "City": "Prague", "Food": "Carbonara"},
    {"name": "Ron", "City": "San Diego", "Food": "Egg"},
    {"name": "Cris", "City": "Austin", "Food": "Lasagna"}
]

students.sort(key=lambda city: city["Food"])
print(students)