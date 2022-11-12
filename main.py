import requests
import threading
import datetime
import time

def keep_alive(username, password, a):
	while True:
		payload = "http://192.168.8.1:8090/live?mode=192&username="+username+"&a="+a+"&producttype=0"
		r = requests.get(payload)
		print("Keep alive: "+str(r))
		time.sleep(10)

def log_in(username, password, a):
	payload = {"mode" :"191", "username" : username, "password": password, "a": a, "producttype": "0" }
	r = requests.post("http://192.168.8.1:8090/login.xml",payload)
	print("Log in request: "+str(r))
	time.sleep(7)
	return 0

def log_out(username, password, a):
	payload = {"mode" :"193", "username" : username, "password": password, "a": a, "producttype": "0" }
	r = requests.post("http://192.168.8.1:8090/logout.xml",payload)
	print("Log out request: "+str(r))

def main():
	while True:
		#taking inputs
		username = str(input("Enter username\n"))
		password = str(input("Enter password\n"))
	
		#time stamp(DO NOT TOUCH THIS) 
		date_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
		a = str(time.mktime(date_time.timetuple()))

		#for checking if portal is available
		r = requests.get("http://192.168.8.1:8090")
		print("Server connection: "+str(r))
	
		if (r.status_code == 200):
			r = log_in(username,password,a)
			t1 = threading.Thread(target = keep_alive, args=(username, password, a))
			if(r == 0):
				t1.start()
				choice = str(input("Press N or n to Log-out\n"))
				if (choice == 'N' or choice == 'n' ):
					log_out(username, password, a)

		else:
			time.sleep(20)

if __name__ == '__main__':
	main()
