"""
读取文件里面的信息
"""
import os
import pandas as pd
path = './data/'

class Article:
    def __init__(self, title, content, time, author, url):
        self.title = title
        self.content = content
        self.time = time
        self.author = author
        self.url = url

    def getAllPerson(self):
        content = self.content
        name =
read