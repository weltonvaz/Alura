# Python Library 
# -*- coding: UTF-8 -*-

import os

def create_directory(server_path, branch):
    if not os.path.exists(rserver_path):
        os.makedirs(rserver_path)
    os.makedirs(server_path + "/" + branch)
