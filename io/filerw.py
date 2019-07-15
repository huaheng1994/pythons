import os

fp = open('huaheng.csv', 'w')
fp.write('lhh,26,n')
fp.close()


fp = open('huaheng.csv')
data = fp.read()
print(data)
fp.close()
