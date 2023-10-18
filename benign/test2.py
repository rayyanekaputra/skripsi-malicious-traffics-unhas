import xmlrpc.client
import ssl
url = 'https://12345/'

api = xmlrpc.client.ServerProxy(url,context=ssl._create_unverified_context())
print(api.system.listMethods())

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
