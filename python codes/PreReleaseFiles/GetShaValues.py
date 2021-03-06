'''
 Using the first GitHub api, we fetch the commit data and store just the sha values in a file for later use (2nd api)

'''

import requests
path='/home/pranav/Project/Eclipse2.1/PreReleaseFiles/'
# URL to be inserted as first paramenter. Since and until date : prev version to current version
l = requests.get('https://api.github.com/repos/eclipse/eclipse.jdt.core/commits', auth=('pranavrr93', 'project1'),params={'since':'2002-06-27T18:35:00-04:00','until':'2003-03-27T21:30:00-05:00'})
# l.json() returns multiple dict objects.
commit_data=l.json()
enter='\n'
id=1
f=open(path+'sha_pre.dat','w')
for x in commit_data:	
	print 'Sha value : {} written'.format(id)
	f.write(x['sha'])
	f.write(enter)
	id+=1
# Required due to pagination in GitHub. Need to get next page link and get all sha values.
import re
pat=re.compile(',|;')
#pat.split(l.headers['link'])
#this is how u iterate through all pages

while True:
	# If the next link is missing, l.headers['link'] won't have that attribute and hence length =2
	if len(pat.split(l.headers['link']))==2: break 
    	l=requests.get(pat.split(l.headers['link'])[0].strip('<>'),auth=('pranavrr93','project1'))
    	commit_data=l.json()
	for x in commit_data:	
		print 'Sha value : {} written'.format(id)
		f.write(x['sha'])
		f.write(enter)
		id+=1


