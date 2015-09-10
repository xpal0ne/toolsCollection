# coding: utf-8
__author__ = 'xP'
import os
from xml.etree import ElementTree as ET

def file_searcher(path):
    fList = []
    for rt, dirs, files in os.walk(path):
        for i in files:
            if 'saf'in i and 'client' in i and i.endswith('xml'):
                fList.append(rt+os.sep+i)
                print(rt+os.sep+i)
    return fList

def xml_analyze(file_list):
    interface_list = []
    for i in file_list:
        try:
            tree = ET.parse(i)
            root = tree.getroot()
            for childroot in root:
                if 'reference' in childroot.tag:
                        interface_list.append(childroot.attrib)
        except Exception, e:
            print('解析文件出错：' + i)
    return interface_list

def interface_handle(interface):
    for key, value in interface:
        if '{' in value:

    return interface

def conf_analyze(interface):
    pass
if __name__ == '__main__':
    flist = file_searcher('c:\\Users\\xP\\workspace\\dropship_trunk\\vc_dropship_service\\src\\main\\resources\\')
    print(xml_analyze(flist))

