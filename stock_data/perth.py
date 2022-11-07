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

error_list = []
list_info = []

for filename in list_japan_data_xml:
    try:
        tree = ET.parse('./japan_data/' + filename)
        root = tree.getroot()
        list_tag = []
        for child in root:
            if '{http://nlftp.mlit.go.jp/ksj/schemas/ksj-app}TourismResource_Point' == child.tag:
                list_info_tmp = [x.text for x in child]
                list_info.append(list_info_tmp)

    except:
        print('Error')
        error_list.append(filename)

print('error_list : ', error_list)
df = pd.DataFrame(list_info)
df.to_csv('sample.csv')
                    
        # print(child.tag)
        # print('child#tag#########')
        # print(child.attrib)