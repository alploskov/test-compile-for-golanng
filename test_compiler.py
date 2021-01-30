import subprocess
import sys
import re


out = subprocess.getoutput(f'go build {sys.argv[1]}')
if re.search(r'\.\/.+\.go:\d+:\d+:\s.+\sdeclared but not used', out):
    errs = out.split('\n')[1:]

pos = []
for i in errs:
    if re.match(r'\.\/.+\.go:\d+:\d+:\s.+\sdeclared but not used', i):
        pos.append(re.search(r'\d+:\d+', i).group().split(':')[0])

print(pos)

test_file = open('test'+sys.argv[1], 'w+')
print(type(pos[0]))
for i, ii in enumerate(open(sys.argv[1], 'r')):
    if str(i+1) in pos:
        test_file.write('//'+ii)
    else:
        test_file.write(ii)
test_file.close()
subprocess.call(['go', 'build', '-o', sys.argv[1].replace('.go', ''),'test'+sys.argv[1]])
