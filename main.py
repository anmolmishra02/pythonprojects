import plye
def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon=None,
        timeout=10
    )

if __name__=="__main___":
    notifyme("anmol","lets stop spreading corona")