import sys
from twisted.internet import reactor
from twisted.internet.protocol import Protocol,Factory

#自定义协议（要继承Protocol超类）
class SimpleLogger(Protocol):
    def connectionMade(self):
        print('Got connection from',self.transport.client)

    def connectionLost(self):
        print(self.transport.client,'disconnected')

    def dataReceived(self,data):
        print(data)
        #sys.stdout.write(data)

#以下两行使用Factory类制造自定义协议的实例
fac = Factory()
fac.protocol = SimpleLogger

#指定监听端口
reactor.listenTCP(1234,fac)
#启动服务器
reactor.run()
