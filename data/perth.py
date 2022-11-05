import os
import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET




list_japan_data = os.listdir('./japan_data')


list_japan_data_xml = []

for filename in list_japan_data:
    # print(filename)
    if '.xml' == os.path.splitext(filename)[1]:
        if 'KS-META' in filename:
            continue
        else:
            list_japan_data_xml.append(filename)


for filename in list_japan_data_xml:
    print(filename)
    tree = ET.parse('./japan_data/' + filename)
    root = tree.getroot()
    print('tag#########')
    print(root.tag)
    print('attr#########')
    print(root.attrib)
    print('#'*100)
    print(len(root))
    list_tag = []
    for child in root:
        if '{http://nlftp.mlit.go.jp/ksj/schemas/ksj-app}TourismResource_Point' == child.tag:
            print(child.attrib, child.attrib)
            for a in child:
                print(a.tag)
                break
                
        # print(child.tag)
        # print('child#tag#########')
        # print(child.attrib)
    break