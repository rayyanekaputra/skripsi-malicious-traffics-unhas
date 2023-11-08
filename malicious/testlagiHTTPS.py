
import sys
sys.path.extend(['/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/benign/register',
                 '/home/expresidentz/Desktop/skripsi-malicious-traffics-unhas/'])


import http.client
import xmlrpc.client
from ProxyTest import ProxyTester

class ProxiedTransport(xmlrpc.client.Transport):

    def set_proxy(self, host, port=None, headers=None, secure=False):
        self.proxy = host, port
        self.proxy_headers = headers
        self.secure = secure

    def make_connection(self, host):
        if self.secure:
            connection = http.client.HTTPSConnection(*self.proxy)
        else:
            connection = http.client.HTTPConnection(*self.proxy)
        connection.set_tunnel(host, headers=self.proxy_headers)
        self._connection = host, connection
        return connection

proxy_complete = ProxyTester().split(":")
proxy_ip, proxy_port = proxy_complete
print(proxy_ip, proxy_port)

transport = ProxiedTransport()
transport.set_proxy(proxy_ip, proxy_port,secure= True)
