import tornado.ioloop
import tornado.web
from celery_app.tasks import demo_celery_run


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        async_result = demo_celery_run.apply_async()
        resp = await tornado.ioloop.IOLoop.current().run_in_executor(None, async_result.get)
        self.write(resp)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

def main():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()