# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"59158.0","system":"readv2"},{"code":"5692.0","system":"readv2"},{"code":"9699.0","system":"readv2"},{"code":"7832.0","system":"readv2"},{"code":"662.0","system":"readv2"},{"code":"33826.0","system":"readv2"},{"code":"28587.0","system":"readv2"},{"code":"3141.0","system":"readv2"},{"code":"9206.0","system":"readv2"},{"code":"60360.0","system":"readv2"},{"code":"33538.0","system":"readv2"},{"code":"10119.0","system":"readv2"},{"code":"10830.0","system":"readv2"},{"code":"29710.0","system":"readv2"},{"code":"2394.0","system":"readv2"},{"code":"29890.0","system":"readv2"},{"code":"422.0","system":"readv2"},{"code":"23344.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('appendicitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["appendicitis-procedure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["appendicitis-procedure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["appendicitis-procedure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
