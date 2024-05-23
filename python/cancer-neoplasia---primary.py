# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2024.

import sys, csv, re

codes = [{"code":"B340100","system":"readv2"},{"code":"B834000","system":"readv2"},{"code":"B34yz00","system":"readv2"},{"code":"B34..00","system":"readv2"},{"code":"B13z.00","system":"readv2"},{"code":"B343.00","system":"readv2"},{"code":"B933.00","system":"readv2"},{"code":"B345.00","system":"readv2"},{"code":"B342.00","system":"readv2"},{"code":"B134.00","system":"readv2"},{"code":"B35..00","system":"readv2"},{"code":"B340000","system":"readv2"},{"code":"B141.00","system":"readv2"},{"code":"B34z.00","system":"readv2"},{"code":"B834100","system":"readv2"},{"code":"B58y000","system":"readv2"},{"code":"B13..00","system":"readv2"},{"code":"Byu6.00","system":"readv2"},{"code":"B915.00","system":"readv2"},{"code":"B46..00","system":"readv2"},{"code":"B350100","system":"readv2"},{"code":"B902400","system":"readv2"},{"code":"B575100","system":"readv2"},{"code":"B142.00","system":"readv2"},{"code":"B350.00","system":"readv2"},{"code":"B35z.00","system":"readv2"},{"code":"B902500","system":"readv2"},{"code":"B58y500","system":"readv2"},{"code":"B142000","system":"readv2"},{"code":"ZV10415","system":"readv2"},{"code":"B35zz00","system":"readv2"},{"code":"B346.00","system":"readv2"},{"code":"B575000","system":"readv2"},{"code":"B341.00","system":"readv2"},{"code":"B34y.00","system":"readv2"},{"code":"B350000","system":"readv2"},{"code":"B344.00","system":"readv2"},{"code":"B340.00","system":"readv2"},{"code":"B340z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cancer-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cancer-neoplasia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cancer-neoplasia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cancer-neoplasia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
