# coding: utf-8
import requests
from PIL import Image
from bs4 import BeautifulSoup
class BUPTjwxt:
    def __init__(self):
        self.formdata = dict()
        self.logindata = dict()
        self.__webloginurl = 'http://jwxt.bupt.edu.cn/wengine-auth/login/'
        self.__jwxtloginurl = 'http://jwxt.bupt.edu.cn/'
        self.__session = requests.session()
        self.formdata['auth_type'] = 'local'
        self.formdata['username'] = '2016211350' #外网登陆学号
        self.formdata['password'] = '060375' #外网登陆密码
        self.formdata['sms_code'] = ''
        self.logindata['type'] = 'sso'
        self.logindata['zjh'] = '2016211350' #教务系统登陆学号
        self.logindata['mm'] = '123456aa' #教务系统登陆密码
        self.__headers = {
            'User-Agent'
                :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15',
            'Accpept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9'
          }

    def __jwxtlogin(self):
        try:
            with open('yanzhengma.jpeg', 'wb+') as img:
                img.write(self.__session.get('http://jwxt.bupt.edu.cn/validateCodeAction.do?random=').content)
            pic = Image.open('yanzhengma.jpeg')
            pic.show()
            yanzhengma = input("Input Captcha: ")
            self.logindata['v_yzm'] = yanzhengma
            r = self.__session.post('http://jwxt.bupt.edu.cn/jwLoginAction.do', data=self.logindata, headers=self.__headers)
            print(r.text)
        except Exception as e:
            print('jwxt Login Error: '+ str(e))

    def login(self):
        data = self.__session.get(self.__webloginurl, headers=self.__headers)
        soup = BeautifulSoup(data.content, 'html.parser')
        if len(soup.find_all(id='v_chart')) != 0:
            print('no yanzhengma')
        else:
            with open('weblogincaptcha.png','wb+') as captcha:
                captcha.write(self.__session.get('http://jwxt.bupt.edu.cn/wengine-auth/captcha/').content)
            pic1 = Image.open('weblogincaptcha.png')
            pic1.show()
            captcha1 = input("Input Captcha: ")
            self.formdata['captcha'] = captcha1
        t = self.__session.post(self.__webloginurl, data=self.formdata, headers=self.__headers)
        code = t.status_code
        data = self.__session.get(self.__jwxtloginurl, data=self.logindata, headers=self.__headers)
        soup = BeautifulSoup(data.content, 'html.parser')
        print(soup.title)
        if code == 200:
            print ('Web Login Success')
            self.__jwxtlogin()
        else:
            print('Web Login Fail, Error Code: ' + str(code))

wenhe = BUPTjwxt()
wenhe.login()
