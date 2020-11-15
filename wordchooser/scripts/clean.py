import pprint
import csv

def huijiang():
    answers = {}
    with open('allanswers') as allanswers:
        readCSV = csv.reader(allanswers, delimiter=',')
        for row in readCSV:
            answers[row[0]] = row[1:]

    choices = {}
    with open('allchoices') as allchoices:
        readCSV = csv.reader(allchoices, delimiter=',')
        for row in readCSV:
            if ".txt" in row[0]:
                f = row[0]
                choices[f] = []
                q = 0
            else:
                answer = row[int(answers[f][q])]
                if ' ' not in answer:
                    answer = '_' + answer + '_'
                choices[f].append(answer)
                q += 1

    texts = {}
    with open('alltext') as alltexts:
        alllines = alltexts.readlines()
        curtext = ""
        f = ""
        for row in alllines:
            if ".txt" in row:
                if curtext != "":
                    curtext = curtext.format(*choices[f])
                    texts[f] = curtext
                f = row.strip()
                curtext = ""
            else:
                # piece together all lines for current text
                curtext += row.strip()

    with open("huijiang2.txt", "w") as file:
        for passage in texts.values():
            print(passage, file=file)