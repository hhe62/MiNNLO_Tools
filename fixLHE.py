import sys,re,pdb

# file name should contain "pre" to indicate before fixing
fn = sys.argv[1]
fin = open(fn)
fout = open(fn.replace("pre",""),"w")
lstore = []
store = False
noEndLine = True
for line in fin:
    #search for pattern #---...--
  
    line2 = re.sub("^#-+$","#",line) #this keeps \n in the line as it is
    
    if "<event>" in line2:
        store = True
    
    if store:
        lstore.append(line2)
        
        #Don't write content in between event tags until seeing end tag 
        if "</event>" in line2:
            store = False
            for sl in lstore:
                fout.write(sl)
            lstore = []
            continue
    
    if not store:
        fout.write(line2)

    if "</LesHouchesEvents>" in line:
        noEndLine = False

    #skip comments after this line. If event tag not closed, then don't end yet
    if not store and "</LesHouchesEvents>" in line:
        sys.exit() 

# At the end of line, if event tags still not close or no endline due to other reason, write end line
if store or noEndLine:
    fout.write("</LesHouchesEvents>\n")