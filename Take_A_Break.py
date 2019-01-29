import webbrowser
import time
import random

a=("https://www.youtube.com/watch?v=U39tdiKiaUQ","https://www.youtube.com/watch?v=mYgFJuiAGrg","https://www.youtube.com/watch?v=byitAI7kkOM")
i=1
print("The Break Starts at :"+time.ctime())
while(i<=3):	
	time.sleep(2*60*60)
	webbrowser.open(random.choice(a))
	i +=1
