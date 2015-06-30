    import csv
import sys
def read_data(processed_file):
    #initializing empty lists
    titleList = []
    bodyList = []
    tagsList = []
    with open(processed_file,'r') as fhandle:
        reader = csv.DictReader(fhandle);
        for row in reader:
            titleList += row["Title"]
            bodyList  += row["Body"]
            doc_tags   = row["Tags"].split()
            tagsList  += [doc_tags]
    return titleList,bodyList,tagsList

'''
if __name__ == "__main__":
    titleList, bodyList, tagsList = read_data(sys.argv[1])

