# client.downloadPage()下载网页到临时文件并打印网页内容

from twisted.web import client
import tempfile # 创建临时文件临时工作路径的模块

def returnFilename(result, filename):
    return filename


def downloadToTempFile(url):
    '''
    传递一个URL，并返回一个Deferred对象用于下载完成时的回调
    '''
    filenum, tempfilename = tempfile.mkstemp()
    # 返回示例(6, '/var/folders/6y/kjgmpy6n1kl93r4tykvrcj1h0000gn/T/tmpkb_srsl5')
    # print(tempfilename)
    os.close(filenum)

    return client.downloadPage(url, tempfilename).addCallback(returnFilename, tempfilename)
    # 这一行实现了返回Deferred对象，并且将returnFilename作为其回调，临时文件名为附加参数。
    # 这就是说，当downloadToTempFile返回时，reactor将会调用returnFileName作为downloadTempFile的首个参数
    # 文件名作为第二个参数

if __name__ == '__main__':
    import sys, os
    from twisted.internet import reactor

    def printFile(filename):
        for line in open(filename, 'r+b').readlines():
            sys.stdout.write(line.decode())  # write() argument must be str, not bytes
        os.unlink(filename)  #删除文件

        reactor.stop()

    def printError(failure):
        print('>>>', sys.stderr, 'Error:', failure.getErrorMessage())
        reactor.stop()

    url = 'http://www.baidu.com'
    downloadToTempFile(url.encode()).addCallback(printFile).addErrback(printError)

    reactor.run()
