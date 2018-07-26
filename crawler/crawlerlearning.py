# coding: utf-8
import requests, os
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
        self.formdata['username'] = '2016211350'  # 外网登陆学号
        self.formdata['password'] = '060375'  # 外网登陆密码
        self.formdata['sms_code'] = ''
        self.logindata['type'] = 'sso'
        self.logindata['zjh'] = '2016211350'  # 教务系统登陆学号
        self.logindata['mm'] = '123456aa'  # 教务系统登陆密码
        self.__headers = {
            'User-Agent'
                : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                  'Version/11.1.2 Safari/605.1.15',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Accept-Encoding': 'gzip, deflate'
          }

    def jwxtlogin(self):
        try:
            with open('yanzhengma.jpeg', 'wb+') as img:
                img.write(self.__session.get('http://jwxt.bupt.edu.cn/validateCodeAction.do?random=').content)
            pic = Image.open('yanzhengma.jpeg')
            pic.show()
            yanzhengma = input("Input Captcha: ")  # OCR.OCR_captcha('yanzhengma.jpeg')
            os.remove('yanzhengma.jpeg')
            self.logindata['v_yzm'] = yanzhengma
            data = self.__session.post('http://jwxt.bupt.edu.cn/jwLoginAction.do',
                                    data=self.logindata, headers=self.__headers)
            soup = BeautifulSoup(data.content, 'html.parser')
            print(soup.title.string)
            print('jwxt Login Success')
        except Exception as e:
            print('jwxt Login Error: ' + str(e))

    def login(self):
        data = self.__session.get(self.__webloginurl, headers=self.__headers)
        soup = BeautifulSoup(data.content, 'html.parser')
        '''
        if len(soup.find_all(id='v_chart')) != 0:
            print('no yanzhengma')
        else:
            with open('weblogincaptcha.png', 'wb+') as captcha:
                captcha.write(self.__session.get('http://jwxt.bupt.edu.cn/wengine-auth/captcha/').content)
            pic1 = Image.open('weblogincaptcha.png')
            pic1.show()
            captcha1 = input("Input Captcha: ")  # OCR.OCR_captcha('weblogincaptcha.png')

            os.remove('weblogincaptcha.png')
            self.formdata['captcha'] = captcha1
            '''
        t = self.__session.post(self.__webloginurl, data=self.formdata, headers=self.__headers)
        code = t.status_code
        data = self.__session.get(self.__jwxtloginurl, data=self.logindata, headers=self.__headers)
        soup = BeautifulSoup(data.content, 'html.parser')
        print(soup.title.string)
        if code == 200:
            print('Web Login Success')
            self.jwxtlogin()
        else:
            print('Web Login Error: ' + str(code))

    def get_this_semester_grades(self):
        try:
            print('Start Getting Grades...')
            self.__temp__headers = self.__headers
            self.__temp__headers['host'] = 'jwxt.bupt.edu.cn'
            data = self.__session.get('http://jwxt.bupt.edu.cn/bxqcjcxAction.do', data=self.logindata, headers=self.__headers)
            soup = BeautifulSoup(data.content, 'html.parser')
            tables = soup.find_all('table',{'class': 'titleTop2'})
            tab = tables[0]
            with open('grades.csv','w+') as f:
                for th in tab.find_all('th'):
                    if th == tab.find_all('th')[len(tab.find_all('th'))-1]:
                        f.write(th.string.strip())
                    else:
                        f.write(th.string.strip()+',')
                f.write('\n')
                for tr in tab.find_all('tr', {'class': 'odd'}):
                    for td in tr.find_all('td'):
                        if td == tr.find_all('td')[len(tr.find_all('td'))-1]:
                            f.write(td.string.strip())
                        else:
                            f.write(td.string.strip() + ',')
                    f.write('\n')
                print('Get Grades Success')
        except Exception as e:
            print('Get Grades Error: ' + str(e))

    def get_all_grades(self):
        try:
            print('Start Getting Grades...')
            self.__temp__headers = self.__headers
            self.__temp__headers['host'] = 'jwxt.bupt.edu.cn'
            data = self.__session.get('http://jwxt.bupt.edu.cn/gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001',
                                        data=self.logindata, headers=self.__headers)
            soup = BeautifulSoup(data.content, 'html.parser')
            tables = soup.find_all('table',{'class': 'titleTop2'})

            with open('grades_all.csv','w+') as f:
                for th in tables[0].find_all('th'):
                    if th == tables[0].find_all('th')[len(tables[0].find_all('th'))-1]:
                        f.write(th.string.strip())
                    else:
                        f.write(th.string.strip()+',')
                f.write('\n')
                for tab in tables:
                    for tr in tab.find_all('tr', {'class': 'odd'}):
                        for td in tr.find_all('td'):
                            if td == tr.find_all('td')[len(tr.find_all('td')) - 1]:
                                if td.string is not None:
                                    f.write(td.string.strip())
                                else:
                                    if td.text.strip() != None:
                                        f.write(td.text.strip())
                            else:
                                if td.string is not None:
                                    f.write(td.string.strip() + ',')
                                else:
                                    if td.text.strip() != None:
                                        f.write(td.text.strip() + ',')
                        f.write('\n')
                print('Get Grades Success')

        except Exception as e:
            print('Get Grades Error: ' + str(e))

if __name__ == "__main__":
    wenhe = BUPTjwxt()
    wenhe.login()
    wenhe.get_all_grades()
