import csv

new_data = []
# Reading with custom delimiter and quote character
with open('sentences_with_audio.csv', 'r+', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter='\t')
    counter = 0
    for row in csvreader:
        if len(row) >= 3 and row[2] == "arh":
            print("Audio ID: " + row[1] + " Sentence ID: " + row[0])
            counter += 1
            print(row)
            new_data += [row[0:2]]
    print(counter)

# Writing with custom delimiter and quote character
data = [
    ['Name', 'Age', 'City'],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

with open('output_custom.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t', quotechar="'")
    csvwriter.writerow(['Sentence ID', 'Audio ID'])
    for row in new_data:
        csvwriter.writerow(row)
