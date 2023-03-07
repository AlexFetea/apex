from pyautogui import *
import pyautogui
import time
import keyboard
import random
from pynput.keyboard import Key

Random = ['a', 'w', 's', 'd', '6', '5']

while True:
    
    if pyautogui.locateOnScreen('team_fill_true.png', region=(53, 665, 28, 28), grayscale=True, confidence=0.99) != None:
        print("checked")
        pyautogui.moveTo(171, 675)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)

    if pyautogui.locateOnScreen('ManuNotReady.png', region=(0, 538, 447, 528), grayscale=True, confidence=0.90) != None:
        pyautogui.moveTo(230, 950)
        pyautogui.click()
        time.sleep(5)


    if pyautogui.locateOnScreen('ManuReady.png', region=(0, 538, 447, 528), grayscale=True, confidence=0.7) != None:
         print("Waiting for game")
         time.sleep(5)


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
         print("In game waiting")
         keyboard.press_and_release('5')
         time.sleep(random.randint(5, 20))

    if pyautogui.locateOnScreen('dead.png', region=(693,113,553,79), grayscale=True, confidence=0.9) != None:
          print("dead")
          keyboard.press_and_release('space')


    if pyautogui.locateOnScreen('match_summary.png', region=(721, 113, 459,78), grayscale=True, confidence=0.9) != None:
          print("gameover")
          keyboard.press_and_release('space')
                
    
    if pyautogui.locateOnScreen('leave.png', region=(0,0,1920,1080), grayscale=True, confidence=0.6) != None:
          pyautogui.click(963, 623)
          time.sleep(0.5)
     
    if pyautogui.locateOnScreen('yes.png', region=(506,550,912,304), grayscale=True, confidence=0.6) != None:
         pyautogui.click(850, 713)
         time.sleep(0.5)
         pyautogui.click(850, 713)
         time.sleep(0.5)


    if pyautogui.locateOnScreen('Continue.PNG', region=(768, 960, 384, 66), grayscale=True, confidence=0.6) != None:
         keyboard.press_and_release('space')
         time.sleep(0.5)
         keyboard.press_and_release('space')
         
    if pyautogui.locateOnScreen('startmanu.PNG', region=(773,581,379,304), grayscale=True, confidence=0.6) != None:
         pyautogui.click(952, 717)
         time.sleep(0.5)
         pyautogui.click(952, 717)
