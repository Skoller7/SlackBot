class Commands:

    def __init__(self, channel):
        self.channel = channel
        self.username = "chatbot_v1"
        self.icon_emoji = ":robot_face:"
        self.timestamp = ""
    


    def get_message_help(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.HELP_BLOCK,
                self.DIVIDER_BLOCK,
                self.SELECTION_BLOCK,
                #self.INTERACTIVE_SELECTION_BLOCK,
                self.DIVIDER_BLOCK
            ],
        }


    def get_sentiment(self, sentiment):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*We noticed your are a little bit " + sentiment + " lately :pensive:. Do you want to have a chat?*"
					}
				},
				self.APPORVE_ACTION_BLOCK
            ],
        }

####################### All data block ########################
    HELP_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Here is a _list_ of all our commands:\n"
                "!help, !payment, !trello !meeting"
            )
        }
    }

    DIVIDER_BLOCK = {"type": "divider"}

    SELECTION_BLOCK = {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Here are some suggestions"
                },
                "accessory": {
                    "action_id": "action_helpme",
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select an item",
                        "emoji": True
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": ":memo: Trello help",
                                "emoji": True
                            },
                            "value": "!trello"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": ":date: Meeting help",
                                "emoji": True
                            },
                            "value": "!meeting"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": ":money_with_wings: Payment help",
                                "emoji": True
                            },
                            "value": "!review"
                        },
                                                {
                            "text": {
                                "type": "plain_text",
                                "text": ":robot_face: Sentiment Analysis",
                                "emoji": True
                            },
                            "value": "!sentiment"
                        },
                    ]
                }
            }

    APPROVE_INFO_BLOCK = {
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "*We noticed a certain sentiment analyse. Do you want us to contact HR?*"
			}
	}

    APPORVE_ACTION_BLOCK = 		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Yes! Lets have a chit chat"
					},
					"style": "primary",
					"action_id": "approve_request_sentiment"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "No I dont like to talk."
					},
					"style": "danger",
					"action_id": "deny_request_sentiment"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "More info"
					},
					"action_id": "request_info_sentiment"
				}
			]
		}
    
    def get_approved_sentiment(self):
        view = {
            "type": "modal",
            "title": {
                "type": "plain_text",
                "text": "Sentiment",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": True
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Waar situeert het probleem zich?"
                    },
                    "accessory": {
                        "type": "multi_static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Kies opties",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Externe werkplek",
                                    "emoji": True
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Privé probleem",
                                    "emoji": True
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Andere",
                                    "emoji": True
                                },
                                "value": "value-2"
                            }
                        ]
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Wil je er iets over kwijt?",
                        "emoji": True
                    }
                }
            ]
        }
        return view
