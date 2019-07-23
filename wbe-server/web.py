import os, os.path

import requests

import cherrypy
import test

cherrypy.config.update({'server.socket_port': 80})
cherrypy.engine.restart()


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

    @cherrypy.expose
    def generate(self, email, phone, text):
        test.send_message(email, phone, text)
        return open('rev.html')

    @cherrypy.expose
    def rev(self):
        return open('rev.html')

    @cherrypy.expose
    def qr(self):
        return open('qr.html')

    @cherrypy.expose
    def bot(self, text):
        print(text)
        return 'ok'


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.quickstart(StringGenerator(), '/', conf)
