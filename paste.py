import urllib.request

#loads all pokemon into one array to check against later
pokefile = open("pokemon.txt",'r')
POKEMON = pokefile.read().splitlines()
pokefile.close()

#should use regex in the future, however these two strings allow selection of just the pokemon in a raw pastebin
BEGIN_OF_RAW_TEXT = '<textarea id="paste_code" class="paste_code" name="paste_code" onkeydown="return catchtab(this,event)">'
BEGIN_OF_RAW_TEXT_LENGTH = len(BEGIN_OF_RAW_TEXT)
END_OF_RAW_TEXT="</textarea>"

class Paste():
    def __init__(self, url, author, sixmons = []):
            raw = self.open_paste_from_url(url).lower()

            #normally you do not specify sixmons, however if you are reading a dump you put it in the args to save time
            if sixmons == []:
                for mon in POKEMON:
                    if mon + " @" in raw or mon + "-" in raw:
                        sixmons.append(mon)
            if ("://pastebin.com/") not in url or ("/raw" in url) or ("http" not in url or "##" in author):
                raise ValueError("Url not in correct format")
            else:
                self.id = url[url.index("com/") + 4:].replace("/","")
            if "##" in author:

            self.author = author
            self.sixmons = sixmons

    @staticmethod
    #scrapes pastebin for the pastebin raw data, in this case our team of 6 pokemon
    def open_paste_from_url(url):
        request = urllib.request.urlopen(url)
        request_str = request.read().decode("utf8")
        return request_str[request_str.index(BEGIN_OF_RAW_TEXT)+BEGIN_OF_RAW_TEXT_LENGTH:request_str.index(END_OF_RAW_TEXT)]

    #returns a new Paste object from a string formatted below
    @staticmethod
    def read(dump):
        arr = dump.split("##")
        return Paste(url = "https://pastebin.com/" + arr[0], author = arr[1], sixmons = arr[2:])

    #dumps the object into a string that can be turned back into a Paste object
    def dump(self):
        output = self.id + "##" + self.author + "##"
        for mon in self.sixmons:
            output += mon + "##"
        return output[:len(output)-2]

    def __str__(self):
        output = ""
        for mon in self.sixmons:
            output += mon.title() + " / "
        return output[:len(output)-1] + "\nBy: {}".format(self.author)

#sampleteam = Paste("http://pastebin.com/5AcrDVnB", "rob")
