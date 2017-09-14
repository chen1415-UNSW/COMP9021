#usage:
#solve.py in current dictionary, all test files in a3test dictionary
import sys
import os

directory = 'a3test'
if not os.path.exists(directory):
    print('There is no directory named {}, giving up...'.format(directory))
    sys.exit()
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    if 'out' in filename:
        continue
    print('running {}'.format(filename))
    os.system('echo {} | python3 solve.py >{}'.format(directory + '/' + filename, directory + '/' + filename.split('.')[0]+'_my_output.txt'))
    os.system('diff -b {} {}'.format(directory + '/' + filename.split('.')[0]+'_output.txt', directory + '/' + filename.split('.')[0]+'_my_output.txt'))

