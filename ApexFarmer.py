from pyautogui import *
import pyautogui
import time
import keyboard
import random
from pynput.keyboard import Key
from PIL import Image
from pytesseract import pytesseract

Random = ['a', 'w', 's', 'd', '6', '5']


start_time = time.time()
print("Started")

games_played = 0

total_xp = 0


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"C:\Users\ahfet\OneDrive\CGS 9th Grade\Pictures\cyber2.PNG"
pytesseract.tesseract_cmd = path_to_tesseract

while True:

     # Defining paths to tesseract.exe
     # and the image we would be using
     

     if pyautogui.locateOnScreen('team_fill_true.png', region=(53, 665, 28, 28), grayscale=True, confidence=0.99) != None:
          print("checked")
          pyautogui.moveTo(171, 675)
          time.sleep(0.1)
          pyautogui.click()
          time.sleep(0.1)

     if pyautogui.locateOnScreen('ManuNotReady.png', region=(0, 538, 447, 528), grayscale=True, confidence=0.90) != None:
          pyautogui.moveTo(230, 950)
          pyautogui.click()
          pyautogui.moveTo(860, 540)
          time.sleep(0.5)



#done with lobby
     if pyautogui.locateOnScreen('launch.PNG', region=(885, 904, 1034, 928), grayscale=True, confidence=0.9) != None:
          time.sleep(2)
          keyboard.press_and_release('e')
          time.sleep(0.5)
          key_start = 0
          key_end = 900
          while key_start < key_end:
               time.sleep(0.025)
               keyboard.press('w')
               key_start += 1
          keyboard.release('w')
          time.sleep(0.5)

     if pyautogui.locateOnScreen('InGame.png', region=(87,755,379,304), grayscale=True, confidence=0.5) != None:
          keyboard.press_and_release('5')
          time.sleep(random.randint(5, 20))

     if pyautogui.locateOnScreen('dead.png', region=(693,113,553,79), grayscale=True, confidence=0.9) != None:
          keyboard.press_and_release('space')


     if pyautogui.locateOnScreen('match_summary.png', region=(721, 113, 459,78), grayscale=True, confidence=0.9) != None:
          keyboard.press_and_release('space')
          time.sleep(0.1)

     if pyautogui.locateOnScreen('yes.png', region=(506,550,912,304), grayscale=True, confidence=0.9) != None:
          pyautogui.moveTo(850, 713)
          time.sleep(0.1)
          pyautogui.click()
          time.sleep(0.1)


     # if pyautogui.locateOnScreen('xp_breakdown.png', region=(210,155,268,63), grayscale=True, confidence=0.9) != None:
     #      time.sleep(0.5)
     #      screenshot = pyautogui.screenshot(region = (800,550,204,66))
     #      screenshot.save(image_path)
     #      text = pytesseract.image_to_string(screenshot)

     #      try:
     #           xp_earned = int(text[:-1])
     #           games_played+=1
     #           total_xp+=xp_earned

     #           print("Game #:", games_played, "XP:", xp_earned, "Total XP:", total_xp, "XP/Hour:", total_xp/((time.time()-start_time)/3600), "XP/Game:", total_xp/games_played)
     #      except Exception as e:
               
     #           print('Failed: '+ repr(e))

     #      keyboard.press_and_release('space')
     #      time.sleep(0.5)
          

     
     if pyautogui.locateOnScreen('Continue.PNG', region=(768, 960, 384, 66), grayscale=True, confidence=0.9) != None:
          keyboard.press_and_release('space')
          time.sleep(0.1)

     if pyautogui.locateOnScreen('Continue2.PNG', region=(859, 687, 202, 62), grayscale=True, confidence=0.9) != None:
          pyautogui.moveTo(900, 700)
          time.sleep(0.1)
          pyautogui.click()
          time.sleep(0.1)
         
     if pyautogui.locateOnScreen('startmanu.PNG', region=(773,581,379,304), grayscale=True, confidence=0.9) != None:
          pyautogui.moveTo(952, 717)
          time.sleep(0.1)
          pyautogui.click()
                
    
     # if pyautogui.locateOnScreen('leave.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
     #      pyautogui.click(963, 623)
     #      time.sleep(0.5)
     
     # if pyautogui.locateOnScreen('yes.png', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
     #      pyautogui.click(850, 713)
     #      time.sleep(0.5)
     #      pyautogui.click(850, 713)
     #      time.sleep(0.5)
