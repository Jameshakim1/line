from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('1lyb002v13710iCw4x7ps5w26An9Bm+zNQ9cix11SD9uex2FfP7RuNlrfFfSkpGYPaLv1YmkOaxRwjw7cQ6oiJOguZFNFQklwOK678TfP0XqhwJqxeZX6UQlDy+3g6/czJ4GsuaIwAlRQi9yUGmuK1GUYhWQfeY8sLGRXgo3xvw=')
# Channel Secret
handler = WebhookHandler('8f73e4e50a53d0e4ab2d90c262657143')
#===========[ NOTE SAVER ]=======================
notes = {}

# Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)

def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get user_id
    gid = event.source.sender_id #get group_id
#=====[ LEAVE GROUP OR ROOM ]==========
    if text == 'bye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Leaving group'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
#=====[ TEMPLATE MESSAGE ]=============
    elif text == '.fot':
                                    message  = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://scontent.fkul7-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51142161_1056866164498689_6048546161705353216_o.jpg?_nc_cat=111&efg=eyJpIjoidCJ9&_nc_ht=scontent.fkul7-1.fna&oh=b9ca383a51fed38a4e20842cf1b4078d&oe=5CF5692B",
        "action": {
          "uri": "http://line.me/ti/p/~jameshakim1",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "body": {
        "contents": [
          {
            "text": "?????KF°?????\n\n    ? ???? ????? ?\n???? ??????? ???? ?????\n?s?????? & ??3?\n\n? Selfbot only.\n? 1 Sb + 3 assist.\n? 1 Sb + 5 assist.\n? 1 Sb + 10 assist.\n\n???? ?????..\n????? kepoin aja ?? ???? :\n ? ? line.me/ti/p/~jameshakim1 ?\n ? ? line.me/ti/p/~afex123 ?",
            "wrap": True,
            "gravity": "center",
            "flex": 0,
            "color": "#F0F8FF",
            "type": "text",
            "size": "sm"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "header": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "s??? ???? ????",
            "weight": "bold",
            "color": "#ffffff",
            "size": "sm",
            "action": {
              "type": "uri",
              "label": "link",
              "uri": "http://line.me/ti/p/~jameshakim1"
            },
            "align": "center"
          }
        ]
      },
      "type": "bubble",
       "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#e71c2c"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "TAP HERE TO ORDER",
            "weight": "bold",
            "color": "#ffffff",
            "size": "sm",
            "action": {
              "type": "uri",
              "label": "link",
              "uri": "http://line.me/ti/p/~jameshakim1"
            },
            "align": "center"
          }
        ]
      }
    },
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://scontent.fkul7-1.fna.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/51142161_1056866164498689_6048546161705353216_o.jpg?_nc_cat=111&efg=eyJpIjoidCJ9&_nc_ht=scontent.fkul7-1.fna&oh=b9ca383a51fed38a4e20842cf1b4078d&oe=5CF5692B",
        "action": {
          "uri": "http://line.me/ti/p/~jameshakim1",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "body": {
        "contents": [
          {
            "text": "???????????????????\n?           ??   ?????\n???????????????????\n?     ???? ???? ????? \n?\n? 1000 c      => 75 k\n? 500 c.       => 40 k\n? 100 c.      => 9 k\n???????????????????",
            "wrap": True,
            "gravity": "center",
            "flex": 0,
            "color": "#F0F8FF",
            "type": "text",
            "size": "sm"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "header": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "s??? ???? ????",
            "weight": "bold",
            "color": "#ffffff",
            "size": "sm",
            "action": {
              "type": "uri",
              "label": "link",
              "uri": "http://line.me/ti/p/~jameshakim1"
            },
            "align": "center"
          }
        ]
      },
      "type": "bubble",
       "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#e71c2c"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "TAP HERE TO ORDER",
            "weight": "bold",
            "color": "#ffffff",
            "size": "sm",
            "action": {
              "type": "uri",
              "label": "link",
              "uri": "http://line.me/ti/p/~jameshakim1"
            },
            "align": "center"
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                    line_bot_api.reply_message(event.reply_token, message)
    elif text == '.foto':
        message = ImagemapSendMessage(
            base_url='https://assets.digicorus.corusdigitaldev.com/wp-content/uploads/sites/19/2018/06/04133345/CartoonNetwork_Ben10_462x386.jpg/base',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                URIImagemapAction(
                    link_uri='https://assets.digicorus.corusdigitaldev.com/wp-content/uploads/sites/19/2018/06/04133345/CartoonNetwork_Ben10_462x386.jpg',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=1040
                    )
                ),
                MessageImagemapAction(
                    text='hello',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=1040
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == '/ca':
        message = TextSendMessage(text='Hello, world')
        line_bot_api.reply_message(event.reply_token, message)
    elif text == '/template':
        buttons_template = TemplateSendMessage(
            alt_text='template',
            template=ButtonsTemplate(
                title='[ TEMPLATE MSG ]',
                text= 'Tap the Button',
                actions=[
                    MessageTemplateAction(
                        label='Culum 1',
                        text='/aditmadzs'
                    ),
                    MessageTemplateAction(
                        label='CULUM 2',
                        text='/aditmadzs'
                    ),
                    MessageTemplateAction(
                        label='CULUM 3',
                        text='/aditmadzs'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
#=====[ CAROUSEL MESSAGE ]==========
    elif text == '/carousel':
        message = TemplateSendMessage(
            alt_text='OTHER MENU',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='ADD ME',
                        text='Contact Aditmadzs',
                        actions=[
                            URITemplateAction(
                                label='>TAP HERE<',
                                uri='https://line.me/ti/p/~adit_cmct'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Instagram',
                        text='FIND ME ON INSTAGRAM',
                        actions=[
                            URITemplateAction(
                                label='>TAP HERE!<',
                                uri='http://line.me/ti/p/~adit_cmct'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=====[ FLEX MESSAGE ]==========
    elif text == 'flex':
        bubble = BubbleContainer(
            direction='ltr',
            hero=ImageComponent(
                url='https://lh5.googleusercontent.com/VoOmR6tVRwKEow0HySsJ_UdrQrqrpwUwSzQnGa0yBeqSex-4Osar2w-JohT6yPu4Vl4qchND78aU2c5a5Bhl=w1366-h641-rw',
                size='full',
                aspect_ratio='20:13',
                aspect_mode='cover',
                action=URIAction(uri='http://line.me/ti/p/~adit_cmct', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='Aditmadzs', weight='bold', size='xl'),
                    # review
                    BoxComponent(
                        layout='baseline',
                        margin='md',
                        contents=[
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/gold_star.png'),
                            IconComponent(size='sm', url='https://example.com/grey_star.png'),
                            TextComponent(text='4.0', size='sm', color='#999999', margin='md',
                                          flex=0)
                        ]
                    ),
                    # info
                    BoxComponent(
                        layout='vertical',
                        margin='lg',
                        spacing='sm',
                        contents=[
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Place',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text='Tangerang, Indonesia',
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5
                                    )
                                ],
                            ),
                            BoxComponent(
                                layout='baseline',
                                spacing='sm',
                                contents=[
                                    TextComponent(
                                        text='Time',
                                        color='#aaaaaa',
                                        size='sm',
                                        flex=1
                                    ),
                                    TextComponent(
                                        text="10:00 - 23:00",
                                        wrap=True,
                                        color='#666666',
                                        size='sm',
                                        flex=5,
                                    ),
                                ],
                            ),
                        ],
                    )
                ],
            ),
            footer=BoxComponent(
                layout='vertical',
                spacing='sm',
                contents=[
                    # separator
                    SeparatorComponent(),
                    # websiteAction
                    ButtonComponent(
                        style='link',
                        height='sm',
                        action=URIAction(label='Aditmadzs', uri="https://line.me/ti/p/~adit_cmct")
                    )
                ]
            ),
        )
        message = FlexSendMessage(alt_text="hello", contents=bubble)
        line_bot_api.reply_message(
            event.reply_token,
            message
        )
#=======================================================================================================================
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
