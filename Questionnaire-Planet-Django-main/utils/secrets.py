
class Secrets:

    class DataBase:
        # database information
        host = 'localhost'
        user = 'root'
        passwd = ''  # 修改为您本地或远程的 mysql数据库信息
        db = 'questionnaire'

    class Email:
        emailHost = 'smtp.163.com'
        emailPort = 25
        emailAddr = 'xianzhoyyu@163.com'
        emailPasswd = 'Xzy20030229@'# 邮箱 SMTP 授权码，此处为虚拟，须修改

    class Host:  # 修改为django允许运行的网址
        allowedHost = ['localhost', '127.0.0.1', 'xxxxx']

    class RootUrl:
        webFront = 'http://127.0.0.1:8080'
        # webBack = 'http://127.0.0.1:8000'
        webBack = 'http://127.0.0.1:8080/api/api/qs'
