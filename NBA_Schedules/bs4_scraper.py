import requests
import bs4
from bs4 import BeautifulSoup as bsp
import datetime

url = 'https://www.basketball-reference.com/leagues/NBA_2023_games.html'


# Get the current date
current_date = datetime.date.today()

# Get the month from the current date
actual_month= current_date.strftime("%B")

res=requests.get(url)
print(res.status_code)

#find link of specefic month
soup=bsp(res.text,'html.parser')
months=soup.find(attrs={'class':'filter'})
link=months.find('a',string=actual_month)
new_link=link['href']
#new_link
print(new_link)

schedule_res=requests.get(f'https://www.basketball-reference.com{new_link}')
print(schedule_res.status_code)
soup=bsp(schedule_res.text,'html.parser')


#get schedule rows
schedule=soup.find(attrs={'id':'schedule'})
data=schedule.tbody

#extract relevant data
dates=[]
for date in data.find_all(attrs={'data-stat':'date_game'}):
    dates.append(date.string)

times=[]
for time in data.find_all(attrs={'data-stat':'game_start_time'}):
    times.append(time.string)

visitor_teams=[]
for visitor in data.find_all(attrs={'data-stat':'visitor_team_name'}):
    visitor_teams.append(visitor.string)

home_teams=[]
for home in data.find_all(attrs={'data-stat':'home_team_name'}):
    home_teams.append(home.string)

arenas=[]
for arena in data.find_all(attrs={'data-stat':'arena_name'}):
    arenas.append(arena.string)

with open(f'Nba_{actual_month}.txt','w')as file:
    for date,time,visitor_team,home_team,arena in zip(dates,times,visitor_teams,home_teams,arenas):
        file.write(f"{date},{time},{visitor_team},{home_team},{arena}\n")