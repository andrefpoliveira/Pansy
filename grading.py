import sys
import os
import filecmp
import shell
import json
from itertools import islice

#f1 executed
#f2 on git
def compareFiles(file1, file2):
    f1 = [line.replace('\n','') for line in open(file1).readlines()]
    f2 = [line.replace('\n','') for line in open(file2).readlines()]

    if len(f1) - 1 > len(f2):
        return False

    for i in range(len(f2)):
        if f1[i] != f2[i]:
            return False

    return True

orig_stdout = sys.stdout


codes_path = "Challenges/Challenge1/"

# Obtain pansy codes
codes = [f for f in os.listdir(codes_path) if os.path.isfile(os.path.join(codes_path, f)) and "pansy" in f]
results = {}

tests = json.loads(open(codes_path + "tests.json", "r").read())
resultsFile = open("Challenges/Challenge1/results.txt", "w")

for i in codes:
    name = i.split(".")[0]
    results[name] = {}
    results[name]['result'] = 0

    wrongs = {}

    for j in tests:
        f = open('out.txt', 'w')
        sys.stdout = f
        with open("result.pansy", "w") as file:
            file.write(f'imports("{codes_path + i}")\n')
            file.write(f'print(solution({tests[j]["input"]}))')

        with open("output.txt", "w") as file:
            file.write(str(tests[j]["output"]))

        shell.main('run("result.pansy")')
        f.flush()
        if compareFiles("out.txt", "output.txt"):
            results[name]['result'] += 1
        else:
            wrongs[j] = {}
            with open("out.txt", "r") as f:
                wrongs[j]['given'] = f.readline().strip()

            wrongs[j]['expected'] = tests[j]["output"]

        f.close()

    results[name]['wrongs'] = wrongs

    sys.stdout = resultsFile

    print(f"\n{name}: {results[name]['result']}\n")

    n_items = list(islice(wrongs, 3))

    if len(n_items) != 0:
        print("Wrong Answers:")
        for i in n_items:
            print(f"Test case: {i}")
            print(f"Expected Answer: {wrongs[i]['expected']}")
            print(f"Given Answer: {wrongs[i]['given']}")
            print()

    print("==============================================================================")

    os.remove("out.txt")
    os.remove("output.txt")
    os.remove("result.pansy")

        

