import pyautogui

whatToDo = input("newtab(n), upload(u), saveshirts(s) color(c)")


def new_tab():
    for x in range(50):
        pyautogui.hotkey('ctrl', 't')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")
        x += 1
    else:
        pyautogui.hotkey("ctrl", "tab", interval=0.5)
        for x in range(50):
            # pressUploadButton
            pyautogui.click(794, 1272, interval=1)
            # leftClickLatestPicture
            pyautogui.click(406, 254, interval=1)
            # deletePic
            pyautogui.press('delete', interval=1)
            pyautogui.click(406, 254, interval=1)
            # pressEnter
            pyautogui.press('enter', interval=15)
            # leftClickLatestPicture();
            # pyautogui.click(406, 254, interval=2)
            # pressopen
            # pyautogui.click(900, 785, interval=2)
            # clickNextTab();
            pyautogui.hotkey("ctrl", "tab", interval=0.5)
            x += 1
        for x in range(50):
            pyautogui.click(1466, 1368, interval=0.5)
            pyautogui.hotkey("ctrl", "tab", interval=0.5)
            x += 1
        for x in range(50):
            pyautogui.click(1819, 720, interval=0.1)
            pyautogui.click(1893, 717, interval=0.1)
            pyautogui.click(1973, 717, interval=0.1)
            pyautogui.click(2062, 703, interval=0.1)
            pyautogui.click(2139, 717, interval=0.1)
            pyautogui.click(2549, 1305, interval=0.3)
            pyautogui.click(1521, 867, interval=0.2)
            pyautogui.hotkey("ctrl", "tab", interval=0.3)
            x += 1
# loop
def upload():
    for x in range(50):
        # pressUploadButton
        pyautogui.click(794, 1272, interval=1)
        # leftClickLatestPicture
        pyautogui.click(406, 254, interval=1)
        # deletePic
        pyautogui.press('delete', interval=1)
        pyautogui.click(406, 254, interval=1)
        # pressEnter
        pyautogui.press('enter', interval=15)
        # leftClickLatestPicture();
        # pyautogui.click(406, 254, interval=2)
        # pressopen
        # pyautogui.click(900, 785, interval=2)
        # clickNextTab();
        pyautogui.hotkey("ctrl", "tab", interval=0.5)
        x += 1
    else:
        print("done")


def save_shirts():
    for x in range(50):
        pyautogui.click(1466, 1368, interval=0.5)
        pyautogui.hotkey("ctrl", "tab", interval=0.5)
        x += 1
    else:
        print("done")


def color():
    for x in range(50):
        pyautogui.click(1819, 720, interval=0.1)
        pyautogui.click(1893, 717, interval=0.1)
        pyautogui.click(1973, 717, interval=0.1)
        pyautogui.click(2062, 703, interval=0.1)
        pyautogui.click(2139, 717, interval=0.1)
        pyautogui.click(2549, 1305, interval=0.3)
        pyautogui.click(1521, 867, interval=0.2)
        pyautogui.hotkey("ctrl", "tab", interval=0.3)
        x += 1
    else:
        print("done")


if whatToDo == "u":
    upload()

if whatToDo == "c":
    color()

if whatToDo == "s":
    save_shirts()

if whatToDo == "n":
    new_tab()
