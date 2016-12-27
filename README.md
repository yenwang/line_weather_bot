# line_weather_bot
#bot setup
I use line as my bot platform  
You can create your line bot on https://business.line.me/zh-hant/services/bot  
My bot need to connect to my server,so I do the setting to allow webhook service on line  
And then set webhook url to https://"your heroku domain name here"/line_bot/callback/  
#server setup
I use Heroku as my server  
You can go to https://dashboard.heroku.com/ to create your own server  
And follow the tutorial on the above web to install Heroku cli and upload your project  
#confidential key
For i don't want to let others know some secrect values, I put these values on Heroku.  
1.LINE_CHANNEL_ACCESS_TOKEN (check your own key on your line bot)  
2.LINE_CHANNEL_SECRET (check your own key on your line bot)  
3.SECRET_KEY (check your own key on your settings.py)  
4.WEATHER_KEY (I use this key to access weather and parse it, you can create your own account on http://opendata.cwb.gov.tw/index and then your will get this key)  
#Useage
Add your line bot by Connected Bot ID or QR Code  
My line bot id is @yxh4216r  
QR Code <img src="http://qr-official.line.me/L/5jfaC62qL2.png">  
This bot can search the weather for you(Only cities in Taiwan)  
1.If "天氣" appears in your message, the bot will search the weather in Tainan for you(by default).  
2.If "天氣" and a city name(eg:"南投") appear simutaneously in your message, the bot will search the weather in the city you enter for you.  
3.Because Taiwan has "新竹縣" "新竹市" "嘉義縣" "嘉義市", please specify the city/country when "新竹" and "嘉義" is mentioned.For other cities, you can simply input the city name witout city/country(eg:"桃園天氣"), then the bot will search the weather in "桃園市" in this example.  
4.Both "台" and "臺" is an available match.For example input "台北天氣" or "臺北天氣", the bot will search the weather in Taipei city.  
