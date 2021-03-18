import requests
import xml.etree.ElementTree as ET
import urllib.request

numbers = range(0, 100)
for n in numbers:
    #data_file = urllib.URLopener()
    try:
        urllib.request.urlretrieve("https://ovakszeged.hu/test_env/opendatapublicapi/api/v1.0/SharedData/" + str(n), 'data_'+ str(n) +'.xml')
    except:
        continue