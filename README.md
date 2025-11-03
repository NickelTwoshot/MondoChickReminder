# MondoChickReminder

> [!CAUTION]
> This code is very basic, VERY BAD, and throw together at 11 pm with barely any knowledge of Python. Use at your own risk. ReadMe might also be incomplete and missing libraries you need for this project.

> [!NOTE]
> This script has only been tested on Windows 10. it MIGHT work on Windows 11, But is NOT offically supported on any platforms other then Windows 10 (This includes Windows 8 or older, Windows 11 or Newer, Mac Os, Linux, BSD, Etc etc...)


a VERY basic Python script that will send a push notification 2 minutes before Mondo Chick spawns in Bee Swarm Simulator. 


![A screenshot of a Windows 10 Notification using the script that is provided in this Repository.](/images/notif.png) 

To use this script you will need to install a few libraries through python. 
With Python 3 Already installed go to a Command Prompt and type the following

```
pip install win10toast schedule pylance
```

One done, Download and run the script
You should be able to run the python file without issues.
Here is an example command to run the file (assuming the file is in Downloads)
```
python C:\Users\YOURUSER\Downloads\reminder.py
```
Adjust this command for the saved file location
Side note: Python has been weird for me. You MIGHT need to replace `python` with `python3` for it to work.

Once you run the script you should get a confirmation Notification saying the script is running
![a notification confirming my script is running](/images/running.png)

To stop this script press `Ctrl+C` while focused into your Command Prompt Window

The end :)
