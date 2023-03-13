from latest_news import get_news
from network_speed import get_download_speed, get_upload_speed
from speech_to_text import speech_to_text, text_to_speech
from weather_info import getWeather
from web_functions import get_joke, open_google, open_youtube, wish_me


def handle_audio_input():
    query = speech_to_text().lower()
    return user_command(query)

def handle_text_input(query):
    return user_command(query)

def user_command(query):

    if 'open youtube' in query:
        text_to_speech("Opening youtube")
        open_youtube()
        return ""

    elif 'search youtube for' in query:
        query = query.split('search youtube for ')[-1]
        text_to_speech("Searching youtube for " + query)
        open_youtube(query)
        return ""

    elif 'open google' in query:
        text_to_speech("Opening google")
        open_google()
        return ""

    elif 'search google for' in query:
        query = query.split('search google for')[-1]
        text_to_speech("Searching google for "+ query)
        open_google(query)
        return ""

    elif 'download speed' in query:
        down_speed = get_download_speed()
        text_to_speech("Your download speed is " + down_speed)
        return "Your download speed is " + down_speed
    
    elif 'upload speed' in query:
        up_speed = get_upload_speed()
        text_to_speech("Your upload speed is " + up_speed)
        return "Your upload speed is " + up_speed
    
    elif 'network speed' in query:
        up_speed = get_upload_speed()
        down_speed = get_download_speed()

        text_to_speech("Your download speed is " + down_speed + " and upload speed is " + up_speed)
        return "Download speed is " + down_speed + " and upload speed is " +  up_speed
    
    elif 'joke' in query:
        joke = get_joke()
        text_to_speech("Sure here's a joke for you , , " + joke)
        return joke
    
    elif 'show weather'in query:
        weather = getWeather()
        text_to_speech(f"The weather in {weather.get('city')} is, Temperature {weather.get('temperature')}, Humidity {weather.get('humidity')}, Pressure {weather.get('pressure')} with {weather.get('report')}")
        
        return f"Temperature: {weather.get('temperature')}\nHumidity: {weather.get('humidity')}\nPressure: {weather.get('pressure')}\nReport: {weather.get('report')}"
    
    elif 'weather in' in query:
        city = query.split()[-1]

        weather = getWeather(city)
        
        text_to_speech(f"The weather in {weather.get('city')} is, Temperature {weather.get('temperature')}, Humidity {weather.get('humidity')} percent, Pressure {weather.get('pressure')} with {weather.get('report')}")
        
        return f"Temperature: {weather.get('temperature')}\nHumidity: {weather.get('humidity')}\nPressure: {weather.get('pressure')}\nReport: {weather.get('report')}"

    elif 'news' in query:

        all_news = []
        num_articles = 0
        query = query.split()
        for i in range(len(query)):
            if query[i].isdigit():
                num_articles = int(query[i])
                all_news = get_news(num_articles)
                break
            else:
                all_news = get_news()

        audio_output = ""
        text_output = ""

        for i in range(len(all_news)):
            audio_output += "Headline: " + str((i+1)) + ": " + all_news[i][0]

            text_output += f"Headline {i}: {all_news[i][0]}\nDescription: {all_news[i][1]}\nURL: {all_news[i][2]}\n"


        text_to_speech(f"Here are the news headlines:  {audio_output}")
        return text_output
    
    elif 'ark' in query:
        if 'how' in query:
            text_to_speech("I am fine. Thank you for asking. How can I help you?")
            return "I am fine. Thank you for asking. How can I help you?"
        else:
            query = wish_me()
            text_to_speech(query)
            return query

    else:
        text_to_speech("Sorry, I did not understand. Please try again")
        return "Please try again"
