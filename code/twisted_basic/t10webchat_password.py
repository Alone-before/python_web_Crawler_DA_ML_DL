# 提交表单的伪代码
from twisted.web import client, error as weberror
from twisted.internet import reactor
import sys, getpass, base64


def printPage(data):
    # print(data.decode())
    reactor.stop()


def checkHTTPError(failure, url):
    failure.trap(weberror.Error)

    if failure.value.status=='401':
        print('>>>', sys.stderr, failure.getErrorMessage())

        username = input('用户名：')
        password = getpass.getpass('密码：')
        basicAuth = base64.encodestring('%s:%s' % (username, password))
        authHeader = 'Basic' + basicAuth.strip()
        # 加入验证信息后，尝试再次获取页面，
        return client.getPage(url.encode(), headers={'Authorization':authHeader})
    else:
        return failure


def printError(failure):
    print('>>>', sys.stderr,'Error:', failure.getErrorMessage())
    reactor.stop()

if __name__ == '__main__':
    url = 'http://www.example.com/protected/page' # '一个需要登陆才能访问的页面'

    client.getPage(url.encode()).addErrback(
        checkHTTPError, url).addCallback(printPage).addErrback(printError)

    reactor.run()