import repltalk
import repltalk
import asyncio
from os import system
from time import sleep
def menu():
    print("""


  _____            _   _ _     _   _                         _____ _               _             
 |  __ \          | | (_) |   | \ | |                       / ____| |             | |            
 | |__) |___ _ __ | |  _| |_  |  \| | __ _ _ __ ___   ___  | |    | |__   ___  ___| | _____ _ __ 
 |  _  // _ \ '_ \| | | | __| | . ` |/ _` | '_ ` _ \ / _ \ | |    | '_ \ / _ \/ __| |/ / _ \ '__|
 | | \ \  __/ |_) | |_| | |_  | |\  | (_| | | | | | |  __/ | |____| | | |  __/ (__|   <  __/ |   
 |_|  \_\___| .__/|_(_)_|\__| |_| \_|\__,_|_| |_| |_|\___|  \_____|_| |_|\___|\___|_|\_\___|_|   
            | |         By: Raz                                                                      
            |_|                                                                                  


""")


menu()

def clr():
    system('clear')
def load(_time_):
        _time_ = _time_ / 4
        for i in range (0, 5):
            message = " Fetching User Data" + "."*i
            print (message, end="\r")
            sleep(_time_)
        print("                          ", end="\r")
    
run = True
repl = repltalk.Client()
async def parse_user():
    global userName, cycles, bio, birthday, langs, subs, postNum, comNum, url, avatar, roles, place, onBoard
    userName = str(input('Enter a repl.it Username (without the @)\n>> '))
    user = await repl.get_user(userName)
    print('\nPlease wait patiently. This will take a few seconds.')
    load(5)
    board = await repl.get_leaderboard(limit=100)
    if user is None: 
        print("\n\nThis user could not be found, Maybe its available? ('Maybe it's your spelling!)")
        return

    cycles = user.cycles
    bio = user.bio
    birthday = user.timestamp
    langs = user.languages
    s = user.subscription
    url = user.url
    avatar = user.avatar

    url = 'repl.it' + str(url)

    if user in board:
        place = board.index(user) + 1
        onBoard = True
    else: onBoard = False

    if str(s) == 'None': subs = 'Starter (Free)'
    elif str(s) == 'hacker': subs = 'Hacker ($7/month)'

    comments = await user.get_comments()
    comNum = 0
    for comment in comments:
        comNum += 1
    
    if comNum >= 100: comNum = '100+'

    posts = await user.get_posts()
    postNum = 0
    for post in posts:
        postNum += 1
    return True

def prTable():
    global userName, cycles, bio, birthday, langs, subs, postNum, comNum, url, avatar, roles, place, onBoard
    

    fBday = str(birthday)
    header = userName.center(25, ' ')
    print("Found Userinfo!")
    tableTitle = "-~-~-"+header+"-~-~-\n"
    inLine = '\n'+' '*16 + '|'

    info = "\nCycles          | {0:<7}"+inLine+"\nDate Joined     | {1:<7}"+inLine
    info2 = "\nFav Languages   | {0}"+inLine+"\nNum of Posts    | {1:<7}"+inLine
    info3 = "\nNum of Comments | {0:<7}"+inLine+"\nSubscription    | {1:<7}"+inLine
    info4 = "\nBio             | \"{0:<}\""+inLine+"\nProfile URL     | {1:<7}"+inLine

    if onBoard == True:
        info5 = "\nAvatar URL      | {0:<7}"+inLine+"\nTop 100 Users   | {1:<4} - Place: #{2:<7}"
        print(
        tableTitle,
        info.format(str(cycles), str(fBday[0:10])),
        info2.format(str(langs[:3]), str(postNum)),
        info3.format(str(comNum), str(subs)),
        info4.format(str(bio), str(url)),
        info5.format(str(avatar), str(onBoard), str(place)))
    elif onBoard == False:
        info5 = "\nAvatar URL      | {0:<7}"+inLine+"\nTop 100 Users   | {1:<7}"
        print(
        tableTitle,
        info.format(str(cycles), str(fBday[0:10])),
        info2.format(str(langs[:3]), str(postNum)),
        info3.format(str(comNum), str(subs)),
        info4.format(str(bio), str(url)),
        info5.format(str(avatar), str(onBoard)))

while run:
    try:
        asyncio.run(parse_user())
        prTable()
    except NameError: pass
    input('\n'*6 + 'Press enter to search again\n>> ')
    clr()

