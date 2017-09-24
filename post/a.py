import os
import sys
import pdb
#pdb.set_trace()
def func(n):
	f=open(n,'r')
	s=f.read()
	f.close()
	f=open(n,'w')
	x=s.split('\n')
	x.insert(0,'---')
	x.insert(4,'---')
	x[1]='title: "'+x[1][7:]
	x[1]+='"'
	x[2]='tags: ['+x[2][6:]
	x[2]+=']'
	s1=x[3].split('-')
	if (len(s1[1])==1): s1[1]='0'+s1[1]
	if (len(s1[2])==1): s1[2]='0'+s1[2]
	x[3]='-'.join(s1)
	x[3]='d'+x[3][1:]+'T10:02:43Z'
	x[7]=''
	f.write('\n'.join(x))
	f.close()
for a,b,c in os.walk('./'):
	for n in c:
		if (n.endswith('.md')):
			func(n)