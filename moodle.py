import pyautogui, time, threading
from pynput import keyboard
#print(pyautogui.position())
cardPosX, cardPosY = 1592, 519
knowPosX, knowPosY = 1778, 519
mess= "-----------\nG - toggle autoclick\nH - toggle flashcards\nF8 - toggle access to functions above\n--------------"

def flashcards():
    print("flashcards init")
    while True:
        if flashcard:
            for i in range(10):
                pyautogui.click(cardPosX, cardPosY)
                time.sleep(0.15) 
                pyautogui.click(knowPosX, knowPosY)
                time.sleep(0.15) 
            time.sleep(0.15)
            pyautogui.click(knowPosX, knowPosY)
            print("end of flashcards function")

def autoclicker():
    print("autoclicker init\n")
    while True:
        if autoclickerBool:
            pyautogui.click()
            time.sleep(0.25)

def on_press(key):
    global flashcard
    global autoclickerBool
    global access

    if access:
        if flashcard:
            if 'h' in str(key):
                print(f"flashcards off \n")
                flashcard = False
        else:
            if 'h' in str(key):
                print(f"flashcards on \n")
                flashcard = True
    
        if autoclickerBool:
            if 'g' in str(key):
                print("auto clicker off\n")
                autoclickerBool = False
        else:
            if 'g' in str(key):
                print("auto clicker on\n")
                autoclickerBool = True
        if "f8" in str(key):
            print("Restricing access\n")
            flashcard = False
            autoclickerBool = False
            access = False
    else:
        if 'f8' in str(key):
            print("Granting access\n")
            access = True

flashcard = False
autoclickerBool = False
access = False

threadFlashcard = threading.Thread(target=flashcards)
threadClicker = threading.Thread(target=autoclicker)
threadFlashcard.start()
threadClicker.start()

print(mess)
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
    
