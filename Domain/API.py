import cherrypy
import os, os.path
import hashlib
import requests
import imghdr
import sqlite3
from flask import Flask

from flask import redirect, url_for, request, render_template, send_file
from io import BytesIO

baseDir = os.path.dirname(os.path.abspath(__file__))

USERS = {'admin': 'admin', 'medico': 'medico', 'cliente': 'cliente'}

# Dict with the this app's configuration:
config = {
  "/":     { "tools.staticdir.root": baseDir },
  "/js":   { "tools.staticdir.on": True,
             "tools.staticdir.dir": "../Site/js/" },
  "/css":  { "tools.staticdir.on": True,
             "tools.staticdir.dir": "../Site/css/" },
#   "/scss": { "tools.staticdir.on": True,
# 			 "tools.staticdir.dir": "../Site/scss/" },
  "/images":{"tools.staticdir.on": True,
			 "tools.staticdir.dir": "../Site/img" },
  "/html": { "tools.staticdir.on": True,
             "tools.staticdir.dir": "../Site/" },
}

cherrypy.config.update({'server.socket_port': 10022,})

class Root(object):
    def __init__(self):
        #self.add = Add()
        self.actions = Actions()
        #self.comment = Comment()

    @cherrypy.expose
    def index(self):
        cherrypy.response.headers["Content-Type"] = "text/html"
        return open("../Site/index.html", "r").read()

    @cherrypy.expose
    def profile(self):
        return open("../Site/profile.html").read()

    @cherrypy.expose
    def login(self):
        return open("../Site/login.html").read()

    @cherrypy.expose
    def shop(self):
        return open("../Site/shop.html").read()

    # @cherrypy.expose
    # def pic(self):
    #     cherrypy.response.headers["Content-Type"] = "text/html"
    #     return open("../Site/Pic.html").read()

    @cherrypy.expose
    def subcription(self):
        return open("../Site/subcription.html").read()

    @cherrypy.expose
    def about(self):
        return open("../Site/about.html").read()

    index.exposed = True 

class Actions(object):
    @cherrypy.expose
    def doLogin(self, username=None, password=None):
        if username in USERS and USERS[username] == password:
            raise cherrypy.HTTPRedirect("/profile")
        else:
            raise cherrypy.HTTPRedirect("/login")

class HelloWorld(object):
    def index(self):
    
        return "Hello World!"
    
    index.exposed = True

if __name__ == "__main__":
	cherrypy.quickstart(Root(), "/", config)
