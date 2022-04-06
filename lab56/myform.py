from bottle import post, request
import re
import json

@post('/meow', method='post')
def my_form():
    print(check_mob())

    mail = request.forms.get('ADDRESS')
    question = request.forms.get('QUESTION')

    saveDataInJson(mail, question)

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

def saveDataInJson(mail, text):
    data = {}
    try:
        with open('data.json') as json_file:
            data = json.load(json_file)
            print('Email: ' + data[mail])
            parsed_mail = data[mail]
    except:
        print("mem")

    if(mail in data):
        data[mail].append(text)
    else:
        data[mail] = [text]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(data)