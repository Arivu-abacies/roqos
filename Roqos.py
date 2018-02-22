from flask import render_template,Flask
from flask_ask import Ask,question,statement,audio,session
import twilio.rest
from twilio.rest import Client
import boto3


app = Flask(__name__)
ask = Ask(app, "/")

account_sid='AC38bd38931db4e7a783f7c8fdcee5abe9'		   
auth_token='c4a0e6903aa7a0edcec2e38c478f6780'
client = Client(account_sid, auth_token)

dynamodb = boto3.resource('dynamodb',aws_access_key_id='AKIAJRQEZIFRY4M7QTTA',aws_secret_access_key='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',region_name='us-east-1')
table = dynamodb.Table('Roqos')
Link_List=[]
card_title = "Roqos"
small = "https://s3.amazonaws.com/test-5/Small.png"
#large = "https://s3.amazonaws.com/test-5/Large.png"

@app.route('/')
def welcome():
    welcome_msg="Welcome to Roqos"
    return welcome_msg

@ask.launch
@ask.intent("WelcomeIntent")
def launching():
    launch_message = "Roqos.  How can I help? If you are having an issue, just describe it to me and I will do my best to answer you. "
    return question(launch_message).standard_card(title=card_title, text=launch_message, small_image_url=small)


@ask.intent('colorintent')
def colored(color):
    card_title="Roqos"
    if color == 'different colors':
        DBcolor = color
    elif color == 'white':
        DBcolor = color
    elif color == "red":
        DBcolor =  color
    elif color == "blinking red":
        DBcolor =  color
    elif color == "blue":
        DBcolor =  color
    else:
        DBcolor = "different colors"
    color_msg=DBcolor.title()
    response=table.get_item(Key={'Issue' : color_msg})
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details,  small_image_url=small)

@ask.intent('FiosIntent')
def FIOS():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'FIOS'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details,  small_image_url=small)

@ask.intent('BoostwifiIntent')
def Boost_WiFi():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'Boost WIFI'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details, small_image_url=small)

@ask.intent('KidsvpnIntent')
def Kids_VPN():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'Kids VPN'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details,  small_image_url=small)

@ask.intent('VpninIntent')
def VPN_IN():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'VPN IN'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details,  small_image_url=small)

@ask.intent('RoqosserviceIntent')
def Roqos_Service():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'Roqos Service'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details,  small_image_url=small)

@ask.intent('RoqoscoreIntent')
def Roqos_Core():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'Roqos Core'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details,  small_image_url=small)

@ask.intent('KrackwifiIntent')
def Krack_WiFi():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'KRACK WIFI'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details,  small_image_url=small)

@ask.intent('KrackwifiIntent')
def Krack_WiFi():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'KRACK WIFI'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details,  small_image_url=small)

@ask.intent('WirelessmeshIntent')
def Wireless_Mesh():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'Wireless Mesh'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,details,  small_image_url=small)

@ask.intent('VPNconnectionIntent')
def VPN_Connection():
    card_title = "Roqos"
    response=table.get_item(
    Key={
    'Issue' : 'VPN Connection'
    }
    )
    item = response['Item']
    details = item['Description']
    Link_List.append(item['Link'])
    return question("{}. Did you want me to send you more details?".format(details)).standard_card(card_title,  small_image_url=small)

@ask.intent('NoIntent')
def No():
    return statement(" ").standard_card(card_title, small_image_url=small)

@ask.intent('AMAZON.StopIntent')
def Stop():
    return statement(" ").standard_card(card_title, small_image_url=small)

@ask.intent('AMAZON.CancelIntent')
def Cancel():
    return statement(" ").standard_card(card_title, small_image_url=small)

@ask.intent('AMAZON.HelpIntent')
def Help():
    return question("Roqos.  How can I help? If you are having an issue, just describe it to me and I will do my best to answer you. ").standard_card(card_title, small_image_url=small)

@ask.intent('YesIntent')
def Yes():
    try:
        table = dynamodb.Table('Roqos_Mobile_Number')
        user_id=session.user.get('userId')
        DB_User = table.get_item(Key={'User ID':user_id})
        DB_Item = DB_User['Item']
        DB_Number = DB_Item['Phone Number']
        client.api.account.messages.create(to="+918073425687",from_='+17042702074',body = Link_List[-1])
        Yes_msg="Ok. Just texted you a link with more information.  Anything else?"
        return question(Yes_msg).standard_card(card_title,Yes_msg,  small_image_url = small)
    except:
        Yes_msg=" Oops.  Looks like I don’t have your cell phone number.  If you are good, please go ahead and tell me whats your cell phone number is."
        return question(Yes_msg).standard_card(card_title,Yes_msg,  small_image_url = small)


@ask.intent('PhoneNumberIntent')
def Phone_Number(Number):
    try: 
        table = dynamodb.Table('Roqos_Mobile_Number')
        user_id = session.user.get('userId')
        table.put_item(Item={'User ID':user_id,'Phone Number':Number})
        dictionary = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",'7': "seven", '8': "eight", '9': "nine", '0': "zero"}
        new_my_number = ",".join(map(lambda x: dictionary[x], str(Number)))
        return question("{} Right? ".format(new_my_number)).standard_card(card_title, small_image_url="https://s3.amazonaws.com/test-5/R1000px+(1).png")
    except:
        return question("I dint get that please repeat").standard_card(card_title,  small_image_url=small)

@ask.intent('SupportIntent')
def Support():
    try: 
        table = dynamodb.Table('Roqos_Mobile_Number')
        user_id=session.user.get('userId')
        DB_User = table.get_item(Key={'User ID':user_id})
        DB_Item = DB_User['Item']
        DB_Number = DB_Item['Phone Number']
        client.api.account.messages.create(to="+918073425687",from_='+17042702074',body="Customer Care Mobile number!")
        return question("Sure.  Just texted you the phone number.  Please click on it to speak with someone Roqos customer care. Anything else?").standard_card(card_title,  small_image_url=small)
    except:
        Yes_msg=" Oops.  Looks like I don’t have your cell phone number.  If you are good, please go ahead and tell me whats your cell phone number is."
        return question(Yes_msg).standard_card(card_title,Yes_msg,  small_image_url = small)
    
@ask.session_ended
def session_ended():
    return "{}", 200

if __name__=='__main__':
    app.run(debug=True)
