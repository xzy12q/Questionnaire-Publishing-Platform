"""
djangoProject 项目的 Django 设置。

由 'django-admin startproject' 使用 Django 3.2.6 生成。

有关此文件的更多信息，请参阅
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
from pathlib import Path
import pymysql

from utils.secrets import *

pymysql.install_as_MySQLdb()

# 在项目内部构建路径，如下所示：BASE_DIR / 'subdir'。
BASE_DIR = Path(__file__).resolve().parent.parent

# 快速启动开发设置 - 不适合生产
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# 安全警告：对生产中使用的密钥保密！
SECRET_KEY = 'django-insecure-171w4v=lzo@ya3b9i@m+n@r0_2^g-l$_kb!i1x!db^5+p@#$i9'

# 安全警告：不要在生产环境中打开调试的情况下运行！
DEBUG = True

ALLOWED_HOSTS = Secrets.Host.allowedHost

# 应用定义
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'userinfo',
    'Qn',
    'Submit',
    'exam',
    'vote',
    'signup',
    'epidemic',
    'resources',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

# 允许全部来源
CORS_ORIGIN_ALLOW_ALL = True  # 如果为True，将不使用白名单，并且将接受所有来源。默认为False。

# 白名单
# CORS_ORIGIN_WHITELIST  =  [
#     "https://example.com",
#     "https://sub.example.com",
#     "http：// localhost：8080",
#     "http://127.0.0.1:9000"
# ]
#
# # 白名单也可使用正则
# CORS_ORIGIN_REGEX_WHITELIST  =  [
#     r"^https://\w+\.example\.com$",
# ]

ROOT_URLCONF = 'djangoProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': []
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoProject.wsgi.application'

# SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# 推出浏览器session失效，但是好像有问题
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {  # 配置 mysql 数据库
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': Secrets.DataBase.db,
        'USER': Secrets.DataBase.user,
        'PASSWORD': Secrets.DataBase.passwd,
        'HOST': Secrets.DataBase.host,
        'POST': '3306',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci'
        }
    }
}

# 密码验证
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'  # 时间错位问题

USE_I18N = True

USE_L10N = True

USE_TZ = False  # 当地时间，若为True会与实际相差8小时

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# 默认主键字段类型
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 发送邮件配置

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = Secrets.Email.emailHost
EMAIL_PORT = Secrets.Email.emailPort
EMAIL_HOST_USER = Secrets.Email.emailAddr
EMAIL_HOST_PASSWORD = Secrets.Email.emailPasswd  # 邮箱 SMTP 授权码

CONFIRM_DAYS = 3  # 确认有效天数

# File path root

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# Root url

WEB_FRONT = Secrets.RootUrl.webFront
WEB_ROOT = Secrets.RootUrl.webBack

# X_FRAME_OPTIONS = 'SAMEORIGIN'
