import csv
import re
import os
import random

TAG_RE = re.compile(r'<[^>]+>')
SO_rule = "(OSVDB|NVD|CVE|XXE|security|cross-site|brute force|injection|denial of service|DOS|Heap buffer overflow|Integer division by zero|Undefined behavior|Heap OOB write|Division by zero|Crashes the Python interpreter|Heap overflow|Uninitialized memory accesses|Heap OOB access|Heap underflow|Heap OOB|Heap OOB read|Segmentation faults|Segmentation fault|seg fault|Buffer overflow|Null pointer dereference|FPE runtime|segfaults|segfault)"
bug_rule = "(bug|Bug|Fix|fix|fixed|Fixed|Wrong|wrong|Error|error|nan|inf|Issue|issue|defect|Defect|Fault|fault|fail|Failed|Failing|failing|crash|crashed|Crash|Crashed)"

def loadFile():
    for root, dir, files in os.walk('./SO filtered bugs'):
        for file in files:
            rows = []
            current_file = os.path.join(root, file)
            with open(current_file, mode='r') as f:
                csv_reader = csv.DictReader(f)
                for row in csv_reader:
                    header = []
                    rows.append(row)
                    for k, v in row.items():
                        header.append(k)

            if len(rows) >= 500:
                selected = random.sample(rows, 500)
            else:
                selected = rows
            if not os.path.exists('./SO random'):
                os.makedirs('./SO random')
            with open('./SO random/'+file, 'w') as f:
                wr = csv.DictWriter(f, fieldnames=header)
                wr.writeheader()
                for item in selected:
                    wr.writerow(item)

        
def main():
    loadFile()

if __name__ == '__main__':
    main()