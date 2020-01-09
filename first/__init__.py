from flask import Flask

app=Flask(__name__)

@app.route("/hello")
def hello():
	return("hello suhas and fuck off ASAP")
@app.route("/")
def index():
        return("helloooooo")
@app.route("/aa")
def aa():
        return("come on u can do better")
if __name__ == '__main__':
    app.run()


	# ServerName 127.0.0.1
	# 	WSGIDaemonProcess first threads=5
	# 	WSGIScriptAlias / /home/suhas/projects/flask/first/first.wsgi
	# 	<Directory /home/suhas/projects/flask/first/first/>
	# 		Require all granted
	# 		WSGIScriptReloading On
	# 	</Directory>
	# 	Alias /static /home/suhas/projects/flask/first/first/static
	# 	<Directory /home/suhas/projects/flask/first/first/static/>
	# 		Require all granted
	# 	</Directory>
	# 	ErrorLog ${APACHE_LOG_DIR}/error.log
	# 	LogLevel warn
	# 	CustomLog ${APACHE_LOG_DIR}/access.log combined
