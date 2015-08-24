# coding: utf-8
__author__ = 'xP'
from jenkins import Jenkins

jenkins_object = Jenkins('http://127.0.0.1:8080')
print(jenkins_object.get_info())
