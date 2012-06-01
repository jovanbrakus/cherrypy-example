"""
Ini file Config server
"""
__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

import os

import cherrypy
from cherrypy.lib import static

from configserver.tools.iniconfig import IniConfig, purge_config_dict, validate_config_dict
from configserver.tools.common import render_template, info, error, success, warning
from configserver import settings

class IniConfigServer:
	@cherrypy.expose
	def index(self):
		return render_template("iniconfig.html", ini_config = IniConfig(current=True))
		
	@cherrypy.expose
	def download(self):
		#If log_filename is 'all', log archive is actually requested.
		config_file = IniConfig(current=False).config_filepath
		return static.serve_file(config_file, "application/x-download", "attachment", os.path.basename(config_file))
		
	@cherrypy.expose
	def edit(self, **kwargs):
		if cherrypy.request.method == 'POST':
			return self.edit_post(kwargs)
		else:			
			return self.edit_get(IniConfig(current=True).to_dict())
			
	def edit_get(self, config_dict):
		return render_template("iniconfig_edit.html", conf = config_dict)
		
	def edit_post(self, post_dict):
		post_dict = purge_config_dict(post_dict)
		if not validate_config_dict(post_dict):
			error("Invalid parameters given.")
			return self.edit_get(post_dict)
		else:
			conf = IniConfig(config_dict = post_dict)
			conf.updateConfigFile()
			success("Ini file configuration updated successfully.")
			return self.index()
		
		