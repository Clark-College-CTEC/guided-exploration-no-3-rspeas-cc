# Guided Exploration No. 3
# Speas, Roger

# access a library of python function related to randomality
import random

# initializes an empty list, I assume a pointer
#    this will be a list of string - the randomly generated rap names
possible_names = []


# creates fileref, outputFile, specifies location and Write Acccess
outputFile = open(
    'Crap-names-output.txt', 'w')
exit
# create fileref, datafile, specifies location and Read Access
#   with facilities opening and closing the file during FOR read
with open('rap-names.txt', 'r') as dataFile:
    # FOR reads each line of the input file as text into NAME
    for name in dataFile:
        # and rstrip removes trailing blanks and EOL character - variable length
        # each name is appended to the list - POSSIBLE_NAMES
        possible_names.append(name.rstrip())

print()
# terminal input from user for number(int) names to generate - COUNT
count = int(input('How many rap names would you like to create? '))
# terminal input from user for number(int) of words/parts in name - PARTS
parts = int(input('How many parts should the name contain? '))
print(20*"-")

# loops for the number names to generate from user input
for i in range(count):
    # creates an empty list, NAME_PARTS which the names parts will
    #   be sequentials added
    name_parts = []
    # loops for the number of user requested name parts
    for j in range(parts):
        # the number of elements in the possible_names list is determined
        #   during each execution of the loop and passed as the maximum
        #   range limit of randint (random integer generator)
        # the random int is used to select a name from a list of names
        #   and appended to the multipart NAME_PARTS
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

    # a leading blank and NAME_PARTS are joined and appended with a non-printable
    #   newline and written to the fileref, OUTPUTFILE
    outputFile.write(f"{' '.join(name_parts)}\n")
    # the same value without the newline is written to the terminal
    print(f"{' '.join(name_parts)}")

print(20*"-")
# close the output file
outputFile.close()
