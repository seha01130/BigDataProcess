import sys

inputFile = sys.argv[1]
outputFile = sys.argv[2]

genre_dict = dict()

with open(inputFile, "rt") as f:
    for line in f:
        line = line.strip()
        line = line.split("::")
        #print(line)
        genre = line[2].split("|")
        #print(genre)
        for g in genre:
            if g in genre_dict:
                genre_dict[g] += 1
            else:
                genre_dict[g] = 1
    #print(genre_dict)
    with open(outputFile, "wt") as fp:
        keylist = genre_dict.keys()
        for key in keylist:
            line = key + " " + str(genre_dict[key])
            fp.write(line + "\n")