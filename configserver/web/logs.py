"""
Log files manager pages
"""
__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

import os
import cherrypy
from datetime import datetime
from cherrypy.lib import static

from configserver import settings

from configserver.tools.logs import get_logs_list, create_log_archive
from configserver.tools.common import render_template, info, error, success, warning


class LogsServer:
	@cherrypy.expose
	def index(self):
		log_files = get_logs_list()
		return render_template("logs.html", log_files=log_files)
		
	@cherrypy.expose
	def download(self, log_filename):
		#If log_filename is 'all', log archive is actually requested.
		if log_filename == 'all':
			return self.download_archive()
		
		if log_filename not in get_logs_list():
			return index()
		
		logfile_fullpath = os.path.join(os.getcwd(), settings.LOG_DIR, log_filename)
		return static.serve_file(logfile_fullpath, "application/x-download", "attachment", os.path.basename(logfile_fullpath))

	def download_archive(self):
		temp_archive_filename = create_log_archive()
		archive_firendly_name = 'cherrypy-logs-' + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.zip'	
		return static.serve_file(temp_archive_filename, "application/x-download", "attachment", archive_firendly_name)
		