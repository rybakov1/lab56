from bottle import post, request
import re

@post('/meow', method='post')
def my_form():
    print(check_mob())

    mail = request.forms.get('ADDRESS')
    question = request.forms.get('QUESTION')

    pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})'  
    correctMail = re.match(pattern, mail, flags=re.IGNORECASE)
    if (correctMail is None):
        message = "Email input is incorrect!"
    else:
        message = "Thanks! The answer will be sent to the mail {}".format(mail)
    return message

def check_mob():
    mobile_reg = '\+7\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}'
    mobile = '+7 (911) 123-21-31' 
    correct_tel = re.match(mobile_reg, mobile)
    if(correct_tel is None):
        return "NotFine"
    else:
        return "Fine"