from flask import Flask
import os
#import subprocess

app = Flask(__name__)
dom = input("Enter Domain To check")
#@app.route('/')


@app.route('/MX_Check')
def MX_Check():
	out = os.popen('ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net host ' +dom+ '').read()
	print(out)
	#out.kill()

	output = os.popen('ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net dig mx vvslbuilders.com +short').read()
	print(output)
	#res.split(" ")

	if dom in output:
		dom_points_to_server= os.popen('ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net sudo grep vvslbuilders.com /etc/localdomains').read()
		if dom in dom_points_to_server:
			print("Yes, Local")
	else:
		print("Remote")
	return "MX Check Complete!!!"
	
@app.route('/m_index')
def Missing_index():
	login = os.popen('ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net sudo grep vvslbuilders.com /etc/trueuserdomains')
	out = login.read()
	username = out.split(":",1)
	user=username[1]
	print(user)
	index = os.popen("ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net sudo ls /home/vvslbr1n/public_html |  grep index")
	a=index.read().split("\n")
	#print(a[1])
	try:
		if "index" in a[1] :
			return "Site has Index Page"
	except:
		return "No Index File Found"
	
	
#Missing_index()

#MX_Check()

if __name__ == '__main__':
    app.run(debug=True)





#dig = os.popen('dig a vvslbuilders.com +short')

#pprint(dig.read())

