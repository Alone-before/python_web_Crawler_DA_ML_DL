from twisted.web import http


class MyRequestHandler(http.Request):
    '''http.Request子类，重载了process方法'''
    pages = {
        '/': '<h1>Home</h1>Home Page',
        '/test': '<h1>Test</h1>Test Page',
        } # 此字典存放不同请求下的响应体内容

    def process(self):
        # print(self.path) # 可以打印尝试并和浏览器发送的地址做对比, self.path是bytes型哦，注意有些地方解码哦
        if self.path.decode() in self.pages: # 判断请求路径并发送相应的信息
            self.write(self.pages[self.path.decode()].encode())
        else: # 不存在的返回404并输出不存在信息
            self.setResponseCode(http.NOT_FOUND)  # 设置响应状态码
            self.write('<h1>Not Found</h1>Sorry, no such page.'.encode())
        self.finish() # 告知响应已完成


class MyHttp(http.HTTPChannel):
    '''继承http.HTTPCHannel类，这是一个Protocol，即用来处理每个成功的连接'''
    requestFactory = MyRequestHandler


class MyHttpFactory(http.HTTPFactory):
    '''继承http.HTTPFcatory类，这是一个ServerFactory，即用来管理http服务器连接'''
    protocol = MyHttp


if __name__ == '__main__':
    from twisted.internet import reactor
    reactor.listenTCP(8000, MyHttpFactory())

    reactor.run()