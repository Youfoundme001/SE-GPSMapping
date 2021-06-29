import xmltodict
from collections import OrderedDict

with open('SANDBOX_0_0_0_.sbs') as fd:
    doc = xmltodict.parse(fd.read())

base = doc['MyObjectBuilder_Sector']['SectorObjects']['MyObjectBuilder_EntityBase']['CubeBlocks']['MyObjectBuilder_CubeBlock']


for item in base:
    if 'Cargo' in item['@xsi:type']:
        for attribute in item:
            print(attribute['@xsi:type'])
    #print(item['@xsi:type'])

# def recursive_items(dictionary):
#     for key, value in dictionary.items():
#         if type(value) is dict:
#             yield from recursive_items(value)
#         else:
#             yield (key, value)

# for key, value in recursive_items(doc):
#     print(key, value)

#print(doc[MyObjectBuilder_Sector])