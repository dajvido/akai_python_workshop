# -*- coding: UTF-8 -*-
import csv


class Datum(object):
    """ imaginary base class for a CSV row """
    pass


def get_fruits(filename):
    with open(filename) as csvfile:
        fruits = []
        file_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        rows = [row[0].split(',') for row in file_reader]
        Fruit = type(filename.split('.')[0], (Datum, ), dict())
        for row in rows[1:]:
            MyFruit = Fruit()
            values = dict(zip(rows[0], row))
            for value in values:
                setattr(MyFruit, value, float(values[value]))
            fruits.append(MyFruit)

        return fruits


f1 = get_fruits("Orange.csv")
f2 = get_fruits("Pear.csv")

# both oranges and pears have id's and weight, there are 2 of each
assert f1[0].id
assert f2[0].id
assert f1[0].weight
assert f2[0].weight
assert len(f1) == len(f2) == 2

# oranges have slices
assert f1[0].slices
assert f1[0].__class__.__name__ == "Orange"

# pears are oblong and have diameter
assert f2[0].oblongless
assert f2[0].diameter
assert f2[0].__class__.__name__ == "Pear"

total_weight = sum([f.weight for f in f1 + f2])
print("total weight", total_weight)
assert total_weight == 1.035
