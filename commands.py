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