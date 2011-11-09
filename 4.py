import urllib, re, time

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

regexp = "and the next nothing is (\d+)"
nothing = "12345"

while True:
    try:
        src = urllib.urlopen(uri % nothing).read()
        nothing = re.search(regexp, src).group(1)
    except:
        break

nothing = int(nothing)/2
 
while True:
    try:
        src = urllib.urlopen(uri % nothing).read()
        nothing = re.search(regexp, src).group(1)
    except:
        break

print urllib.urlopen(uri % nothing).read()
