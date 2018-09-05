# coding:utf-8
import os

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "template"),
    "debug": True,
    "cookie_secret": "skdfkdkjfksdfkdkfd",
    "xsrf_cookies": True,
}

mysql_options = dict(
    host="127.0.0.1",
    database="ihome",
    user="root",
    password="123456"
)

redis_options = dict(
    host="127.0.0.1",
    port=6379
)

# 日志配置
# 路径
log_file = os.path.join(os.path.dirname(__file__), "logs/log")
# 日志等级 debug,info,warning,error
log_level = "debug"
