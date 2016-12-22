from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from urllib.request import urlopen
from xml.etree.ElementTree import parse

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
def request_handler(area):
    url = "https://opendata.cwb.gov.tw/opendataapi?dataid=F-C0032-001&authorizationkey={WEATHER_KEY}".format(WEATHER_KEY = settings.WEATHER_KEY)
    response = urlopen(url)
    tree = ET.parse(response)
    root = tree.getroot()
    for element in root.iterfind(".//urn:cwb:gov:tw:cwbcommon:0.1location")
        if area in element[0].text
            output = element.find(".//urn:cwb:gov:tw:cwbcommon:0.1parameterName")
            return "Weather of" + element[0].text + ":" + output.text
    return area + "not found.Please Enter a city of Taiwan to check the weather!"
@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=event.message.text)
                    )
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
