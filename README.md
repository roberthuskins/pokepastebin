# pokepastebin
###### Paste() object for scraping and organizing Pokemon teams from pastebin.com

### How to Use (Python 3):
```python
from paste import Paste
sampleteam = Paste("http://pastebin.com/5AcrDVnB", "Rob")

print(sampleteam.author)
print(sampleteam.id)
print(sampleteam.sixmons)
print(sampleteam.open())
print(sampleteam.dump_to_json())
#excuse my 1AM team
```
### IMPORTANT:
I made this for personal use, and proof that I could make python objects. Pastebin reccomends you use their [scraping API](https://pastebin.com/api_scraping_faq), as they might block your IP if they detect suspicious activity. I'm not responsible for anything that happens while you use this code.

All Pokemon are trademarks of The Pokémon Company.
