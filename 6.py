import urllib, zipfile, re

next, next_re, _list, f_re = '90052', 'Next nothing is (\d+)', [], '%s.txt'
file = zipfile.ZipFile("channel.zip")

while True :
	try :
		next = re.search(next_re, file.read(f_re % next)).group(1)	
	except :
		print file.read(f_re % next)
		break

	_list.append(file.getinfo(f_re % next).comment)

print ''.join(_list)
