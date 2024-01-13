import os
import glob

freindName = "Deepesh"
count = 0
for filename in glob.glob('dataset/*.txt'):
    with open(filename, 'r') as f:
        content = f.read()
        count += 1
        if freindName in content:
            print(freindName + " is in " + filename)

print("Done")
print("Total files: " + str(count))