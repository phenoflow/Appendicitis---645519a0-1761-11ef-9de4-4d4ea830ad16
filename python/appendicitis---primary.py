# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"J221.00","system":"readv2"},{"code":"J21..00","system":"readv2"},{"code":"J222.00","system":"readv2"},{"code":"14C2.00","system":"readv2"},{"code":"J223.00","system":"readv2"},{"code":"16040.0","system":"readv2"},{"code":"104722.0","system":"readv2"},{"code":"15393.0","system":"readv2"},{"code":"104496.0","system":"readv2"},{"code":"29882.0","system":"readv2"},{"code":"9388.0","system":"readv2"},{"code":"3472.0","system":"readv2"},{"code":"25856.0","system":"readv2"},{"code":"698.0","system":"readv2"},{"code":"37817.0","system":"readv2"},{"code":"52383.0","system":"readv2"},{"code":"16152.0","system":"readv2"},{"code":"1999.0","system":"readv2"},{"code":"15490.0","system":"readv2"},{"code":"24325.0","system":"readv2"},{"code":"17014.0","system":"readv2"},{"code":"4130.0","system":"readv2"},{"code":"16716.0","system":"readv2"},{"code":"7210.0","system":"readv2"},{"code":"35406.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('appendicitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["appendicitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["appendicitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["appendicitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
