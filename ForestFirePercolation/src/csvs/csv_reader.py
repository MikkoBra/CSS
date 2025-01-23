import csv


def read_csv():
    with open('../Simulation_data_test_criticalp.csv', mode='r') as file:
        csvFile = csv.reader(file)
        print(csvFile)
        header = True
        data = {}
        labels = []
        for line in csvFile:
            if header:
                labels = line
                for label in labels:
                    data[label] = []
                header = False
            else:
                column = 0
                while column < len(line):
                    if column != 2 and column != 4:
                        value = float(line[column])
                        data[labels[column]].append(value)
                    else:
                        data[labels[column]].append(t)



read_csv()
