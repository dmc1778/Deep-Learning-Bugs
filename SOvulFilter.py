import csv
import re
import os, json
label = {'secure': 0,'Integer division by zero': 0,'exposing': 0, 'endless loop': 0,'denial of service': 0, 'expose': 0 ,'DOS': 0, 'XXE':0, 'remote code execution':0, 'bopen': 0,  'redirect': 0, 'OSVDB': 0, 'bvuln': 0, 'CVE': 0, 'XSS': 0, 'ReDoS': 0, 'NVD': 0, 'malicious': 0, 'x-frame-options': 0, 'attack': 0, 'cross-site': 0, 'exploit': 0, 'directory': 0, 'traversal': 0, 'RCE': 0, 'XSRF': 0, 'clickjack': 0, 'session-fixation': 0,  'hijack': 0, 'advisory': 0, 'insecure': 0, 'security': 0, 'cross-origin': 0, 'unauthorized': 0, 'infinite loop': 0, 'brute force': 0, 'bypass': 0, 'constant time': 0, 'crack': 0, 'credential': 0, 'exposure': 0, 'hack': 0, 'harden': 0, 'injection': 0, 'lockout': 0, 'overflow': 0, 'password': 0, 'PoC': 0, 'proof of concept': 0, 'priveale': 0, 'insecurity': 0, 'Heap buffer overflow': 0, 'Integer': 0, 'division by zero': 0, 'Undefined behavior': 0, 'Heap OOB write': 0, 'Division by zero': 0, 'Crashes the Python interpreter': 0, 'Heap overflow': 0, 'Uninitialized memory accesses': 0, 'Heap OOB access': 0, 'Heap underflow': 0, 'Heap OOB': 0, 'Heap OOB read': 0, 'Segmentation faults': 0, 'Segmentation fault': 0, 'seg fault': 0, 'Buffer overflow': 0, 'Null pointer dereference': 0, 'FPE runtime': 0, 'segfaults': 0, 'segfault': 0, 'attack': 0, 'authenticate': 0, 'authentication': 0, 'check': 0, 'click': 0, 'jack': 0, 'compromise': 0, 'constant-time': 0, 'corrupt': 0, 'crack': 0, 'craft': 0, 'credential': 0, 'cross-Site Request Forgery': 0, 'CVE-': 0, 'Dan Rosenberg': 0, 'deadlock': 0, 'deep recursion': 0, 'denial-of-service': 0, 'directory': 0, 'traversal': 0, 'disclosure': 0, 'divide by 0': 0, 'divide by zero': 0, 'divide-by-zero': 0, 'division by zero': 0, 'division by 0': 0, 'division-by-zero': 0, 'division-by-0': 0, 'double free': 0, 'endless': 0, 'loop': 0, 'exhaust': 0, 'dos': 0, 'fail': 0, 'fixes': 0, 'CVE-': 0, 'forgery': 0, 'fuzz': 0, 'general protection': 0, 'fault': 0, 'GPF': 0, 'grsecurity': 0, 'guard': 0, 'leak': 0, 'initialize': 0, 'insecure': 0, 'invalid': 0, 'KASAN': 0, 'info leak': 0, 'limit': 0, 'lockout': 0, 'long loop': 0, 'loop': 0, 'man in the middle': 0, 'man-in-the-middle': 0, 'mishandle': 0, 'MITM': 0, 'negative': 0, 'null deref': 0, 'null-deref': 0, 'NULL dereference': 0, 'null function pointer': 0, 'null pointer dereference': 0, 'null-ptr': 0, 'null-ptr-deref': 0, 'off-by-one': 0, 'OOB': 0, 'oops': 0, 'open redirect': 0, 'oss-security': 0, 'out of array': 0, 'out of bound': 0, 'out-of-bound': 0, 'overflow': 0, 'overread': 0, 'override': 0, 'overrun': 0, 'panic': 0, 'password': 0, 'poison': 0, 'prevent': 0, 'privesc': 0, 'privilege': 0, 'protect': 0, 'race': 0, 'race condition': 0, 'RCE': 0, 'remote code execution': 0, 'replay': 0, 'sanity check': 0, 'sanity-check': 0, 'security': 0, 'security fix': 0, 'security issue': 0, 'security problem': 0, 'session fixation': 0, 'snprintf': 0, 'spoof': 0, 'syzkaller': 0, 'trinity': 0, 'unauthorized': 0, 'undefined behavior': 0, 'underflow': 0, 'unexpected': 0, 'uninitialize': 0, 'unrealize': 0, 'use after free': 0, 'use-after-free': 0, 'valid': 0, 'verification': 0, 'verifies': 0, 'verify': 0, 'violate': 0, 'violation': 0, 'vsecurity': 0, 'vuln': 0, 'vulnerab': 0, 'XML External Entity': 0}

