#!/usr/bin/python
# -*-coding=UTF-8-*-
i=0
codes = [1,2,3,4,5]
for a in codes:
    for b in codes:
        for c in codes:
            if ( a != b ) and ( a != c )and( b != c ):
                i+=1
                print a,b,c
print i