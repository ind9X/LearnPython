import re
r = r"(.+?).mp3"
songs = "123.mp3 456.mp3 789.mp3"
mp3_re = re.compile(r)
print(mp3_re.findall(songs))