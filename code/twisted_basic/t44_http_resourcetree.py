'''http://www.114la.com/other/rgb.htm  颜色对照表'''
'''ff0000 红色'''
'''访问主页得到Color viewer连接'''
'''点击Color viewer进入localhost:8000/colors/'''
'''点击/colors/ff0000 进入localhost:8000/colors/ff0000页面，此页面显示六位十六进制数代表的颜色'''
'''访问localhost:8000/colors/六位十六进制数字   即可获得此代码代表的颜色'''
from twisted.web import resource, static, server


class ColorPage(resource.Resource):

    def __init__(self, color):

        self.color = color.decode()

    def render(self, request):
        return ('''
        <html>
        <head>
            <title>Color:%s</title>
            <link type='text/css' href='/styles.css' rel='Stylesheet'/>
        </head>
        <body style='background-color: #%s'>
            <h1>This is #%s.</h1>
            <p style='background-color: red'>
            <a href='/colors'>Back</a>
            </p>
        </body>
        </html>
        ''' % (self.color, self.color, self.color)).encode()


class ColorRoot(resource.Resource):

    def __init__(self):
        resource.Resource.__init__(self)
        self.requestedColors=[]
        self.putChild(b'', ColorIndexPage(self.requestedColors))

    def render(self, request):
        #  将url里的/colors 重定向到/colors/
        request.redirect((request.path.decode() + '/').encode())
        return b'please use /colors/ instead.'

    def getChild(self, path, request):
        # print(self.requestedColors)
        if path not in self.requestedColors:
            self.requestedColors.append(path.decode())
        return ColorPage(path)


class ColorIndexPage(resource.Resource):
    def __init__(self, requestColorList):
        resource.Resource.__init__(self)
        self.requestedColors = requestColorList

    def render(self, request):
        request.write(b'''
        <html>
        <head>
            <title>Colors</title>
            <link type='text/css' href='/styles.css' rel='Stylesheet'/>
        </head>
        <body>
        <h1>Colors</h1>
        To see a color, enter a url like
        <a href='/colors/ff0000'>/colors/ff0000</a>.<br/>
        Colors viewed so far:
        <ul>''')

        for color in self.requestedColors:
            request.write(("<li><a href='/blog/%s' style='color: #%s'>%s</a></li>" % (color, color, color)).encode())

        request.write(b'''
        </ul>
        </body>
        </html>
        ''')

        return b""

class HomePage(resource.Resource):
    def render(self, request):
        return b'''
        <html>
        <head>
            <title>Colors</title>
            <link type='text/css' href='/styles.css' rel='Stylesheet'>
        </head>
        <body>
        <h1>Colors Demo</h1>
        what's here:
        <ul>
            <li><a href='/colors'>Color viewer</a></li>
        </ul>
        </body>
        </html>
        '''


if __name__ == '__main__':
    from twisted.internet import reactor
    root = resource.Resource()
    root.putChild(b'', HomePage())
    root.putChild(b'colors', ColorRoot())
    root.putChild(b'styles.css', static.File('./css/styles.css'))

    site = server.Site(root)

    reactor.listenTCP(8005, site)
    reactor.run()