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
				"text": "*We noticed a " + sentiment + " :worried:. Do you want us to contact HR?*"
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
                    "action_id": "action",
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
						"text": "Approve"
					},
					"style": "primary",
					"action_id": "approve_request"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "Deny"
					},
					"style": "danger",
					"action_id": "deny_request"
				},
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"emoji": True,
						"text": "More info"
					},
					"action_id": "request_info"
				}
			]
		}
