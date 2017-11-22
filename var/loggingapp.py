import ConfigParser
import logging

from logging.handlers import RotatingFileHandler
from flask import Flask, url_for

app = Flask(__name__)
@app.route('/')
def root():
    this_route = url_for('.root')
    app.logger.info("Logging a test messgage from "+this.route)
    return ("Hello Napier from the config logger test app")

def init(app):
   config = ConfigParser.ConfigParser()
   try:
     config_location = url_for('etc/logging.cfg')
     config.read(config_location)

     app.config['DEBUG'] = config.get("config","debug")
     app.config['ip_address'] = config.get("config","ip_address")
     app.config['port'] = config.get("config", "port")
     app.config['url'] = config.get("config", "url")
     
     app.config['log_file'] = config.get("logging", "name")
     app.config['log_location'] = config.get("logging", "location")
     app.config['log_level'] = config.get("logging", "level")
   except:
     print "could not read config files from :", config_location

def logs(app):
    log_pathname = app.config['log_location'] + app.config['log_file']
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024*1024*10 , backupcount=1024)
    file_handler.setLevel = (app.config['log_level'])
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName)s | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel( app.config['log_level'])
    app.logger.addHandler(file_handler)

if __name__ == '__main__'
  init(app)
  logs(app)
  app.run(
     host=app.config['ip_address']
     port=init(app.config['port']))

