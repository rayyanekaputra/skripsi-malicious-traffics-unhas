from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost
from wordpress_xmlrpc.exceptions import InvalidCredentialsError
from selenium.common.exceptions import TimeoutException

#FIX SSL: https://stackoverflow.com/questions/48056116/ssl-issue-with-xmlrpc-using-python-and-wordpress
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



client = Client(url = "https://10.163.10.244/xmlrpc.php", username = "resepharisankamu",password="LiG5hqDiMNCacSa")

post = WordPressPost()
post.title = 'My post'
post.content = 'This is a wonderful blog post about XML-RPC.'
post.id = client.call(posts.NewPost(post))



# posts == [WordPressPost, WordPressPost, ...]
