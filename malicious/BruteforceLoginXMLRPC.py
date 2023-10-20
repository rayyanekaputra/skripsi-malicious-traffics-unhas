from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#XMLRPC API from WORDPRESS
from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.exceptions import InvalidCredentialsError

#FIX SSL: https://stackoverflow.com/questions/48056116/ssl-issue-with-xmlrpc-using-python-and-wordpress
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#IMPORT FOLDER OF THE MODULES
import sys
sys.path.insert(0,'/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/register')

#MODULES
from EmailMaker import NamesPickRandom
from PasswordMaker import PasswordPickRandom

"""
For BruteForce testing purpose with XML-RPC
"""

client = Client(url = "https://10.163.10.244/xmlrpc.php", username = "resephariankamu",password="LiG5hqDiMNCacSa")

post = WordPressPost()
post.title = 'My post'
post.content = 'This is a wonderful blog post about XML-RPC.'
post.id = client.call(posts.NewPost(post))
post.post_status = "publish"

try:
    client.call(posts.EditPost(post.id, post))
    success = 1
except InvalidCredentialsError:
    success = 0
    print("incorrect username or password")

