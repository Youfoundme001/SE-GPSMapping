from lxml import etree
import os

hangarfiles = r'C:\Users\nicho\Documents\GitHub\SE-GPSMapping'
lookup = ['Refinery', 'Assembler', 'ShipWelder', 'ShipGrinder']

hv = open('hv.txt', 'w')

#directory = r'C:\Users\nicho\Documents\GitHub\SE-GPSMapping'
#for filename in os.listdir(directory):
#    refcount = 0
#    asscount = 0
#    if filename.endswith('.sbc'):

for subdir, dirs, files in os.walk(hangarfiles):
    totalref = 0
    totalass = 0
    totalweld = 0
    totalgrind = 0
    for filename in files:
        filepath = subdir + os.sep + filename
        refcount = 0
        asscount = 0
        weldcount = 0
        grindcount = 0
        if filepath.endswith(".sbc"):
            doc = etree.parse(filepath)
            for att in doc.xpath('//MyObjectBuilder_CubeBlock'):
                for subtype in att.iter():
                    try:
                        if subtype.tag == 'SubtypeName':
                            for type in lookup:
                                if type in subtype.text:
                                    #print(subtype.tag)
                                    #print(subtype.attrib)
                                    #print(subtype.text)
                                    if type == 'Refinery':
                                        refcount += 1
                                    if type == 'Assembler':
                                        asscount += 1
                                    if type == 'ShipWelder':
                                        weldcount += 1
                                    if type == 'ShipGrinder':
                                        grindcount += 1
                                        #print(subtype.tag)
                                        #print(subtype.attrib)
                                        #print(subtype.text)
                                    
                    except:
                        negative = 0
            findsteamid = len(subdir)
            steamid = subdir[findsteamid -17 :]
            #if refcount > 0 or asscount > 0 or weldcount > 0:
                #print(steamid)
            totalref += refcount
            totalass += asscount
            totalweld += weldcount
            totalgrind += grindcount
    if totalref > 9 or totalass > 9 or totalweld > 9 or totalgrind > 9:
        hv.write('----------\n')
        hv.write(f'{steamid}: \n{totalref} Refineries\n{totalass} Assemblers \n{totalweld} Welders\n{totalgrind} Grinders\n')

hv.close()