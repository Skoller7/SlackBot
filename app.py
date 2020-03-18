import os
import logging
import json
from flask import Flask
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from slack import WebClient
from slackeventsapi import SlackEventAdapter
import ssl as ssl_lib
import certifi
from commands import Commands

#Setting up flask to host the chatbot:
app = Flask(__name__)
CORS(app)

#To retrieve messages from the /Slack/events url.
slack_events_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/slack",app)

#TODO omzetten naar een export.
verification_token = "WHUrKOg6hBfeYZMoyiddfzNO"

#to retrieve interactive components (buttons clicked, dates added to calender etc) TODO: implement it, atm still un-needed.
slack_interactive_endpoint_adapter = SlackEventAdapter(os.environ['SLACK_SIGNING_SECRET'], "/interactive-endpoint")

slack_web_client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

listOfNames = { 'aaron', 'alexey', 'anissa', 'anouchka', 'attila', 'axel', 'bart', 'ben', 'bert', 'berten', 'bianca', 'cathy', 'cedric', 'chantal', 'christophe', 'dario', 'dary', 'dave', 'dennis', 'didier', 'dieter', 'domien', 'dylan', 'eline', 'ellen','fabio','farhood', 'ferra', 'frederik', 'hadrien', 'hilde', 'jan', 'jasper', 'jef', 'jello', 'jens', 'jeroen', 'joachim', 'joel', 'johan', 'jonas', 'joost', 'jorne' , 'julie', 'kevin', 'kim', 'koen', 'kristof', 'kurt', 'luca', 'maarten', 'mario', 'mathias', 'maurice', 'melissa', 'michael', 'nick', 'nicky', 'nico', 'niels', 'oliver', 'peter', 'philip', 'pieter-jan', 'robin', 'roeland', 'ruben', 'rubin', 'sarah', 'seb', 'sigrid', 'stephanie', 'theriessa', 'thierry', 'tom', 'torsten', 'vincent', 'wesley', 'yannick'}

#/helpme command.
@app.route('/slack/helpme', methods=['POST'])
def helpme():
    #If this comes from slack & it has the bot verification token then.
    if request.form['token'] == verification_token:
        commands = Commands(request.form['channel_id'])
        message = commands.get_message_help()
        return message


#/sentiment command.
@app.route('/slack/sentiment', methods=['POST'])
def sentiment():
    #If this comes from slack & it has the bot verification token then.
    if request.form['token'] == verification_token:
        commands = Commands(request.form['channel_id'])
        message = commands.get_sentiment("down")
        return message



# ============= Interactive components ============= #
# When a user clicks on interactive blocks
# an example of this is the !help block where they will chose a select click.
# After clicking on the slecect you will get pointed to the next bot action.

#Interactive endpoint for when a use clicks on an interactive endpoint
@app.route('/interactive-endpoint', methods=['POST'])
def find_replies():
    
    #We have to turn the obtained string into a json object to obtain 
    #the data that is inside.
    message = json.loads(request.form['payload'])
    
    #BLOCK interaction and also check if verification token is correct.
    if message['type'] == 'block_actions' and message['token'] == verification_token:    

        print('message of block action:')
        print(message)
        #actions is a list so we also parse that.
        message_action = message['actions'][0]
        
        #declaration of the input json
        channel_id = message['container']['channel_id']
        message_ts = message['container']['message_ts']
        user_id = message['user']['id']
        trigger_id = message['trigger_id']
       
        print('message_action:')
        print(message_action)
        #Here we check what kind of message it is. This is from an option menu.
        #An example of this is the /helpme command.
        #info locals: https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
        if message_action['action_id'] == 'action_helpme':
            #this is how we get the value out of it.
            message_value = message_action['selected_option']['value']
            #here we check what value is inside of it and create interactivity
            if message_value == '!trello':

                #you can also return the user id so it send him a pm.
                commands = Commands(user_id)
                message = commands.get_message_trello()
                answer = slack_web_client.chat_postMessage(
                    channel = user_id,
                    text="Here is some information of how i can be used with Trello:"
                )
                return ("",200)

            elif message_value == '!review':
                commands = Commands(user_id)
                message = commands.get_message_review()
                slack_web_client.chat_postMessage(**message)
                return ("",200)
            elif message_value == '!meeting':
                commands = Commands(user_id)
                message = commands.get_meeting_planner()
                slack_web_client.views_open(
                    trigger_id = trigger_id,
                    view =  message
                )
                return ("",200)
            elif message_value == '!sentiment':
                commands = Commands(user_id)
                message = commands.get_sentiment_modal()
                slack_web_client.views_open(
                    response_action = "clear",
                    trigger_id = trigger_id,
                    view = message
                )
                return ("",200)
            #if it is this action we know its a "approve block"
        elif message_action['action_id'] == 'approve_request_sentiment':
                #Show sentiment approval modal.
                commands = Commands(user_id)
                message = commands.get_approved_sentiment()
                slack_web_client.views_open(
                    trigger_id = trigger_id,
                    view = message
                )
                return("",200)
        elif message_action['action_id'] == 'deny_request_sentiment':
            #if they dont want to submit a form.
            commands = Commands(user_id)
            message = commands.get_feedback_block()
            slack_web_client.chat_postMessage(**message)
            return ("",200)
        

    #check if it comes from a submitted modal & accept verification token
    elif message['type'] == 'view_submission' and message['token'] == verification_token:

        print('message of view submission')
        #retrieve the title of the modal to know which one it is.
        submit_name = message['view']['title']['text']
        test = message['view']['state']['values'].values()

        user_id = message['user']['id']
        trigger_id = message['trigger_id']
        print("trigger Id :")
        print(trigger_id)
        
        #if then name of the modal is sentiment then do this if statement.
        if submit_name == "Sentiment":
            #nadenken over wat we met die info willen doen
            #bericht sturen naar HR? Indien ja navragen aan persoon
            #of dat oké is ,....
            """commands = Commands(user_id)
            messageZ = commands.get_specific_sentiment_info()
            slack_web_client.views_push(
                response_action = "push",
                trigger_id = trigger_id,
                view = messageZ
            )"""
            return("",200)

        
    else:
        return  ("",200)