import sys
import re
import pdb

fn = sys.argv[1]
fin = open(fn)
fout = open(fn+"formatted","w")

recH = False
ref = False
ids = []
idcount = 0
#Work on fixed LHE file
for line in fin:

    if "<initrwgt>" in line:
        recH = True
        fout.write(line)
        continue

    if recH:
        if "<weight id='" in line:
            id = line.split("<weight id='")[1].split("' > renscfact")[0]
            ids.append(id)
            fout.write(line)
            continue

        if "</initrwgt>" in line:
            fout.write(line)
            recH = False
            continue


    if "<weights>" in line:
        ref = True
        fout.write("<rwgt>\n")
        idcount = 0
        continue

    if ref:
        if "</weights>" in line:
            ref = False
            fout.write("</rwgt>\n")
            continue

        else:
            line = "<wgt id='{}'> ".format(ids[idcount])+line.strip()+" </wgt>\n"  
            idcount+=1
            fout.write(line)
            continue
    
    fout.write(line)