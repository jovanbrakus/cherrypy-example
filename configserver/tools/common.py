"""
Common functionality
"""
__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

import os
import logging

import cherrypy
import configserver

from configserver.web.templates import jinja_env

log = logging.getLogger(__name__)
    
def get_version():
    '''
    Returns current software version
    '''
    return configserver.__version__
    
class FlashMessage(object):
    def __init__(self, message, level):
        self.message = message
        self.level = level

    def __repr__(self):
        return self.message
    
class FlashMessagesIterator(object):
    def __init__(self):
        self.messages = list()

    def append(self, message):
        self.messages.append(message)

    def __iter__(self):
        return self

    def next(self):
        if len(self.messages):
            return self.messages.pop(0)
        else:
            raise StopIteration
    
def flash(message, level='info'):    
    if 'flash' not in cherrypy.session:
         cherrypy.session['flash'] = FlashMessagesIterator()

    if not level in ['info', 'error', 'warning', 'success']:
        log.warning("Got flash message '%s' with invalid message level: '%s'", message, level)
        level = 'info'

    flash_message = FlashMessage(message, level)
    cherrypy.session['flash'].append(flash_message)
    
def info(message):
    flash(message, 'info')

def error(message):
    flash(message, 'error')

def warning(message):
    flash(message, 'warning')

def success(message):
    flash(message, 'success')
    
def get_messages():
    if 'flash' in cherrypy.session:
        return cherrypy.session['flash']
    else:
        return list()
        
def render_template(template, **kwargs):
    kwargs['messages'] = get_messages()
    return jinja_env.get_template(template).render(**kwargs)
    
