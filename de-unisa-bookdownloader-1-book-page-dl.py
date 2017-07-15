#quick script to download a book from the unisa library, page by page. Saves all files as a JPG.
#Note: This hack uses the mouse and keyboard, dont expect it to work. 
#Step 1, open the book in the online library. Then run this script
#2017-07-12

import time
import autopy as ap
from autopy.mouse import LEFT_BUTTON
from autopy.mouse import RIGHT_BUTTON
from autopy import key

def leftClick():
    ap.mouse.click(LEFT_BUTTON)
    time.sleep(.1)
    print "# click"

def rightClick():
    ap.mouse.click(RIGHT_BUTTON)
    time.sleep(.1)
    print "# click"

print('de script to DL book from uniSA')

width, height = ap.screen.get_size()
print 
print 'screen size: ',ap.screen.get_size()
mouseX,mouseY = ap.mouse.get_pos()
print 'mouse position: ',ap.mouse.get_pos()
#time.sleep(1)
print 'mouse position: ',ap.mouse.get_pos()
#time.sleep(1)
print 'mouse position: ',ap.mouse.get_pos()
print 'Starting autokey script in 2 seconds'
time.sleep(3)
#

#Adjust Page Number Downloading Here.
pageNumber= 2 		#2=The next page to DL. Have Start macro on page 1
pageNumberEnd=540 	#The end page
#CONSTANTS For Mac 1280x800px screen
nextButtonX=798
nextButtonY=211

#Move Mouse to Next Page Button
ap.mouse.smooth_move(nextButtonX, nextButtonY) 
	
#Click to view Browser
leftClick()

#CLICK on Next Page Button
leftClick()

#Start Looping Process
for i in range(pageNumber, pageNumberEnd):

	#WAIT for image to load
	time.sleep(6)

	#Move Mouse to Page So Mouse can right click and press save
	pageX=480
	pageY=329
	ap.mouse.smooth_move(pageX, pageY)  

	rightClick()
	ap.mouse.smooth_move(pageX+23,pageY+28) #Move Mouse to Save (move 23 to the right, 28 down)
	leftClick() #for save
	

	#Save Dialog Appears
	time.sleep(2)

	print('typing in page number:')
	print pageNumber
	ap.key.type_string(str(pageNumber))
	time.sleep(2)

	#Hit Enter
	key.tap(long(key.K_RETURN))

	time.sleep(2)

	#Move Mouse to Next Page Button
	ap.mouse.smooth_move(nextButtonX, nextButtonY) 
	time.sleep(1)
	
	#Click to view Browser
	leftClick()

	#inc
	pageNumber = pageNumber + 1

