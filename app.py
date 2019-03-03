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
line_bot_api = LineBotApi('hgvBBYgaY0OoJoA02eGD8I9PXQZoxvm+SVF+iPRbrejxxyvZ/5sKM4if2Jvnf2c72Wp6JOHp6fx/prQS4R9x1ecA2g24fykgisPDrGmRQuP6NZdqjowa07VJzVp9SobMl8Hi6z/DXYh2LAfRm7zdywdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('62e1960b9f0f2b84ec8869e0a7825a25')
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
    if text == "/kick":
        line_bot_api.kickoutFromGroup(0, gid, "u2a61372cacb6e89afa01194d7e8f52d2")
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
    if text == '/contact':
        buttons_template_message = TemplateSendMessage(
            alt_text='God message',
            template=ButtonsTemplate(
                thumbnail_image_url='https://gamingroom.co/wp-content/uploads/2017/11/CyCYOArUoAA2T6d.jpg',
                title='??????',
                text='????????????????',
                actions=[
                    PostbackAction(
                        label='????',
                        text='http://line.me/ti/p/~esci_',
                        data='action=buy&itemid=1'
                    ),
                    MessageAction(
                        label="???????",
                        text='https://www.facebook.com/pasun.cf'
                    ),
                    URIAction(
                        label='??????',
                        uri='http://line.me/ti/p/~esci_'
                    )
                ]
            )
        )
        line_bot_api.push_message(gid, buttons_template_message)
    elif text == '/ca':
        message = TextSendMessage(text='Hello, world')
        line_bot_api.reply_message(event.reply_token, message)
    elif text == 'Asem':
        message = TextSendMessage(text='Dirimu yg asem')
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
                        text='/JamesHakim'
                    ),
                    MessageTemplateAction(
                        label='CULUM 2',
                        text='/JamesHakim'
                    ),
                    MessageTemplateAction(
                        label='CULUM 3',
                        text='/JamesHakim'
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
                        text='Contact JamesHakim',
                        actions=[
                            URITemplateAction(
                                label='>TAP HERE<',
                                uri='line://nv/profilePopup/mid=uc66a26f635ba47a1e95174652660585f'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='Instagram',
                        text='FIND ME ON INSTAGRAM',
                        actions=[
                            URITemplateAction(
                                label='>TAP HERE!<',
                                uri='line://nv/profilePopup/mid=uc66a26f635ba47a1e95174652660585f'
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
                action=URIAction(uri='line://nv/profilePopup/mid=uc66a26f635ba47a1e95174652660585f', label='label')
            ),
            body=BoxComponent(
                layout='vertical',
                contents=[
                    # title
                    TextComponent(text='JamesHakim', weight='bold', size='xl'),
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
                        action=URIAction(label='JamesHakim', uri="line://nv/profilePopup/mid=uc66a26f635ba47a1e95174652660585f")
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
