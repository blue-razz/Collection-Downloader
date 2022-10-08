import requests
import subprocess
from rich import print
from bs4 import BeautifulSoup

print("[bold green]SteamCMD Collection Downloader[/bold green]")
print(":banana:", "version 1")

print("SteamCMD location (steamcmd.exe): ", end="")
steamcmd_path = input()

print("App ID: ", end="")
app_id = input()

print("Collection URL: ", end="")
collection_url = input()

req = requests.get(collection_url)
steam_soup = BeautifulSoup(req.content, 'html.parser')

mod_ids = []

collection_items = steam_soup.findAll('div', attrs = {'class': 'collectionItemDetails'})
for item in collection_items:
    mod_ids.append(item.a['href'][55:])

print(":vampire:", f"Downloading [green]{len(mod_ids)}[/green] mods...")

args = [steamcmd_path, "+login anonymous"]

for mod in mod_ids:
    args.append(f"+workshop_download_item {app_id} {int(mod)}")

args.append("+quit")

subprocess.run(args, shell=True)

print("[green]All done![/green]")
