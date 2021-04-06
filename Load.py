import csv

mydict = [{'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1', 'name': 'Pratik', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3', 'name': 'Gopal', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5', 'name': 'Saurabh', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Pathu', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1', 'name': 'Venku', 'year': '2'}]

fields = ['name', 'branch', 'year', 'cgpa']

filename = "records.csv"

with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    print()
    writer.writeheader()
    print()
    writer.writerows(mydict)