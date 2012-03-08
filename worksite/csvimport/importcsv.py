import csv
import sys

# usage : import importcsv; importcsv.memdictreader("../dir/blah.csv")



def memdictreader(filename):

    # reads the csv file exported from Stickerbook
    memberReader = csv.reader(open(filename, 'rb'), delimiter=',')

    memdict = {}
    for row in memberReader:
        if row[0][0] != "Name":
            memdict[row[0]] = {"gender":row[1], "email":row[2], "room":row[3],
                               "contract_start": row[6], "contract_end":row[7]}

    return memdict


