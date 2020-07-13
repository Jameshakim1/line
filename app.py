import errno
import os
import sys
import tempfile
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json

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
line_bot_api = LineBotApi('mN8qrP9onpESOTeipdHGcJC784WBRGzGJX9fppahkW771sGoRWukgxU8RHL1UnPaI47rkKw5R3eKeGWa56j2rQeH3N2VujeV5MNqOXrTBqywufkWGe19iO7aoB/ZVXf66OcGuCvtxDLqF71a2lK20FGUYhWQfeY8sLGRXgo3xvw=')
# Channel Secret
handler = WebhookHandler('799bf266406c0e613fdb6ef9caf901cd')
#===========[ NOTE SAVER ]=======================
notes = {}
tokenz = {}

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

@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,[
                TextSendMessage(text='Makasih Udah Invite Saya'),
                TextSendMessage(text='https://jamsblogaddress.blogspot.com/?m=1')
        ])
    
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get user_id
    gid = event.source.sender_id #get group_id
    
#=====[ LEAVE GROUP OR ROOM ]==========[ ARSYBAI ]======================
    
    
    if text == '.pamit.':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Aku pamit ya, bye bye'),
                    TextSendMessage(text='https://jamsblogaddress.blogspot.com/?m=1')
                ])
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='aku pergi bye-bye'),
                    TextSendMessage(text='https://jamsblogaddress.blogspot.com/?m=1')
                ])
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
#=====[ TES MESSAGE ]=============[ ARSYBAI ]======================
    if text == "/profile":
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.push_message(gid,TextSendMessage(text=event.source.user_id))
        line_bot_api.push_message(gid,TextSendMessage(text=profile.display_name))
        line_bot_api.push_message(gid,TextSendMessage(text=profile.status_message))
        line_bot_api.push_message(gid,TextSendMessage(text=profile.picture_url))
    if text == '/id':
        profile = line_bot_api.get_profile(event.source.user_id)
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.display_name))
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.source.user_id))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.picture_url))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.status_message))
    if text == '/bio':
        profile = line_bot_api.get_profile(event.source.user_id)
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.display_name))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.source.user_id))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.picture_url))
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.status_message))
    if text == '/pic':
        profile = line_bot_api.get_profile(event.source.user_id)
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.display_name))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.source.user_id))
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.picture_url))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.status_message))
    if text == '/name':
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.display_name))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.source.user_id))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.picture_url))
        #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=profile.status_message))
    if text == "redtube on":
    	angka = random.randint(1, 200)
    	r = requests.get('https://api.boteater.vip/redtube?page={}'.format(angka))
    	data=r.text
    	data=json.loads(data)
    	for anu in data["result"]:
        	line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))
    elif text == "xvideos on":
    	angka = random.randint(1, 200)
    	r = requests.get('https://api.boteater.vip/xvideos?page={}'.format(angka))
    	data=r.text
    	data=json.loads(data)
    	for anu in data["result"]:
    		line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))
