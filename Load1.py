import csv
with open('movie.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Movie", "ACTOR"])
    writer.writerow([1, "Snoden", "SRK"])
    writer.writerow([2, "Batman", "Christan"])