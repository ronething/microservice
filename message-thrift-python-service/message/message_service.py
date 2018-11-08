# coding=utf-8

from message.api import MessageService
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = "13414113153@163.com"
authCode = "PAs092M3FP2AOu0D"


class MessageServiceHandler:

    def sendMobileMessage(self, mobile, message):
        print "sendMobileMessage, mobile: " + mobile + ", message:" + message
        return True

    def sendEmailMessage(self, email, message):
        print "sendEmailMessage, email:" + email + ", message" + message
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj["From"] = sender
        messageObj["To"] = email
        messageObj["Subject"] = Header("docker+k8s", "utf-8")
        try:
            smtpObj = smtplib.SMTP("smtp.163.com")
            smtpObj.login(sender, authCode)
            smtpObj.sendmail(sender, [email], messageObj.as_string())
            print "send mail success"
        except smtplib.SMTPException, ex:
            print "send mail failed"
            print ex
            return False

        return True


if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket("127.0.0.1", "9090")
    tfactory = TTransport.TFramedTransportFactory()  # 帧传输方式
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()  # 传输协议

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "python thrift server start"
    server.serve()
    print "python thrift server exit"
