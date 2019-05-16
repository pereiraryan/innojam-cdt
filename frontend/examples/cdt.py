from flask import Flask
from flask import json
import os
from pprint import pprint
from flask_cors import CORS, cross_origin
#import subprocess

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bdbvbvfdvbdvfevvfsdvdscsdcsdcsavasfvfdaavafdvfvewfvwefvfevfsvafdvefv'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/*": {"origins": "http://localhost:5000"}})
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
#dom = input("Enter Domain To check")
#@app.route('/')


@app.route('/MX_Check',methods=['GET','POST'])
def MX_Check():
	dom = "vvslbuilders.com"
	out = os.popen('ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net host ' +dom+ '').read()
	print(out)
	#out.kill()

	output = os.popen('ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net dig mx vvslbuilders.com +short').read()
	print(output)
	#res.split(" ")

	if dom in output:
		dom_points_to_server= os.popen('ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net sudo grep vvslbuilders.com /etc/localdomains').read()
		if dom in dom_points_to_server:
			return"Yes, Local"
	else:
		print("Remote")
	return "MX Check Complete!!!"
	
@app.route('/m_index', methods=['GET','POST'])
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
	
@app.route('/AUP', methods=['GET','POST'])
def AUP():
	disk_usage= os.popen("ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net sudo du -Sc  /home/vvslbr1n |  sort -rh | head -1").read()
	size=disk_usage.split("  ",1)
	dirsize=size[0]
	print(dirsize)
	if dirsize > "20401094656":
		return "Disk Usage AUP Violation"
		maildir= os.popen("ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net sudo du -Sc /home/vvslbr1n/mail |  sort -rh | head -10").read()
		print(maildir)
		if maildir > "10737418240":
			return "Please reduce Mail Usage, refer https://resellerclub.com/legal-agreements#aup "
	else:
		return "ALL GOOD!"

@app.route('/Email_bl', methods=['GET','POST'])
def Email_bl():
	email_check= os.popen("ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net sudo grep -ir cagentechnologies.com /etc/exim").read()
	print(email_check)
	if "blacklist" in email_check:
		bounce= os.popen("ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net grep cagentechnologies.com /var/log/scripts/blockspam/exim_bounce_check.log").read()
		return json.dumps(bounce)
			
		spammy=os.popen("ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net grep cagentechnologies.com /var/log/scripts/blockspam/cloudmark_spam_bklist.log").read()
		return json.dumps(spammy)
		
		abuse=os.popen("ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net grep cagentechnologies.com /etc/exim/exim_smtp_blacklisted_authenticated_user").read()
		return json.dumps(abuse)
	else:
		return("No Email Accounts Blacklisted")

@app.route('/Infected', methods=['GET','POST'])
def Infected():
	infected = os.popen("ssh -i my_key.pem omkar.k@cp-ht-1.webhostbox.net sudo cat /home/vvslbr1n/infected.txt").read().split("\n") # Actual Command is sudo clamdscan -i /home/user
	infected_files=json.dumps(infected)
	return infected_files
if __name__ == '__main__':
    app.run(debug=True)




#dig = os.popen('dig a vvslbuilders.com +short')

#pprint(dig.read())
