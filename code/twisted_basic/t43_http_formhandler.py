# 访问主页，主页提供一个需要输入姓名、选择颜色、选择冰激凌的表单
# 用户在浏览器上点击提交后，服务器上返回用户的选择信息到浏览器
from twisted.web import http


def renderHomePage(request):
    '''主页信息'''
    colors=['red', 'blue', 'green']
    flavors=['vanilla', 'chocolate', 'strawberry', 'coffee']
    request.write('''
    <html>
    <head>
        <title>表单测试</title>
    </head>
    <body>
        <form action="posthandler" method="POST">
            Your Name:
            <p>
                <input type="text" name="name">
            </p>
            你最喜欢的颜色？
            <p>
    '''.encode('gbk'))

    for color in colors:
        request.write(
            ("<input type='radio' name='color' value='%s'>%s<br/>" % (color, color.capitalize())).encode())

    request.write('''
    </p>
    你喜欢哪种冰激凌？
    <p>
    '''.encode('gbk'))

    for flavor in flavors:
        request.write(
            ("<input type='checkbox' name='flavor' value='%s'>%s<br/>" % (flavor, flavor.capitalize())).encode())

    request.write('''
            </p>
        <input type='submit'>
    </form>
</body>
</html>
    '''.encode())

    request.finish()


def handlePost(request):
    '''提交后返回用户填写和选择的信息'''
    request.write('''
    <html><head><title>Posted Form Data</title>
        </head>
        <body>
        <h1>Form Data</h1>
    '''.encode())

    for key, values in request.args.items():
        # print(type(request.args))  request.args是一个字典类型数据
        # request.args里包含所有HTTP POST提交的URI查询字段值，里面的键值数据类型是bytes
        request.write(('<h2>%s</h2>' % key.decode()).encode())
        request.write('<ul>'.encode())

        for value in values:
            request.write(('<li>%s</li>' % value.decode()).encode())

        request.write('</ul>'.encode())

    request.write('''
        </body></html>
    '''.encode())

    request.finish()

class FunctionHandleRequest(http.Request):

    pageHandlers = {
        '/': renderHomePage,
        '/posthandler': handlePost
    }  # 该字典为路径映射，不同路径不同事件处理

    def process(self):  # 重载方法，查找并匹配路径
        self.setHeader(b'Content-Type', b'text/html')
        if self.path.decode() in self.pageHandlers:
            handler = self.pageHandlers[self.path.decode()]
            handler(self) # 调用相应的自定义事件处理器
        else:
            self.setResponseCode(http.NOT_FOUND)
            self.write(b'<h1>Not Found</h1>Sorry, no such page.')
            self.finish()


class MyHttp(http.HTTPChannel):
    requestFactory = FunctionHandleRequest


class MyHttpFactory(http.HTTPFactory):
    protocol = MyHttp


if __name__ == '__main__':
    from twisted.internet import reactor
    reactor.listenTCP(8000, MyHttpFactory())
    reactor.run()