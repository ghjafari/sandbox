import csv

csv_loc="C:/Users/ghjafari/Desktop/svcp2.csv"

delete_next_line = False



def test():
    with open(csv_loc, 'r+') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            if(row[1] is not '') and ("Foundation" in row[1]):
                links = row[1].split('\n')

                for link in links:
                    if "/IPC-9100/" in link:

            #csv_file.close()


    def modify_csv():
        with open(csv_file, '+r') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)

            for row in rows:
                pass