#=====[ TES MESSAGE ]=============[ ARSYBAI ]======================
    elif text == 'confirm':
        confirm_template = ConfirmTemplate(text='Bot nya bagus?', actions=[
            MessageTemplateAction(label='Yes', text='Yes!'),
            MessageTemplateAction(label='No', text='No!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)
    elif "/idline: " in event.message.text:
        skss = event.message.text.replace('/idline: ', '')
        sasa = "http://line.me/R/ti/p/~" + skss
        text_message = TextSendMessage(text=sasa)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/acaratv: " in event.message.text:
        skss = event.message.text.replace('/acaratv: ', '')
        url = requests.get("https://rest.farzain.com/api/acaratv.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&id="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["result"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/artinama: " in event.message.text:
        skss = event.message.text.replace('/artinama: ', '')
        url = requests.get("https://rest.farzain.com/api/nama.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&q="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["result"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/zodiac: " in event.message.text:
        skss = event.message.text.replace('/zodiac: ', '')
        url = requests.get("https://triopekokbots026.herokuapp.com/zodiak="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["result"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/tr-th: " in event.message.text:
        skss = event.message.text.replace('/tr-th: ', '')
        url = requests.get("https://api.tanyz.xyz/translateText/?&to=th&text="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["Hasil"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/tr-en: " in event.message.text:
        skss = event.message.text.replace('/tr-en: ', '')
        url = requests.get("https://api.tanyz.xyz/translateText/?&to=en&text="+ skss)
        data = url.json()
        text_message = TextSendMessage(text=data["Hasil"])
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/jawa " in event.message.text:
        skss = event.message.text.replace('/jawa ', '')
        url = requests.get("http://ariapi.herokuapp.com/api/trans?key=beta&to=jw&text={}".format(skss))
        data = url.json()
        text_message = TextSendMessage("{}".format(data["result"]["translated"]))
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
        
    elif "/fs1: " in event.message.text:
        skss = event.message.text.replace('/fs1: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=rambu&text=' + skss,
        preview_image_url='https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=rambu&text=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/fs2: " in event.message.text:
        skss = event.message.text.replace('/fs2: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=rambu&text=' + skss,
        preview_image_url='https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=rambu&text=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/graffiti: " in event.message.text:
        skss = event.message.text.replace('/graffiti: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/photofunia/graffiti_wall.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&text2=Gans&text1=' + skss,
        preview_image_url='https://rest.farzain.com/api/photofunia/graffiti_wall.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&text2=Gans&text1=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/audio: " in event.message.text:
        skss = event.message.text.replace('/audio: ', '')
        message = AudioSendMessage(
        original_content_url=skss,
        duration=60000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/video: " in event.message.text:
        skss = event.message.text.replace('/video: ', '')
        message = VideoSendMessage(
        original_content_url=skss,
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/image: " in event.message.text:
        skss = event.message.text.replace('/image: ', '')
        message = ImageSendMessage(
        original_content_url=skss,
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/linepost: " in event.message.text:
        skss = event.message.text.replace('/linepost: ', '')
        url = requests.get("https://rest.farzain.com/api/special/line.php?&apikey=vhbotsline&id="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["result"],
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/youtubemp4: " in event.message.text:
        skss = event.message.text.replace('/youtubemp4: ', '')
        url = requests.get("https://api.tanyz.xyz/api/ytDown/?link="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["Hasil"]["urls"][0]["id"],
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/youtubemp3: " in event.message.text:
        skss = event.message.text.replace('/youtubemp3: ', '')
        url = requests.get("https://rest.farzain.com/api/ytaudio.php?&apikey=rambu&id="+ skss)
        data = url.json()
        message = AudioSendMessage(
        original_content_url=data["result"]["webm"],
        duration=60000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/smulevideo: " in event.message.text:
        skss = event.message.text.replace('/smulevideo: ', '')
        url = requests.get("https://api.fckveza.com/getsmule?link={}&apikey=albiansBots".format(str(skss)))
        data = url.json()
        message = VideoSendMessage(
        original_content_url=str(data["result"]["url"]),
        preview_image_url='https://1.bp.blogspot.com/-rLstVoMN8qY/XdtesOntwfI/AAAAAAAAAmI/NBtbsV91_6EL0j4cbO-WD-ZmciZ4CGETwCLcBGAsYHQ/s1600/20191118_203237.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/smuleaudio: " in event.message.text:
        skss = event.message.text.replace('/smuleaudio: ', '')
        url = requests.get("https://api.fckveza.com/getsmule?link={}&apikey=albiansBots".format(str(skss)))
        data = url.json()
        message = AudioSendMessage(
        original_content_url=str(data["result"]["url"]),
        duration=60000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "youtube.com" in event.message.text or "youtu.be" in event.message.text:
        skss = event.message.text.replace("youtu.be/","youtube.com/watch?v=")
        url = requests.get('youtube-dl --format mp4 --output video.mp4 {}'.format(skss))
        vids = "video.mp4"
        time.sleep(2)
        message = VideoSendMessage(
        original_content_url=vids,
        preview_image_url='https://1.bp.blogspot.com/-rLstVoMN8qY/XdtesOntwfI/AAAAAAAAAmI/NBtbsV91_6EL0j4cbO-WD-ZmciZ4CGETwCLcBGAsYHQ/s1600/20191118_203237.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        os.remove("video.mp4")
        return 0
    elif "/music: " in event.message.text:
        skss = event.message.text.replace('/music: ', '')
        url = requests.get("http://api.zicor.ooo/joox.php?song="+ skss)
        data = url.json()
        message = AudioSendMessage(
        original_content_url=data["url"],
        duration=240000
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/light: " in event.message.text:
        skss = event.message.text.replace('/light: ', '')
        url = requests.get("http://api.zicor.ooo/graffiti.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/street: " in event.message.text:
        skss = event.message.text.replace('/street: ', '')
        url = requests.get("http://api.zicor.ooo/streets.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/cookies: " in event.message.text:
        skss = event.message.text.replace('/cookies: ', '')
        url = requests.get("http://api.zicor.ooo/wcookies.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/sletters: " in event.message.text:
        skss = event.message.text.replace('/sletters: ', '')
        url = requests.get("http://api.zicor.ooo/sletters.php?text="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["image"],
        preview_image_url=data["image"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/goimage: " in event.message.text:
        skss = event.message.text.replace('/goimage: ', '')
        url = requests.get("https://api.eater.pw/googleimg?search="+ skss)
        data = url.json()
        message = ImageSendMessage(
        original_content_url=data["result"][0]["img"],
        preview_image_url=data["result"][0]["img"]
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "Corona" in event.message.text or (text == 'corona'):
        r=requests.get("https://api.kawalcorona.com/indonesia")
        data=r.text
        data=json.loads(data)
        ret_ = "「 COVID-19」"
        ret_ += "\nNegara : {}".format(str(data[0]["name"]))
        ret_ += "\nPositif : {}".format(str(data[0]["positif"]))
        ret_ += "\nSembuh : {}".format(str(data[0]["sembuh"]))
        ret_ += "\nMeninggal : {}".format(str(data[0]["meninggal"]))
        text_message = TextSendMessage(text=ret_)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
    elif "/apakah " in event.message.text:
        quo = ('Iya','Tidak','Gak tau','Bisa jadi','Mungkin iya','Mungkin tidak')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
        
    if text == '/tiktok':
        url = requests.get("https://rest.farzain.com/api/tiktok.php?country=jp&apikey=3w92e8nR5eWuDWQShRlh6C1ye&type=json")
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["first_video"],
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/xvideos: " in event.message.text:
        skss = event.message.text.replace('/xvideos: ', '')
        url = requests.get("https://api.boteater.co/xvideos?page="+ skss)
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["result"][0]["dl"],
        preview_image_url='https://i.ibb.co/GFWPRCV/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif (text == 'Bot') or (text == 'bot'):
        message = TextSendMessage(text='Siapa bot? ke bot an lu')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Ping') or (text == 'ping'):
        message = TextSendMessage(text='Pong 􀨁􀄻mantap􏿿')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Respon') or (text == 'respon'):
        message = TextSendMessage(text='Hadir 􀠁􀅢adaapa?􏿿')
        line_bot_api.reply_message(event.reply_token, message)
    
    elif (text == 'Sp') or (text == '.sp') or (text == 'Speed') or (text == '/sp') or (text == '.speed'):
        message = TextSendMessage(text='「 0.003705247497558544 」 second')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mid') or (text == 'mid') or (text == 'Mymid') or (text == 'mymid') or (text == '.mid'):
        message = TextSendMessage(text=event.source.user_id)
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Gid') or (text == 'gid') or (text == 'Groupid') or (text == 'groupid') or (text == '.gid'):
        message = TextSendMessage(text=event.source.sender_id)
        line_bot_api.reply_message(event.reply_token, message)
#=============[ TOKEN ]=============[ ARSYBAI ]======================
    elif (text == '/chromeos') or (text == 'Chromeos'):
        url = requests.get("https://api.eater.pw/token?header=CHROMEOS")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 JamsHakim 」\nKlik Link Dibawah Ini Untuk Login Token Chrome\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/iosipad') or (text == 'Iosipad'):
        url = requests.get("https://api.eater.pw/token?header=IOSIPAD")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 JamsHakim 」\nKlik Link Dibawah Ini Untuk Login Token Iosipad\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/desktopmac') or (text == 'Desktopmac'):
        url = requests.get("https://api.eater.pw/token?header=DESKTOPMAC")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 JamsHakim 」\nKlik Link Dibawah Ini Untuk Login Token Desktopmac\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/desktopwin') or (text == 'Desktopwin'):
        url = requests.get("https://api.eater.pw/token?header=DESKTOPWIN")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 JamsHakim 」\nKlik Link Dibawah Ini Untuk Login Token Desktopwin\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/win10') or (text == 'Win10'):
        url = requests.get("https://api.eater.pw/token?header=WIN10")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 JamsHakim 」\nKlik Link Dibawah Ini Untuk Login Token Win10\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/clova') or (text == 'Clova'):
        url = requests.get("https://api.eater.pw/token?header=CLOVAFRIENDS")
        data = url.json()
        bsy = data['result'][0]['linktkn']
        bsyr = data['result'][0]['linkqr']
        tokenz[event.source.user_id]= bsy
        message = TextSendMessage(text='「 JamsHakim 」\nKlik Link Dibawah Ini Untuk Login Token Clova\n'+bsyr+'\n\nketik /done untuk mendapatkan tokennya')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == '/done') or (text == 'Done'):
        data = tokenz[event.source.user_id]
        cok = requests.get(url = data)
        asu = cok.text
        message = TextSendMessage(text=asu)
        line_bot_api.reply_message(event.reply_token, message)
    
    elif (text == 'Bot') or (text == 'bot'):
        message = TextSendMessage(text='Siapa bot? ke bot an lu')
        line_bot_api.reply_message(event.reply_token, message)
    
    elif text == '.':
        message = TextSendMessage(text='Titik titik amat so high lu')
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Bah') or (text == 'bah'):
        message = TextSendMessage(text='Beh')
        line_bot_api.reply_message(event.reply_token, message)
#=====[ TEMPLATE MESSAGE ]=============[ ARSYBAI ]======================
    elif (text == "!adminlist") or (text == "Adminlist") or (text == "adminlist"):
        message = TemplateSendMessage(
            alt_text="SeGame admin list",
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url="https://i.ibb.co/zhFY7jg/linepy-1548249585-3.jpg",
                        title="SeGame Founder",
                        text="Pendiri SeGame E-sports",
                        actions=[
                            URITemplateAction(
                                label="YunSuh",
                                uri="https://line.me/ti/p/~YunSuh"
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url="https://i.ibb.co/nQkCwXQ/linepy-1547793990-2.jpg",
                        title="SeGame Moderator",
                        text="Pendiri bot official",
                        actions=[
                            URITemplateAction(
                                label="NvStar",
                                uri="https://line.me/ti/p/~kazereborn"
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url="https://i.ibb.co/qgR3DxQ/Screenshot-2.png",
                        title="SeGame Admin",
                        text="Admin SeGame E-sports",
                        actions=[
                            URITemplateAction(
                                label="Abang",
                                uri="https://line.me/ti/p/~rezafaesal22"
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url="https://i.ibb.co/W04LVGR/73316.jpg",
                        title="SeGame Admin",
                        text="Admin SeGame E-sports",
                        actions=[
                            URITemplateAction(
                                label="Penjual Kacang",
                                uri="https://line.me/ti/p/~dya_sudjono"
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == '/help') or (text == 'help') or (text == 'Help'):
        buttons_template = TemplateSendMessage(
            alt_text='Help message',
            template=ButtonsTemplate(
                title='[ HELP MESSAGE ]',
                text= 'Tap the Button',
                actions=[
                    MessageTemplateAction(
                        label='My Creator',
                        text='Me'
                    ),
                    MessageTemplateAction(
                        label='Media',
                        text='/media'
                    ),
                    MessageTemplateAction(
                        label='Musik',
                        text='/musik'
                    ),
                    MessageTemplateAction(
                        label='star bye',
                        text='starbye'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif text == '/media':
        buttons_template = TemplateSendMessage(
            alt_text='Media message',
            template=ButtonsTemplate(
                title='[ MEDIA MESSAGE ]',
                text= '>Tap the Button<',
                actions=[
                    MessageTemplateAction(
                        label='Media 1',
                        text='/media1'
                    ),
                    MessageTemplateAction(
                        label='Media 2',
                        text='/media2'
                    ),
                    MessageTemplateAction(
                        label='Token',
                        text='/listtoken'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif (text == '/media1') or (text == 'media1') or (text == 'Media1'):
        buttons_template = TemplateSendMessage(
            alt_text='Media area',
            template=ButtonsTemplate(
                title='MEDIA COMMAND',
                text= '>Tap the Button<',
                weight= "bold",
                align= 'center',
                actions=[
                    MessageTemplateAction(
                        label='Download Smule',
                        text='≽ Use:\n• /smuleaudio:<Link>\n• /smulevideo:<Link>'
                    ),
                    MessageTemplateAction(
                        label='Translate',
                        text='≽ Use:\n• /jawa<text>'
                    ),
                    MessageTemplateAction(
                        label='Info Bmkg',
                        text='≽ Use:\n• /bmkg'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
        
    elif (text == '/media2') or (text == 'Media2') or (text == 'media2'):
        buttons_template = TemplateSendMessage(
            alt_text='media area',
            template=ButtonsTemplate(
                title='MEDIA COMMAND',
                text= '>Tap the Button<',
                weight= "bold",
                align= 'center',
                actions=[
                    MessageTemplateAction(
                        label='Image Text',
                        text='≽ Use:\n• /fs1:<Text>\n• /fs1:<Text>\n• /graffiti:<text>\n• /light:<text>\n• /street:<text>\n• /cookies:<text>\n• /sletters:<text>'
                    ),
                    MessageTemplateAction(
                        label='Zodiac',
                        text='≽ Use:\n• /zodiac: <text>'
                    ),
                    MessageTemplateAction(
                        label='Download Timeline',
                        text='≽ Use:\n• /linepost: <LinkTimeline>'
                    ),
                    MessageTemplateAction(
                        label='Checking',
                        text='≽ Use:\n• /audio:<link>\n• /video:<link>\n• /image:<link>'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
#=====[ CAROUSEL MESSAGE ]==========[ ARSYBAI ]======================
    elif text == '/musik':
        buttons_template = TemplateSendMessage(
            alt_text='Enjoy whit music',
            template=ButtonsTemplate(
                title='[ GENDRE MUSIC ]',
                text= '>Tap the Button<',
                actions=[
                    MessageTemplateAction(
                        label='Music Indonesia',
                        text='/Mindo'
                    ),
                    MessageTemplateAction(
                        label='Music Barat',
                        text='/Mbarat'
                    ),
                    MessageTemplateAction(
                        label='Music Kpop',
                        text='/Mkpop'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)
    
    elif text == '/listtoken':
        message = TemplateSendMessage(
            alt_text='Token area',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='> LIST TOKEN <',
                        text='JamsHakim',
                        actions=[
                            MessageTemplateAction(
                                label='>Chromeos<',
                                text='/chromeos'
                            ),
                            MessageTemplateAction(
                                label='>Iosipad<',
                                text='/iosipad'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='> LIST TOKEN <',
                        text='JamsHakim',
                        actions=[
                            MessageTemplateAction(
                                label='>Desktopmac<',
                                text='/desktopmac'
                            ),
                            MessageTemplateAction(
                                label='>Desktopwin<',
                                text='/desktopwin'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='> LIST TOKEN <',
                        text='JamsHakim',
                        actions=[
                            MessageTemplateAction(
                                label='>Win10<',
                                text='/win10'
                            ),
                            MessageTemplateAction(
                                label='>Clova<',
                                text='/clova'
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=====[ CAROUSEL MESSAGE ]==========[ ARSYBAI ]======================
    elif (text == 'Me') or (text == 'Me'):
        message = TemplateSendMessage(
            alt_text='>My creator<',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        title='YOUTUBE',
                        text='subcribe',
                        actions=[
                            URITemplateAction(
                                label='>Jams<',
                                uri='https://m.youtube.com/channel/UCQF7nT6GQK65ObrNjozoeuw'
                            )
                        ]
                    ),
                    CarouselColumn(
                        title='My web',
                        text=' Blog',
                        actions=[
                            URITemplateAction(
                                label='>Jams<',
                                uri='https://jamsblogaddress.blogspot.com/?m=1'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    if event.message.text == "/app clone":
        buttons_template = TemplateSendMessage(
            alt_text='App clone',
            template=ButtonsTemplate(
                title='Aplikasi clone',
                text='Klik salah satu menu dibawah ini.',
                thumbnail_image_url='https://imgur.com/Hbv4GWl.jpg',
                actions=[
                    URITemplateAction(
                        label='Parallel Space',
                        uri='https://play.google.com/store/apps/details?id=com.lbe.parallel.intl'
                    ),
                    URITemplateAction(
                        label='APP Cloner',
                        uri='https://play.google.com/store/apps/details?id=com.applisto.appcloner'
                    ),
                    URITemplateAction(
                        label='2Accounts',
                        uri='https://play.google.com/store/apps/details?id=com.excelliance.multiaccount'
                    ),
                    URITemplateAction(
                        label='Multi clone',
                        uri='https://play.google.com/store/apps/details?id=com.jumobile.multiapp'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
#=====[ FLEX MESSAGE ]==========[ ARSYBAI ]======================
    elif (text == 'makasih') or (text == 'Makasih'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/21831487/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Nah') or (text == 'Nahh'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/37652126/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Matamu') or (text == 'Matane'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/7111997/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hoax') or (text == 'Hoaxx'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/11221543/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hmm') or (text == 'Hm'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/18423382/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    elif (text == 'Drama') or (text == 'Eleh'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34558069/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'nyimak') or (text == 'Nyimak'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/9756022/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'ga') or (text == 'gak') or (text == 'gamau') or (text == 'Gamau') or (text == 'Ga') or (text == 'Gak'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683557/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Keren') or (text == 'Mantap') or (text == 'Kerenn') or (text == 'Mantapp') or (text == 'Bagus') or (text == 'Hebat'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12860202/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sepi'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200512/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Malem') or (text == 'Met malem'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/18282481/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Hai') or (text == 'Halo'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186953/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'sabar') or (text == 'Sabar'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22499899/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Ngantuk'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691708/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Haha') or (text == 'Wkwk'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200499/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Kzl') or (text == 'Kezel'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24464008/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Go') or (text == 'Siap'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186952/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif text == 'Bingung':
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34751035/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Tolong') or (text == 'Please'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/11825345/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Okee') or (text == 'Okay') or (text == 'Ok') or (text == 'Oke'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22482252/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Baper') or (text == 'Karepmu'):
        message = TemplateSendMessage(
            alt_text='TRIO PEKOK PROTECTION',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16365505/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kamm') or (text == 'Kam') or (text == 'Wc') or (text == 'Welcome'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24862265/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bye') or (text == 'Minggat'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34558071/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Ngopi') or (text == 'Ngopii') or (text == 'Ngopi cok') or (text == 'Ngopi woy'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691714/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Opo') or (text == 'Opoo') or (text == 'Naon'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691705/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Jancik') or (text == 'Jancok') or (text == 'Jancuk') or (text == 'Ancik'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547155/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sider on') or (text == 'Cctv on') or (text == 'Lurking on') or (text == '.sider on'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200507/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Mandi') or (text == 'Adus') or (text == 'Mandi dulu') or (text == 'Adus sik'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691709/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Juhh') or (text == 'Johh') or (text == 'Juoh'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12521487/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hbd') or (text == 'Met ultah') or (text == 'Selamat hari jadi') or (text == 'Happy Birthday'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/7670129/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Salken') or (text == 'Salam kenal'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24464015/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'O') or (text == 'O aja') or (text == 'Oo') or (text == 'Ooo'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/17530681/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Gift') or (text == 'Gift aku') or (text == 'Gift me') or (text == 'Gift dul'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22220762/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Dih'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12842266/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Yank') or (text == 'Syg') or (text == 'Jo'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/78960399/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'No') or (text == 'Tidak Boleh') or (text == 'Moh') or (text == 'Giah'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12842265/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Galau') or (text == 'Galon') or (text == 'Lagi galon') or (text == 'Lagi galau'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/55737941/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kenyang') or (text == 'Wareg'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12842261/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    
    elif (text == 'Maaf') or (text == 'Sorry'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/18282476/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Muleh'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/20217667/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Mbalik'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547168/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Jembut') or (text == 'Asw') or (text == 'Jiembut') or (text == 'Asu'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200497/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Otw') or (text == 'Otww') or (text == 'Gas'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/20217665/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sue') or (text == 'Suee') or (text == 'Suek') or (text == 'Sueek'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/19002665/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Pm') or (text == 'Pc') or (text == 'Cek pm') or (text == 'Buka pm'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/17241274/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kuy') or (text == 'Kuyy') or (text == 'Kuy ah') or (text == 'Kuyy ah'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200506/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bubug') or (text == 'Bobog') or (text == 'Tidur') or (text == 'Merem'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/26538903/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Apes') or (text == 'Apes aku'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200515/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Pekok') or (text == 'Gemblung') or (text == 'Koplok') or (text == 'Gendeng'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12521475/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sepi') or (text == 'Sepii'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200512/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Makan') or (text == 'Mangan') or (text == 'Maem'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/14038588/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    elif (text == 'Jones') or (text == 'Jomblo') or (text == 'Mblo'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186956/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Pagi') or (text == 'Met pagi') or (text == 'Morning'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/15666186/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bangun') or (text == 'Tangi'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547152/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Terserah') or (text == 'Serah'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691717/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Call') or (text == 'Kojom') or (text == 'Ayo kojom'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200511/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Wekkk') or (text == 'Wekk') or (text == 'Wek'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547171/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kangen') or (text == 'Angen') or (text == 'Kangenn'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/11866860/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Muah') or (text == 'Muach') or (text == 'Muachhh'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691710/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hihi') or (text == 'Hihihi') or (text == 'Hihihihi'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186955/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Typo') or (text == 'Asem typo') or (text == 'Typoo'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547158/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bacot') or (text == 'Omong ae') or (text == 'Padon ae'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/23581910/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=====[ Sticker MESSAGE ]==========[ ARSYBAI ]======================
    elif (text == 'anjir') or (text == 'Anjir'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16135443/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'astaghfirullah') or (text == 'Astaghfirullah'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16135442/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'sackid') or (text == 'Sackid'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/15664374/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'kam') or (text == 'Kam'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626494/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Mantul') or (text == 'mantul') or (text == 'Mantap') or (text == 'mantap'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/1072597/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Wadaw') or (text == 'wadaw'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/15671736/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Hlh') or (text == 'hlh'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/15708876/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Huh') or (text == 'huh'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12690693/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'kaget') or (text == 'Kaget'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/49279761/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'Ngakak') or (text == 'ngakak'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/73760360/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'oksip') or (text == 'Oksip'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
              columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52002735/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'aw i cry') or (text == 'Aw i cry') or (text == 'Aw i cri') or (text == 'aw i cri'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/19599278/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'makasih') or (text == 'Makasih'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/153453/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'nyimak') or (text == 'Nyimak'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/13162615/IOS/sticker.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'ga') or (text == 'gak') or (text == 'gamau') or (text == 'Gamau') or (text == 'Ga') or (text == 'Gak'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683557/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'good night') or (text == 'Good night') or (text == 'selamat malam') or (text == 'Selamat malam'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683546/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hai') or (text == 'Hai') or (text == 'halo') or (text == 'Halo'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52002738/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'sabar') or (text == 'Sabar'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22499899/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'wkwk') or (text == 'Wkwk'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/27695296/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hehe') or (text == 'Hehe'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52002763/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'siap') or (text == 'Siap'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626520/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif text == '?':
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34751035/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'please') or (text == 'Please') or (text == 'tolong') or (text == 'Tolong'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626499/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'ok') or (text == 'oke') or (text == 'Ok') or (text == 'Oke'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/51626500/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'hahaha') or (text == 'Hahaha') or (text == 'Haha')or (text == 'haha'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/40381622/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    elif (text == 'sebel') or (text == 'Sebel'):
        message = TemplateSendMessage(
            alt_text='JamsHakim',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/52114135/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='https://jamsblogaddress.blogspot.com/?m=1')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#=======================================================================================================================
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
