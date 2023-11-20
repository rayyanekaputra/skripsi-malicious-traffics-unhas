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
sys.path.extend(['/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/register',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/'])


#MODULES
from EmailMaker import NamesPickRandom
from PasswordMaker import PasswordPickRandom
from ProxyTest import ProxyTester

# proxy = ProxyTester()
"""
For BruteForce testing purpose with XML-RPC
"""


import http.client
import xmlrpc.client

class ProxiedTransport(xmlrpc.client.Transport):

    def set_proxy(self, host, port=None, headers=None, secure=False):
        self.proxy = host, port
        self.proxy_headers = headers
        self.secure = secure

    def make_connection(self, host):
        if self.secure:
            connection = http.client.HTTPSConnection(*self.proxy)
            # Jika Self-Signed SSL dan skip warning
            context = ssl.create_default_context()
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

        else:
            connection = http.client.HTTPConnection(*self.proxy)
        connection.set_tunnel(host, headers=self.proxy_headers)
        self._connection = host, connection
        return connection

# server = xmlrpc.client.ServerProxy('http://betty.userland.com', transport=transport)
while True:
    proxy_complete = ProxyTester().split(":")
    proxy_ip, proxy_port = proxy_complete
    proxy_port = int(proxy_port)
    print(proxy_ip, proxy_port)

    transport = ProxiedTransport()
    transport.set_proxy(proxy_ip, proxy_port, secure=True)
    client = Client(url = "https://103.185.193.35/xmlrpc.php", username = "resephariankamu",password="LiG5hqDiMNCacSa", transport=transport)

    try:
        post = WordPressPost()
        post.title = 'test nov 10'
        post.content = 'ADAKAH RAYYAN DI HAATIMU'
        post.id = client.call(posts.NewPost(post))
        post.post_status = "publish"
        print("POSTINGAN BERHASIL DIPOST")
        break
    except:
        print("NDA BISA WORDPRESSNYA")

# try:
#     client.call(posts.EditPost(post.id, post))
#     success = 1
# except InvalidCredentialsError:
#     success = 0
#     print("incorrect username or password")

