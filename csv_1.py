import csv
from random import randint as ran

def random_point(size):
    return (ran(0, size), [ran(0, 24), ran(0, 60), ran(0, 60)], ran(0, size))

with open('points.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x', 'y', 'z'])
    for i in range(10):
        writer.writerow(random_point(100))

def read_csv(file):
    with open(file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

read_csv('points.csv')