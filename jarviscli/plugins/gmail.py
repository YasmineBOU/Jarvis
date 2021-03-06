import smtplib                                               # import stmplib
from plugin import plugin                                    # import plugin


@plugin('gmail')                                             # decorator
def gmail(jarvis, s):
    '''
    Sending email from a gmail account using SMTP services.
    To use this plugin :
                1. User should have a gmail id.
                2. Less secure apps should be allowed to access the gmail account.
    '''
    try:
        # establshing server connection
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        print("SERVER CONNECTED")
    except BaseException:
        # in case of failure
        print("Could Not connect to Gmail")
        return
    user = input("Enter User id\n")                          # YOUR ID
    Pass_w = input("\nEnter your Password\n")                # YOUR Password
    reciever_id = input("\nEnter reciever id\n")             # Reciever ID
    msg = input("\nEnter message\n")                         # message

    try:
        server.login(user, Pass_w)                           # user log in
        print("User Logged in")
    except BaseException:
        print(
            '''Allow Less secure apps in GOOGLE ACCOUNT SETTINGS to use SMTP services by following the given steps:
                                                                      \n\t\tStep 1. Log in to email using your browser.
                                                                      \n\t\tStep 2. Go to account settings.
                                                                      \n\t\tStep 3. Find 'allow less secure apps' and mark it as ON.''')
        server.quit()
        exit()
    server.sendmail(user, reciever_id, msg)
    print("MAIL sent")                                       # confirmation
    print("Closing Connection")
    # closing server connection
    server.quit()
    print("Server closed")
