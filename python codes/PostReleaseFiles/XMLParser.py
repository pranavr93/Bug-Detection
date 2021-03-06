'''
	This file takes an xml file as input and picks up all bug ids that were reported one year from date of release of current version.
'''
import xml.etree.ElementTree as et
import datetime as dt
from datetime import timedelta
path='/home/pranav/Project/Eclipse2.1/PostReleaseFiles/'
tree =et.parse(path+'show_bug2.1.xml')
root=tree.getroot()
date_of_rel='2003-03-27 21:30:00'
format = '%Y-%m-%d %H:%M:%S'
enter='\n'
space= ' '
date=dt.datetime.strptime(date_of_rel,format)
f=open(path+'bugz_time.dat','w')
for child in root:
	for neighbor in child.iter('creation_ts'):
		neighbor.text=neighbor.text[:19]
		temp=dt.datetime.strptime(neighbor.text,format)		
		if(temp-date<timedelta(days=365) and temp-date>timedelta(days=0)):
			for neighbor2 in child.iter('bug_id'):
				f.write(neighbor2.text) 
				f.write(space)
			#f.write(neighbor.text) 
			f.write(enter)


	
