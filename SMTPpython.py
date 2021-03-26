import smtplib

def smtp_client():
    smtp_object = smtplib.SMTP("172.30.42.127",25)
    try:
        message = "\b this is my beautiful message"
        smtp_object.sendmail("me@example.com","bob@godon.com", message)
        print("Finished sending message")
    except Exception as e:
        print("Unable to send message: ",e)
    smtp_object.quit()


if __name__ == "__main__":
    smtp_client()
