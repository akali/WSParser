import re

with open("../data/lessons.txt") as fp:
    for line in fp:

        line = line.replace("Круглый зал", "Круглый_зал")
        print(line)
        line = line.rstrip().split(" ")

        match = re.search("\(([0-9:]{5})-([0-9:]{5})\)", line[-1])

        print("Start: " + match.group(1))
        print("End: " + match.group(2))

        print("Room: " + line[-2])
        print("Class: " + line[-3])
        print("Teacher: " + line[-5] + " " + line[-4])
        line = line[:-5]
        print("Subject:" + " ".join(line))
