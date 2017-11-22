import ConfigParser
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/')
def root():
  return render_template('index.html'), 200

@app.route('/asia')
def asia():
  return render_template('asia.html'), 200

@app.route('/europe')
def euro():
  return render_template('euro.html'), 200

@app.route('/southamerica')
def southam():
  return render_template('southamerica.html'), 200

@app.route('/northamerica')
def northam():
  return render_template('northamerica.html'), 200

@app.route('/africa')
def africa():
  return render_template('africa.html'), 200

@app.route('/asia/japan')
def japan():
  return render_template('japan.html'), 200

@app.route('/asia/japan/sushi')
def sushi():
  return render_template('sushi.html'),200

@app.route('/asia/japan/ramen')
def ramen():
  return render_template('ramen.html'), 200

@app.route('/europe/france')
def france():
  return render_template('france.html')

@app.route('/europe/italy')
def italy():
  return render_template('italy.html')

@app.route('/europe/france/onion_soup')
def onion():
  return render_template('onion.html')

@app.route('/europe/italy/pizza')
def pizza():
  return render_template('pizza.html')

@app.route('/southamerica/brazil')
def brazil():
  return render_template('brazil.html')

@app.route('/southamerica/brazil/stew')
def stew():
  return render_template('brazstew.html')

@app.route('/southamerica/argentina')
def argentina():
  return render_template('argetina.html')

@app.route('/southamerica/argentina/empandas')
def empanda():
  return render_template('empanda.html')

@app.route('/northamerica/usa')
def usa():
  return render_template('usa.html')

@app.route('/northamerica/usa/apple_pie')
def apppie():
  return render_template('applepie.html')

@app.route('/northamerica/usa/veg_chilli')
def vegchil():
  return render_template('vegchilli.html')

@app.route('/africa/morocco')
def morocco():
  return render_template('morocco.html')

@app.route('/africa/morocco/chicken_cous_cous')
def chiccous():
  return render_template('chiccous.html')

@app.route('/africa/morocco/lentil_soup')
def morsoup():
  return render_template('lentilmor.html')




@app.route('/config/')
def config():
  str = []
  str.append('Debug:'+app.config['DEBUG'])
  str.append('port:'+app.config['port'])
  str.append('url:'+app.config['url'])
  str.append('ip_address:'+app.config['ip_address'])
  return '/t'.join(str)

def init(app):
   config = ConfigParser.ConfigParser()
   try:
     config.location = "etc/defaults.cfg"
     config.read(config.location)

     app.config['DEBUG'] = config.get("config", "debug")
     app.config['ip_address'] = config.get("config", "ip_address")
     app.config['port'] = config.get("config", "port")
     app.config['url'] = config.get("config", "url")
   except:
     print "Could not get config details: ", config.location

@app.errorhandler(404)
def page_not_found(error):
 return render_template('404.html'), 404


if __name__ == "__main__":
 init(app)
 app.run(
    host=app.config['ip_address'],
    port=init(app.config['port']))
