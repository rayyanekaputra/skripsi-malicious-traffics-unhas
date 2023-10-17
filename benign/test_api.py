from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts

client = Client(url = "https://10.163.10.244/xmlrpc.php", username = "resephariankamu",password="LiG5hqDiMNCacSa")
posts = client.call(posts.GetPosts())
# posts == [WordPressPost, WordPressPost, ...]
