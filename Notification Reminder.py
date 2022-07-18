import time
from plyer import notification
if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "**Please Do Workout Now!!",
 			message ="Exercise can help prevent excess weight gain or help maintain weight loss.",
 			app_icon =  "C:\Users\MSI\Downloads\Iconsmind-Outline-Running.ico",
 			timeout= 12
 			)
 		
time.sleep(60*60)