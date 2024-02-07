from bs4 import BeautifulSoup
import requests 

print("\n9Anime watchlist\n")

genre = { "Action": 1,
        "Adventure": 2,
        "Cars": 3,
        "Comedy": 4,
        "Dementia": 5,
        "Demons": 6,
        "Drama": 7,
        "Ecchi": 8,
        "Fantasy": 9,
        "Game": 10,
        "Harem": 11,
        "Historical": 12,
        "Horror": 13,
        "Isekai": 14, 
        "Josei": 15,
        "Kids": 16,
        "Magic": 17,
        "Martial Arts": 18,
        "Mecha": 19,
        "Military": 20,
        "Music": 21,
        "Mystery": 22,
        "Parody": 23,
        "Police": 24,
        "Psychological": 25,
        "Romance": 26,
        "Samurai": 27,
        "School": 28,
        "Sci-Fi": 29,
        "Seinen": 30,
        "Shoujo": 31,
        "Shoujo Ai": 32,
        "Shounen": 33,
        "Shounen Ai": 34,
        "Slice of Life": 35,
        "Space": 36,
        "Sports": 37,
        "Super Power": 38,
        "Supernatural": 39,
        "Vampire" : 41,
                       
} 
keys = genre.keys()

key_list = []

for key in keys:
    key_list.append(key) #stores all the keys in the key_list

print(key_list)

select = input("\nChoose a genre: ")

while True:
    result = genre.get(select)

    if result == None: #Checks if the result variable is equal to the value of the key
        print("Error: Genre does not exist!")
        select = input("\nChoose a genre: ")
    else:
        break
    
while select == " " :
    print("Error: Invalid entry!")


url = f"https://9anime.pe/filter?keyword=&type=&status=all&season=&language=&sort=default&year=&genre={result}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="form-control form-control-dark input-page") # gets the input tag

pages = int(str(page_text).split("value")[-1][2:-3])#isolates the page number

anime = []
links = []

watchlist = {}

for page in range(1, pages + 1):
    url = f"https://9anime.pe/filter?keyword=&type=&status=all&season=&language=&sort=default&year=&genre={result}&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find_all(class_="film-name") # isolates the <h3> tag
    content = [d.find('a') for d in div] # isolates the <a> tag

    for contents in content:
        link = contents['href']
        site_links = f"https://9anime.pe{link}"
        anime_name = contents['data-jname']
        anime.append(anime_name)
        links.append(site_links)
    for key, value in zip(anime, links):
        watchlist[key]= value

print(watchlist)


    







