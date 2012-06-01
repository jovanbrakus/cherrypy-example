<!-- -*- markdown -*- -->

![CherryPy Screenshot](http://brakus.rs/img/cherrypy/config-view.png)

Introduction
============
CherryPy-Example aims at providing a usefull introductory code for the CherryPy framework, as well as using Jinja2 template engine within CherryPy Server.
Some aspects of CherryPy, Jinja2 and Python used in code are:

 * CherryPy's builtin webserver
 * Shows example of CherryPy application structure
 * Programatic CherryPy Web Server parametrization
 * Basic HTTP Authentication within CherryPy Web Server
 * Simple GET&POST request dispatching
 * File download from CherryPy served page
 * Django-like flash messaging in CherryPy
 * Basic Jinja2 template engine usage
 * Python's ConfigParser usage (parsing&generating .ini files)
 * Python's logging facility usage

Requirements
============

CherryPy-Example has the following dependencies:
 * CherryPy 3.1.2 (or newer)
 * Jinja2 2.5.5 (or newer)

You can install them via easy_install or pip. It's tested&working in Linux and Win.

Overview
========

CherryPy-Example is a failry useless ini-file edit application. 
It provides (not-so-generic) web interface for viewing and editing INI files as well as interface for downloading log files.

Get Started
===========

 * Install all the dependencies
 * Start the server: `python config_server.py`
 * Go to http://localhost:8080 and login (username='cherrypy' & password='cherrypy')
 
Few More screenshots
===========

![CherryPy Overview](http://brakus.rs/img/cherrypy/overview.png)
![CherryPy ConfigView](http://brakus.rs/img/cherrypy/config-view.png)
![CherryPy ConfigEdit](http://brakus.rs/img/cherrypy/config-edit.png)
![CherryPy LogsView](http://brakus.rs/img/cherrypy/logs-download.png)
