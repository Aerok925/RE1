import re

input_file = "base.txt"
result_file = "result.txt"

inputfile = open(input_file, mode='r', encoding='Latin-1')
resultfile = open(result_file, mode='w', encoding='Latin-1')

lookfor = r"([0-9]{3}).*?([0-9]{3}-[0-9]{4})"

mytext = inputfile.read()

results = re.findall(lookfor, mytext)
for elem in results:
    resultfile.write("(" + elem[0] + ") " + elem[1] + "\r")
    print("(" + elem[0] + ") " + elem[1])

print("Total: " + str(len(results)))
