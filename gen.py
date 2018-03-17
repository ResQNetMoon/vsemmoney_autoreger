import requests
from threading import Thread 
from random import randint
from time import sleep
cc = 0
def main():
	global cc
	
	email = "class"+str(randint(0, 1000000))+'@mail.ru'
	login = 'paypayeer300k'+str(randint(0, 100000))
	posts = {'email':str(email), 'wm':'P92193111','login':login, 'ref':'', 'pw':'paymeFORPAYEER300K', 'password':'paymeFORPAYEER300K', 'g-captcha-response':'03ANcjosrJ-rH1mRWIy0fE-UbU5i0JrI7sn14mPw1vZa23fHzb6vhcQeuSGh8hXX7RrslirhRdXwNmn0eTyYCkzBctKAYZ3-XjsA5T2KK971PWZYL4foSaoo-X1NByEIuWg_St7EJ7xKQ4B7LKB07Ec8_uAfFTvNMzHPtLFBs-J-Yt71QHrqeWCfTyeit0RMl8HiDG57-kDbxzI0aaTdYSEZ0K6rrD-PCdFDQU0iTh7CgVRZdinpE-iRsDh4rGLpCrT9SgVRXIHKjzZrFtB_H6FsmjiIW6GPUuni0SRjZJyjgmSEJGHbBAUBhGCqPjns_7BqOkMZ5oQbZKsazShgNcw4MU1r9vNqzigwHFbIJWFb_NzSEnkx5CWltuI5cblmJtMBc8ozc8jcI53ZbRRQkke4HEatJM7UbuwQ'}
	data = requests.post('https://vsem.money/?reg', posts, headers={"User-Agent":"Mozilla/5.0"})
	
	if data.text == 'Успех!':
		cc += 1
		
		print("Зарегистрировано - {}".format(cc), end='\r')
		f = open('users.txt', 'a+')
		f.write(login+':'+'paymeFORPAYEER300K\n')
		f.close()
	else:
		print(data.text)
usr = []

for i in range(0, randint(0, 100000)):
	usr.append(Thread(target=main))
ccs = 0
for iss in usr:
	ccs += 1
	iss.start()
	if ccs >= 170:
		iss.join()
		ccs = 0
