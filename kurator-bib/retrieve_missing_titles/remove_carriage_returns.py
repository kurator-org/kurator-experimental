import csv
import sys

def read_csv(fr):
    fr = open(sys.argv[1], 'rb')
    reader = csv.reader(fr, delimiter=',', dialect=csv.excel)
    return reader
def write_csv(fw):
    fw = open(sys.argv[2],'w')
    writer = csv.writer(fw,lineterminator='\n')
    return writer


# handle extra newlines (carriage returns) in the field/quote of a csv file
def remove_carriage_returns(fr, fw): 
    reader = read_csv(fr)
    writer = write_csv(fw)
    for row in reader:
        row_fw = []
        # print ("Length: ", len(row), row)
        for field in row:
            # print field
            # if '\r\n' in field:
            if field:
                field = field.replace('\n', ' ').replace('\r', '')
            row_fw.append(field)
        writer.writerow(row_fw) 


if __name__ == "__main__":
    remove_carriage_returns(fr = sys.argv[1], fw = sys.argv[2])
    