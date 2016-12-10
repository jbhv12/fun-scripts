import re
import sys,time,datetime
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
count=0
tottime=[]
lines = [line.rstrip('\n').translate(non_bmp_map) for line in open('/Users/jbhv12/Downloads/ws.txt', encoding='utf-8')]
nlines=[]
for line in lines:
    if(len(line)==0):continue
    if(not line[0].isdigit()):continue
    ll=line.split(' -')
    #print(ll[0], 'f')
    ll[0]=time.mktime(datetime.datetime.strptime(ll[0], "%d/%m/%Y, %I:%M %p").timetuple()) #should've used regex
    #print(ll)
    nlines.append(ll)

print(nlines)

for i in range(len(nlines)):
    if(nlines[i][1].split(':')[0][1:] == 'Cheny' and nlines[i-1][1].split(':')[0][1:]== 'Jay Bhavsar'):  #again should've used regex
        count+=1
        tottime.append((nlines[i][0]-nlines[i-1][0]))
        #print('blah')

print(count, tottime)
print(sum(tottime)/count)
