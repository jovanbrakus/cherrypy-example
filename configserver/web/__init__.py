"""
CherryPy Config web server package for Python.
"""
__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

import os.path
import cherrypy

from sha import sha

from configserver import settings
from iniconfig import IniConfigServer
from logs import LogsServer
from root import RootServer

def encrypt_pw(pw):
    return sha(pw).hexdigest()

class ConfigServer:
    users = None
    rootServer = None
    config = None

    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        static_dir = os.path.join(current_dir, '..', 'static')        

        self.config = { '/': {'tools.basic_auth.on': True,
                              'tools.basic_auth.realm': 'CherryPy Restricted space. Hint[user:cherrypy & pass:cherrypy]',
                              'tools.basic_auth.users': {'cherrypy':encrypt_pw('cherrypy')},
                              'tools.basic_auth.encrypt': encrypt_pw,
                              'tools.staticdir.root': static_dir},
                        '/static': {'tools.gzip.on': True,
                                    'tools.staticdir.on': True,
                                    'tools.staticdir.dir': ''},
                        '/static/css': {'tools.gzip.mime_types':['text/css'],
                                        'tools.staticdir.dir': 'css'},
                        '/static/js': {'tools.gzip.mime_types': ['application/javascript'],
                                       'tools.staticdir.dir': 'js'},
                        '/static/img': {'tools.staticdir.dir': 'images'}}

        self.rootServer = RootServer()        
        self.rootServer.ini = IniConfigServer()
        self.rootServer.logs = LogsServer() 
        
    def start(self):
        global_conf = {'global': {'server.socket_host': settings.WEBSERVER_HOST,
                                  'server.socket_port': settings.WEBSERVER_PORT}}
        cherrypy.config.update(global_conf)        
        cherrypy.config["tools.encode.on"] = True
        cherrypy.config["tools.encode.encoding"] = "utf-8"
        cherrypy.config["tools.sessions.on"] = True
        cherrypy.tree.mount(self.rootServer, '/', config = self.config)
        cherrypy.engine.start()
        
