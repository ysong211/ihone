# coding:utf-8
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os
import pymysql
import redis
import config
from tornado.web import RequestHandler
from tornado.options import options, define
from urls import handlers


define("port", default=8001, type=int, help="server port")

class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        # self.db = torndb.Connection(
        # host=config.mysql_options["host"],
        # database=config.mysql_options["database"],
        # user=config.mysql_options["user"],
        # password=config.mysql_options["password"]

        # self.redis = redis.StrictRedis(
        #     host=config.redis_options["host"],
        #     port=config.redis_options["port"]
        # )
        # 简写方式
        self.db = pymysql.Connection(**config.mysql_options)
        self.redis = redis.StrictRedis(**config.redis_options)

def main():
    options.logging = config.log_level
    options.log_file_prefix = config.log_file
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers, **config.settings
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
