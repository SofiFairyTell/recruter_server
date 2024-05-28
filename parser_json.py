import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def get_criteria(data):
    return data['criteria']

def get_employees(data):
    return data['employees']

def assess_employee(employee, criteria):
    print(f"\nAssessing employee {employee['name']}:")
    scores = {}
    for criterion in criteria:
        score = float(input(f"Rate {employee['name']}'s {criterion}: "))
        scores[criterion] = score
    return scores