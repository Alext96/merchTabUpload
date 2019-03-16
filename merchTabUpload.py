import pyautogui
#print(pyautogui.position())

#loop
for x in range(15):
    #pressUploadButton
    pyautogui.click(794, 1272, interval=0.5)
    #leftClickLatestPicture
    pyautogui.click(406, 254, interval=0.5)
    #deletePic
    pyautogui.press('delete', interval=0.5)
    pyautogui.click(406, 254, interval=0.5)
    #pressEnter
    pyautogui.press('enter', interval=15)
    #leftClickLatestPicture();
    #pyautogui.click(406, 254, interval=2)
    #pressopen
    #pyautogui.click(900, 785, interval=2)
    #clickNextTab();
    pyautogui.hotkey("ctrl", "tab", interval=0.5)
    x += 1
else:
    print("done")