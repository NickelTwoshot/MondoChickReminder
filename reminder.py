from win10toast import ToastNotifier
import schedule
import time

toaster = ToastNotifier()

def notify():
    toaster.show_toast(
        "Im over here swarming my shit 😭🙏",
        "Mondo Chick bout to spawn twin 💔🥀. go get that bag 🤑",
        duration=30,  # seconds the toast stays visible
        threaded=True
    )


# - every hour at :58
schedule.every().hour.at(":58").do(notify)

def running():
    toaster.show_toast(
        "The script is running!",
        "You should get notified 2 minutes before Mondo Chick Spawns! :3",
        duration=30,  # seconds the toast stays visible
        threaded=True
    )

running()
while True:
    schedule.run_pending()
    time.sleep(1)

# actual notification lmfao
#notify()