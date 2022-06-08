import fileinput

#def print_report_information(filename):
filename=input()
firstCLB = 0 # we only want the first luts line
firstBlock=0
firstBlockLine=0
linecount =0
DSPexists=0
RegExists=0
with open(filename) as myFile:
        #with open(outputfile, 'w') as file:
            for num, line in enumerate(myFile, 1):
                linecount =linecount +1
                
                if line[:-1].__contains__('| CLB LUTs '): #or 'LUT2'or 'LUT3'or 'LUT3'or 'LUT4'or 'LUT5'or 'LUT6'):
                    if(firstCLB ==0):
                        tokens=line[:-1].split("|")
                        #print('CLBs\t\t\t\t\t\t'+tokens[2])
                        print(tokens[2])
                        firstCLB =linecount; #start from here   
                if linecount == firstCLB+1:
                    if line[:-1].__contains__(' LUT as Logic '):
                        tokens=line[:-1].split("|")
                        print(tokens[2])
                        #print('LUT as Logic\t\t'+tokens[2])
                if linecount == firstCLB+2:
                    if line[:-1].__contains__(' LUT as Memory '):
                        tokens=line[:-1].split("|")
                        print(tokens[2])
                        #print('LUT as Memory\t\t'+tokens[2])
                if line[:-1].__contains__(' Block RAM Tile '):
                    if firstBlockLine ==0:
                        tokens=line[:-1].split("|")
                        print(tokens[2])
                        #print('Block RAM Tiles\t'+tokens[2])
                        firstBlockLine=1
                if firstBlockLine ==1:
                    if line[:-1].__contains__('RAMB36/FIFO* '):
                        tokens=line[:-1].split("|")
                        #print('RAMB36\t\t\t\t'+tokens[2])
                        print(tokens[2])
                        firstBlockLine=firstBlockLine+1
                if firstBlockLine ==2:  
                    if line[:-1].__contains__('   RAMB18  '):
                        tokens=line[:-1].split("|")
                        #print('RAM18\t\t\t\t\t'+tokens[2])
                        print(tokens[2])
                        firstBlockLine=firstBlockLine+1
                if line[:-1].__contains__(' DSPs  '):
                    tokens=line[:-1].split("|")
                    DSPexists=DSPexists+1
                    if DSPexists == 1:
                        #print('DSPs\t\t\t\t\t'+tokens[2])
                        print(tokens[2])
                if line[:-1].__contains__('CLB Registers'):
                    tokens=line[:-1].split("|")
                    RegExists=RegExists+1
                    if RegExists ==1:
                        if line[:-1].__contains__('CLB Registers'):
                            tokens=line[:-1].split("|")
                            print(tokens[2])
                            #print('CLB Registers\t\t'+tokens[2])
                if line[:-1].__contains__('LUT6'):
                    tokens=line[:-1].split("|")
                    print(tokens[2])
                    #print('LUT6\t\t\t\t\t\t'+tokens[2])
                if line[:-1].__contains__('LUT5'):
                    tokens=line[:-1].split("|")
                    print(tokens[2])
                    #print('LUT5\t\t\t\t\t\t'+tokens[2])
                if line[:-1].__contains__('LUT4'):
                    tokens=line[:-1].split("|")
                    print(tokens[2])
                    print(LUT3)
                    #print('LUT4\t\t\t\t\t\t'+tokens[2])
                    #print('LUT3\t\t\t\t\t\t'+LUT3)
                if line[:-1].__contains__('LUT3'):
                    tokens=line[:-1].split("|")
                    LUT3 =tokens[2]                                
                if line[:-1].__contains__('LUT2'):
                    tokens=line[:-1].split("|")
                    print(tokens[2])
                    #print('LUT2\t\t\t\t\t\t'+tokens[2])
