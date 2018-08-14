# coding=utf-8
import io
import yagmail
import sys
reload(sys)


yag = yagmail.SMTP("287833745@qq.com","pmrpbeudthhgbgei" ,"smtp.qq.com", 465)

contents =io.open("C:\\Tester\\case.txt",encoding="utf-8").read()

yag.send(["287833745@qq.com","koukou890@qq.com","1224269915@qq.com"],"測試一下Python發送郵件",contents)