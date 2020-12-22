GNU nano 5.4           p.py
print ("Web info ")
print ("\033[91m")
print ("code by toufiqul islam ")
print ("\033[92m")
print ("facebook toufiqul islam ")

print ("\033[93m")
# ! /usr/bin/python(created by md toufiqul islam)
import urllib2
import sys
url = raw_input ("Enter website link:")
url.rstrip ( )
header = urllib2.urlopen(url) .info ( )
print(str (header) )