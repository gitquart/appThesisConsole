# -*- coding: utf-8 -*-
"""
Spyder Editor

Useful conversions

1 million KB= 1 GB

"""


import readAndUploadThesis as thesis

print('Main program of Quart')
print('1.Start main program')
print('3. Count total rows from main table ')
print('4. Delete some period')
print('5. Update')
print('6. Look for an ID in some period')
query=input()
intquery=int(query)

if intquery==1 or intquery==6:   
    print('Write 1.Onwards 2. Backwards')
    sense=input()
    intsense=int(sense)
    print('Write Low limit -Zero if you do not know-')
    lowlim=input()
    intlow=int(lowlim)
    print('Write Top limit -Zero if you do not know-')
    toplim=input()
    inttop=int(toplim)
    print('Tell me the period (number):')
    period=input()
    intperiod=int(period)
    if intquery==1:
        res=thesis.readUrl(intsense,intlow,inttop,intperiod)
    if intquery==6:
        thesis.getIDLimit(intsense,intlow,inttop,intperiod)
            
elif intquery==3 or intquery==4:
    print('Tell me the period (number):')
    period=input()
    intperiod=int(period)
    thesis.cassandraBDProcess(intquery,'',intperiod)   
else:
    thesis.cassandraBDProcess(intquery,'','')
        
 
print("Main program is done")
    

