import csv

with open('players.csv', 'w', newline='') as file:
    fieldnames = ['player', 'rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player': 'ronaldo', 'rating': 90})
    writer.writerow({'player': 'messi', 'rating': 95})
    writer.writerow({'player': 'neymar', 'rating': 85})