TAG_RE = re.compile(r'<[^>]+>')
SO_rule = "(OSVDB|NVD|CVE|XXE|security|cross-site|brute force|injection|denial of service|DOS|Heap buffer overflow|Integer division by zero|Undefined behavior|Heap OOB write|Division by zero|Crashes the Python interpreter|Heap overflow|Uninitialized memory accesses|Heap OOB access|Heap underflow|Heap OOB|Heap OOB read|Segmentation faults|Segmentation fault|seg fault|Buffer overflow|Null pointer dereference|FPE runtime|segfaults|segfault)"
bug_rule = "(bug|Bug|Fix|fix|fixed|Fixed|Wrong|wrong|Error|error|nan|inf|Issue|issue|defect|Defect|Fault|fault|fail|Failed|Failing|failing|crash|crashed|Crash|Crashed)"
crazy_rule = "(denial of service|DOS|XXE|remote code execution|bopen redirect|OSVDB|bvuln|CVE|XSS|ReDoS|NVD|malicious|x−frame−options|attack|cross-site|exploit|directory traversal|RCE|XSRF|clickjack|session-fixation|hijack|advisory|insecure|security|cross-origin|unauthori[z|s]ed|infinite.loop|brute force|bypass|constant time|crack|credential|expos(e|ing|ure)|hack|harden|injection|lockout|overflow|password|PoC|proof of concept|priveale|(in)?secur(e|ity)|Heap buffer overflow|Integer division by zero|Undefined behavior|Heap OOB write|Division by zero|Crashes the Python interpreter|Heap overflow|Uninitialized memory accesses|Heap OOB access|Heap underflow|Heap OOB|Heap OOB read|Segmentation faults|Segmentation fault|seg fault|Buffer overflow|Null pointer dereference|FPE runtime|segfaults|segfault|attack|authenticate|authentication|checkclickjack|compromise|constant-time|corrupt|crack|craft|credential|cross Site Request Forgery|cross-Site Request Forgery|CVE-|Dan Rosenberg|deadlock|deep recursion|denial-of-service|directory traversal|disclosure|divide by 0|divide by zero|divide-by-zero|division by zero|division by 0|division-by-zero|division-by-0|double free|endless loop|exhaust|dos|fail|fixes CVE-|forgery|fuzz|general protection fault|GPF|grsecurity|guard|leak|initialize|insecure|invalid|KASAN|info leak|limit|lockout|long loop|man in the middle|man-in-the-middle|mishandle|MITM|negative|null deref|null-deref|NULL dereference|null function pointer|null pointer dereference|null-ptr|null-ptr-deref|off-by-one|OOB|oops|open redirect|oss-security|out of array|out of bound|out-of-bound|overflow|overread|override|overrun|panic|password|poison|prevent|privesc|privilege|protect|race|race condition|RCE|remote code execution|replay|sanity check|sanity-check|security|security fix|security issue|security problem|session fixation|snprintf|spoof|syzkaller|trinity|unauthorized|undefined behavior|underflow|unexpected|uninitialize|unrealize|use after free|use-after-free|valid|verification|verifies|verify|violate|violation|vsecurity|vuln|vulnerab|XML External Entity)"

def loadFile():
    for root, dir, files in os.walk('./SO query results'):
        for file in files:
            print(file)
            rows = []
            current_file = os.path.join(root, file)
            with open(current_file, mode='r', encoding='utf-8', errors='ignore') as f:
                csv_reader = csv.reader(f, delimiter = ',')
                counter = 0
                for row in csv_reader:
                    header = []
                    # for k, v in row.items():
                    #     header.append(k)        
                    # row['Body'] = TAG_RE.sub('', row['Body'])
                    # row['Body'] = row['Body'].strip('\n')
                    b = re.findall(crazy_rule, row[8])
                    if b:
                        try:
                            for j in range(len(b)):
                                label[b[j][0]] += 1
                        except ValueError:
                            print('Key not found!')
                        if re.search(r'(how to|How to|What is|what is|does|Does|do|Do|where|Where|How|how|what|What|is|Is)', row[8]):
                            print('Found')
                        else:
                            rows.append([row[0], row[8]])

            if not os.path.exists('./SO filtered vul'):
                os.makedirs('./SO filtered vul')
            with open('./SO filtered vul/'+file, 'w', encoding='utf-8') as f:
                wr = csv.writer(f, delimiter=',')
                #for item in rows:
                wr.writerows(rows)
            # with open('./SO filtered vul/'+file, 'w') as f:
            #     wr = csv.DictWriter(f, fieldnames=header)
            #     wr.writeheader()
            #     for item in rows:
            #         wr.writerow(item)
            file = file.replace('.csv', '')
            with open('SO_keyword_mapping_'+file+'.json', 'w') as fp:
                json.dump(label, fp, indent=4)

        
def main():
    loadFile()

if __name__ == '__main__':
    main()