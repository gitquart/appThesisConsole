# -*- coding: utf-8 -*-
"""
Spyder Editor

Useful conversions

1 million KB= 1 GB

"""

from readAndUploadThesis import readUrl
from readAndUploadThesis import checkRows
from readAndUploadThesis import checkRowsInReal
from readAndUploadThesis import updateRows

print('Main program of Quart')
print('Want to know the total of rows? 1.Yes, 2. No, 3.Update Rows')
query=input()
intquery=int(query)

if(intquery==2):
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
if(intquery==1):
    print('Do you want to read tbthesis or tbthesis per period? 1 OR 2 respect...')
    query=input()
    intquery=int(query)
    if (intquery==1):
        checkRowsInReal()
    else:       
	    checkRows()
if(intquery==3):
    updateRows()     
 
  
print("Main program is done")
    

