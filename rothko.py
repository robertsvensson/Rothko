# Rothko takes to two files as input and writes the
# output to result.txt in the current directory

import sys
 
firstarg = str(sys.argv[1])
secondarg = str(sys.argv[2])

# Read first file into an list called firstfilelist
firstfilelist = []
with open(firstarg, "r") as f:
  for line in f:
    firstfilelist.append(line)
    
    
# Read first file into an list called secondfilelist    
secondfilelist = []
with open(secondarg, "r") as f:
  for line in f:
    secondfilelist.append(line.splitlines())


# Open file for writing
output = open('result.txt', 'w')

    
# Loop through the first list
x = 0
for y in firstfilelist:
    currentrow = firstfilelist[x]
    
    # create a sting and strip the list chars
    currentrow = str(currentrow)
    currentrow = currentrow.strip("'")
    currentrow = currentrow.strip('[')
    currentrow = currentrow.strip(']')
    currentrow = currentrow.strip("'")
    currentrow = currentrow.rstrip('\r\n')
    
    # Loop trhough the second list
    a = 0
    for b in secondfilelist:
        secondcurrentrow = secondfilelist[a]
        secondcurrentrow = str(secondcurrentrow)
        secondcurrentrow = secondcurrentrow.strip("'")
        secondcurrentrow = secondcurrentrow.strip('[')
        secondcurrentrow = secondcurrentrow.strip(']')
        secondcurrentrow = secondcurrentrow.strip("'")
        result = (str(currentrow)+str(secondcurrentrow))
        
        print result
        a = a+1
        
        # And write the combined result to result.txt in the current directory
        output.write(result+'\n')
    x = x+1