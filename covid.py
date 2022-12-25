import requests
import time
import main as bot

def covid_stats():
    global prev_record

    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country": "Nepal"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "58695539dbmsh212731fa972798dp10070fjsn9b487c1888b5"
    }

    data = requests.request("GET", url, headers=headers, params=querystring).json()
    print(data)
   
    country = data['Country_text']
    active_cases = data['Active Cases_text']
    last_updated = data['Last Update']
    new_cases = data['New Cases_text']
    new_deaths = data['New Deaths_text']
    total_cases = data['Total Cases_text']
    total_deaths = data['Total Deaths_text']
    total_recovered = data['Total Recovered_text']
    
    tweet = f"Today in {country}, there were {new_cases} new cases of Covid-19 and {new_deaths} new deaths. \nThe total number of cases have reached {total_cases} with {active_cases} active {total_recovered} recovered and {total_deaths} total deaths"
    
    tweet2 = f"Today in {country}, there were {new_cases} new cases of Covid-19 and {new_deaths} new deaths."
    
    updated = f"\n \nlast Updated: {last_updated}"
    
    summary = f"\n \nSummary : \nNew Cases: {new_cases}  \nNew deaths: {new_deaths}  \nActive Cases: {active_cases}  \nTotal Deaths: {total_deaths}"
    
    hashtags = f"\n \n#covid19 #updates #nepal #stay_home #stay_safe"

    tweet_text = tweet2 + summary + updated + hashtags

    #print(tweet_text)

    if prev_record < int(active_cases.replace(',','')):
        print('Data Updated')
        if new_cases == '' :
            print('New Cases Not Updated')
        else:
            print(f'new cases = {new_cases}')
            prev_record = int(active_cases.replace(',', ''))
            try:
               # bot.tweet(tweet_text)
                print(tweet_text)
            except tweepy.TweepError as e:
                print(e.reason)

    else:
        print('Data not updated')

prev_record = 0

while True:
    covid_stats()
    time.sleep(1800)
