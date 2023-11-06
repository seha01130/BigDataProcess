import sys
import calendar

inputFile = sys.argv[1]
outputFile = sys.argv[2]

dayofweek = ['0', '1', '2', '3', '4', '5', '6']
dayofweek2 = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
uber_dict = dict()

with open(inputFile, "rt") as f:
    for line in f:
        line = line.strip()
        line = line.split(",")
        d = line[1]
        dList = d.split("/")
        year = int(dList[2]); month = int(dList[0]); day = int(dList[1])
        line[1] = dayofweek[calendar.weekday(year,month,day)]
        #print(line)
        
        if (line[0],line[1]) in uber_dict:
            uber_dict[(line[0],line[1])][0] += int(line[2])
            uber_dict[(line[0],line[1])][1] += int(line[3])
        else:
            uber_dict[(line[0],line[1])] = [int(line[2]), int(line[3])]
    # print(uber_dict)
    sorted_dict = dict(sorted(uber_dict.items()))
    # print(sorted_dict)
    
    with open(outputFile, "wt") as fp:
        keylist = sorted_dict.keys()
        for key in keylist:
            value = sorted_dict[key]
            # print(value)
            newone = ''.join(x + ',' for x in key)
            newone = newone.split(",")
            newone[1] = dayofweek2[int(newone[1])]
            # print(newone)
            line = newone[0] + "," + newone[1] + " " + str(value[0]) + "," + str(value[1])
            fp.write(line + "\n")