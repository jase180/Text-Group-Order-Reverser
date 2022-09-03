#  My first program - a script that takes a .txt file as input.  The file would be lines of texts and grouped in lines.
#  The script reverses the order of the groups of lines and writes into an output txt file.
#  The first word of the first line of each group is always the same.  BANANAS is used as a substitute of actual word.


#  Parsing input txt file into a ls

ls = []  # array of each line from input txt file

with open("intxt.txt", "r") as f:
    for line in f:
        if line.strip() == '':
            continue
        else:
            ls.append(line.strip())

#  Sorting using a loop checking starting word of each line, grouping into a list and appending out list with the
#  group list

out = []  # list of lists of grouped lines
group = []  # list of grouped lines

group.append(ls[0]) # put first line into group to avoid an empty ls in out[0]

for line in range(1,len(ls)):  # starting from 1 because first line is already put in
    words = ls[line].split()
    first = words[0] #  check first word
    if "BANANAS" in first:  #  Word would always be in upper case.
        out.insert(0,group)
        group = []
        group.append(ls[line])
    else:
        group.append(ls[line])

out.insert(0,group) #  insert last group


#  Writing out into a txt file with required format

with open("outtxt.txt","w") as f:
    for group in out:
        for line in group:
            print("   " + line, file = f)
