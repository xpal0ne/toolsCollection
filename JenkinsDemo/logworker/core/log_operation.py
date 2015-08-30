#coding: utf-8
__author__ = 'xP'

import commands
import os
import paramiko


class TestNode:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password

    def connect_node(self):
        node_connection = paramiko.SSHClient()
        node_connection.connect(self.host, port=22, username=self.username, password=self.password)
        return node_connection

    def get_log(self, app_name, control):
        log_path = "/export/Domains/%s/server1/logs/catalcat.out" % app_name
        command = 'tail %s -%s'%(log_path, control)
        # data = commands.getoutput(command)
        # data = os.popen(command)
        try:
            node = TestNode.connect_node(self)
            stdin, stdout,stderr = node.exec_command(command)
        except:
            stdout = 'Error connection'
        return stdout