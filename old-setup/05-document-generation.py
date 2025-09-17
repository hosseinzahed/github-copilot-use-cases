# Legacy Python 2 code
import urllib2
import cStringIO
import ConfigParser

def fetch_url(url):
    response = urllib2.urlopen(url)
    return response.read()

def parse_ini(content):
    config = ConfigParser.ConfigParser()
    config.readfp(cStringIO.StringIO(content))
    return config

url = 'http://example.com/config.ini'
content = fetch_url(url)
print content

config = parse_ini(content)
print config.sections()

# Prompt: Document and explain the Python 2 code in preparation to modernize it into Python 3 code. 
