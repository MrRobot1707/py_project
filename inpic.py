import requests
import instaloader
import webbrowser

username = input("enter username:")
webbrowser.open(f'www.instagram.com/{username}')
#speak(f"sir this is {username} profile")
time.sleep(5)
#speak(f"sir would you like to download profile photo")
condition = TackInput().lower()
if "yes" in condition:
    bot = instaloader.Instaloader()
    bot.download_profile(username,profile_pic_only=True)
    #print('sir profile photo is downloaded)
