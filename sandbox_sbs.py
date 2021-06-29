from lxml import etree
import os

sandboxfiles = r'C:\Users\nicho\Documents\GitHub\SE-GPSMapping'

for subdir, dirs, files in os.walk(sandboxfiles):

    for filename in files:
        filepath = subdir + os.sep + filename
        if filepath.endswith(".sbs"):
            doc = etree.parse(filepath)
            for att in doc.xpath('//MyObjectBuilder_CubeBlock'):
                for subtype in att.iter():
                    if subtype.tag == 'BuiltBy':
                        #print(subtype.text)
                        builtby = subtype.text
                    if subtype.tag == 'SubtypeName':
                        #print(subtype.text)
                        compname = subtype.text
                    if subtype.tag == 'Amount':
                        #print(subtype.text)
                        amount = subtype.text
                    try:
                        print(f'Built By: {builtby}\nComponent Name: {compname}\nAmount: {amount}')
                    except:
                        negative = 0
