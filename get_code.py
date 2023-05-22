def get_code(wait_time, mode):
    print(f"You have {wait_time} seconds to enter your code editor!")
    print("After that, just let the computer do the work!")
    print("Remember, once the time is up, you will not be able to stop it!")
    time.sleep(wait_time)

    url = get_url(mode)
    code_returns = requests.get(url).text

    for line in code_returns.splitlines():
        for char in line:
            pyautogui.press(char)
        pyautogui.press('enter')
