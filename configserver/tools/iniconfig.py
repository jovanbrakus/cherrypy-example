"""
Ini file configuration management functionality
"""
__author__    = 'Jovan Brakus <jovan@brakus.rs>'
__contact__   = 'jovan@brakus.rs'
__date__      = '31 May 2012'

import os
import logging
import sys

from ConfigParser import SafeConfigParser
from configserver import settings

log = logging.getLogger(__name__)

class IniConfig:
    general = None
    specific = None
        
    config_filepath = None
    
    def __init__(self, current = True, config_dict = None, update_normalization = False):
        ''' Config object constructor. Can create data from actual config file or from given config dictionary. '''
        #First we create empty config dicts.
        self.general = dict()
        self.specific = dict()
        
        self.config_filepath = os.path.join(os.getcwd(), settings.CONFIG_FILENAME)
        print self.config_filepath
        #If set, read configuration from actual config file.
        if current:
            log.debug("Reading parameters from INI configuration file.")
    
            #Try to guess where is ini file
            if not os.path.exists(self.config_filepath):
                log.error("INI configuration file was not found.")
            
            parser = SafeConfigParser()
            parser.read(self.config_filepath)
            
            if parser.has_section('general'):
                self.general = dict(parser.items('general'))
            if parser.has_section('specific'):
                self.specific = dict(parser.items('specific'))
            log.debug("Current INI Configuration read successfully.")
            
        if config_dict and type(config_dict) is dict:
            log.debug("Reading parameters from INI configuration dictionary.")
            
            if not validate_config_dict(config_dict):
                log.error("Given INI configuration dictionary is not valid.")
				#Failed validation should be handled properly... throw back flash message to user or similar.
            
            self.general['str_param'] = self._get_str_from_dict(config_dict, 'general_str_param')
            self.general['switch_param'] = self._get_onoff_from_dict(config_dict, 'general_switch_param')
            self.general['numerical_value'] = self._get_float_from_dict(config_dict, 'general_numerical_value')
            
            self.specific['something'] = self._get_str_from_dict(config_dict, 'specific_something')
            self.specific['enabled'] = self._get_bool_from_dict(config_dict, 'specific_enabled')
            self.specific['number'] = self._get_float_from_dict(config_dict, 'specific_number')
            
            log.debug("INI configuration dictionary read.")

    def to_dict(self):
        ''' Creates config_dict from object '''
        
        config_dict = dict()
        
        config_dict['general_str_param'] =  self.general['str_param']
        config_dict['general_switch_param'] =  self.general['switch_param']
        config_dict['general_numerical_value'] =  self.general['numerical_value']
        
        config_dict['specific_something'] =  self.specific['something']
        config_dict['specific_enabled'] =  self.specific['enabled']
        config_dict['specific_number'] =  self.specific['number']
        
        return config_dict

    def updateConfigFile(self):
        '''Updated actuall INI configuration file'''
        
        parser = SafeConfigParser()
        
        for section in ['general', 'specific']:
            section_dict = getattr(self, section)
            parser.add_section(section)
            for section_key in section_dict.keys():
                parser.set(section, section_key, str(section_dict[section_key]))

        parser.write(sys.stdout)

        config_file = open(self.config_filepath, 'w')
        parser.write(config_file)
        config_file.close()
        
    def _get_bool_from_dict(self, config_dict, key_name):
        if key_name in config_dict:
            result = bool(config_dict[key_name])
        else:
            result = False
        return result
    
    def _get_str_from_dict(self, config_dict, key_name):
        if key_name in config_dict:
            result = str(config_dict[key_name])
        else:
            result = ''
        return result
        
    def _get_onoff_from_dict(self, config_dict, key_name):
        if key_name in config_dict:
            result = str(config_dict[key_name])
        else:
            result = ''            
        if result != 'on':
            result = 'off'
        return result
        
    def _get_int_from_dict(self, config_dict, key_name):
        try:
            if key_name in config_dict:
                result = int(config_dict[key_name])
            else:
                result = 0
        except:
            result = 0
        return result
    
    def _get_float_from_dict(self, config_dict, key_name):
        try:
            if key_name in config_dict:
                result = float(config_dict[key_name])
            else:
                result = 0
        except:
            result = 0
        return result

def purge_config_dict(post_dict):
    ''' Removes all unnecessary keys from given dict '''
    allowed_keys = ['general_str_param', 'general_switch_param', 'general_numerical_value', 'specific_something', 'specific_enabled','specific_number']
    result_dict = dict()
    
    for key in post_dict.keys():
        if key in allowed_keys:
            result_dict[key] = post_dict[key]
    return result_dict

def validate_config_dict(config_dict):
    return True
        
    
    
    