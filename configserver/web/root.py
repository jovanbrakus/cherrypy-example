"""
Root web server
"""

__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

import platform
import cherrypy
import datetime
from configserver.tools.common import  get_version, render_template, info, error, success, warning

class RootServer:
	@cherrypy.expose
	def index(self, **kwargs):
		sw_version = get_version()
		return render_template("index.html", sw_version = sw_version, current_time = datetime.datetime.now(), os_info = ', '.join(platform.uname()[:4]))