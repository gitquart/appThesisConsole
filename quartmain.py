# -*- coding: utf-8 -*-
"""
Spyder Editor

Useful conversions

1 million KB= 1 GB

"""

from readAndUploadThesis import cassandraBDProcess
from readAndUploadThesis import readUrl

print('Main program of Quart')
print('1.Start main program')
print('2. Get total rows from tbthesis per period table')
print('3. Count total rows from main table ')
query=input()
intquery=int(query)

if(intquery==1):   
    print('Write 1.Onwards 2. Backwards')
    sense=input()
    intsense=int(sense)
    print('Write Low limit -Zero if you do not know-')
    lowlim=input()
    intlow=int(lowlim)
    print('Write Top limit -Zero if you do not know-')
    toplim=input()
    inttop=int(toplim)
    res=readUrl(2,intsense,intlow,inttop)
else:
    cassandraBDProcess(intquery,'')

  
 
print("Main program is done")
    

