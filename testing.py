import sys
import os
import filecmp
import shell

#f1 executed
#f2 on git
def compareFiles(file1, file2):
    f1 = [line.replace('\n','') for line in open(file1).readlines()]
    f2 = [line.replace('\n','') for line in open(file2).readlines()]

    print(f1)
    print(f2)

    if len(f1) - 1 > len(f2):
        raise Exception("Some test is wrong: " + file2 + "\n" + f1 + " " + f2) 

    for i in range(len(f2)):
        if f1[i] != f2[i]:
            raise Exception("Some line failed: " + file2 + "\n" + f1[i] + " " + f2[i])

orig_stdout = sys.stdout
example_path = "examples/"

test_folders = list(filter(lambda x: len(x.split(".")) == 1, os.listdir('examples')))

for i in test_folders:
    f = open('out.txt', 'w')
    sys.stdout = f
    shell.main("run(" + example_path + i + "/code.pansy)")
    f.flush()
    compareFiles("out.txt", example_path + i +"/output.txt")
    f.close()
    
os.remove("out.txt")
sys.stdout = orig_stdout
