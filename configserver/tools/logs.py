"""
Log files management functionality
"""
__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

import os
import uuid
import logging
import zipfile

from configserver import settings

log = logging.getLogger(__name__)

def get_logs_list():
    '''
    Returns list of all present log files.
    '''    
    result = []    
    for file in os.listdir(settings.LOG_DIR):
        result.append(file)
        
    log.debug('Found log files: %s', str(result))
    return result

def create_log_archive():
    '''
    Create log file archive.
    Returns archive file name or None if creation failed.
    '''
    log.debug("Creating log archive with snapshot of current log files.")
    archive_filename = os.path.join(os.getcwd(), settings.TEMP_DIR, str(uuid.uuid4()))
    log.debug("Created log archive filename: %s", archive_filename)
    
    zip_file = zipfile.ZipFile(archive_filename, 'w')
    for log_file in get_logs_list():
        zip_file.write(os.path.join(settings.LOG_DIR, log_file), arcname=log_file)        
    zip_file.close()
    
    log.debug("Created log archive: %s", archive_filename)
    return archive_filename