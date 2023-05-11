import os
import sys
import glob

def count_lines(file_path):
    with open(file_path, 'r') as f:
        return sum(1 for line in f if line.strip() and not line.strip().startswith('//'))

def count_sloc(directory):
    sloc = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.js') or file.endswith('.jsx'):
                file_path = os.path.join(root, file)
                sloc += count_lines(file_path)
    return sloc

def count_js_files(directory):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".js") or file.endswith('.jsx'):
                count += 1
    return count

args = sys.argv
directory = 'testRepo/' + args[1]
num_files = count_js_files(directory)
sloc = count_sloc(directory)
print(f'Total number of files in {directory}: {num_files}')
print(f'Total number of lines of code in {directory}:  {sloc}')


def count_sloc_in_test_files(directory):
    test_files = glob.glob(os.path.join(directory, '**/*test.js'), recursive=True)
    total = 0
    for file in test_files:
        if 'node_modules' not in file and 'dist' not in file:
            sloc = count_lines(file)
            total += sloc

            print(file)
    return total

testFilesRsult = count_sloc_in_test_files('testRepo/')

print(f'Total number of lines of code in files with "test" in the filename:  {testFilesRsult}')