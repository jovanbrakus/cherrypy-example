__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

from jinja2 import Environment, PackageLoader
jinja_env = Environment(loader=PackageLoader('configserver', 'static/templates'))