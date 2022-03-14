import datetime
import requests

#setting interval limits
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(1)

overpass_today = today.strftime("%Y-%m-%dT%H:%M:%SZ")
overpass_yesterday = yesterday.strftime("%Y-%m-%dT%H:%M:%SZ")

r = requests.get('http://overpass-api.de/api/interpreter?data=[out:xml][timeout:600][adiff:\"' + overpass_yesterday +'\",\"' + overpass_today + '\"];(area(3600042611)->.er;area(3600042472)->.fi;relation(area.er)[\"source\"=\"survey:CAI\"][\"source:ref\"=\"9224011\"];relation(area.fi)[\"source\"=\"survey:CAI\"][\"source:ref\"=\"9224011\"];);(._;>;);out meta geom;')

