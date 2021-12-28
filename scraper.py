from bs4 import BeautifulSoup
import requests


def scrap(pages:int=1):
    for i in range(pages):
        site = requests.get(f"https://losots.pl/index.php?action=loshub&do=highscores&list=experience&page={i+1}")

        bs = BeautifulSoup(site.content, 'html.parser')

        rows = bs.find("table", {"class": "tborder"}).find_all("tr")[2:42]
        print(len(rows))

        for row in rows:
            data = row.find_all("td")
            position = data[0].text
            character = data[1].text
            profile_link = data[1].find("a")['href']
            vocation = data[2].text
            level = int(data[3].text)
            experience = int(data[4].text)

            print(position, character, "|", vocation, "|", level, "|", experience)
            
            equipment = BeautifulSoup(requests.get(profile_link).content, 'html.parser').find_all("table", {"class": "tborder"})[2].find_all("img")

            print(', '.join([eq['src'] for eq in equipment]))
            print()



if __name__ == "__main__":
    scrap()