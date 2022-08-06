import requests
from litex.regon import REGONAPI, REGONAPIError
from xml.etree import ElementTree


NIP = ('5861467630')
SERVICE_URL = (
    'https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc')

USER_KEY = ('b71c1c32f1e745f5b305')
api = REGONAPI(SERVICE_URL)
api.login(USER_KEY)
# entity = api.search(nip=NIP)

detailed_report = api.full_report('220356962', 'BIR11OsFizycznaDaneOgolne')
# summary_report = api.summary_report(
#      '2020-01-01',
#      'BIR11NowePodmiotyPrawneOrazDzialalnosciOsFizycznych'
#      )


print(detailed_report)
print('KomunikatKod:')
print(api.get_value('KomunikatKod'))
print('KomunikatTreść:')
print(api.get_value('KomunikatTresc'))
print('StatusSesji:')
print(api.get_value('StatusSesji'))
print('StatusUsługi:')
print(api.get_value('StatusUslugi'))
print('KomunikatUslugi:')
print(api.get_value('KomunikatUslugi'))


for item in api.search(nip=NIP):
    print(item)

print('Logging out...')
api.logout
