# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
#Coded By Qamar
#Telegram >> i4m_qamar
#TB\ agar brdt nawman bhena be ئسوڵ maba ... 
import requests, random, threading, time, os
RE='\033[91m'
GR='\033[92m'
YE='\033[93m'
WH='\033[97m'

os.system('clear')



logo = """

\033[1;91mAuther:Hama.Zw
\033[1;92mYoutube:Warzone Cracker
\033[1;93mTelegram Channel:@kurdhacker_hama_bn_dlaj
\033[1;92mTelegram Group:@kurdhackerzw
-----------------------------------------------------------------------------


"""


print(logo)
qamar =  int(input(WH+" Chand Pet Be >>>\033[97m "))
print('')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print(WH+' Kamek Chawareka ...')
time.sleep(5)
print('')
class Snap(object):
    def __init__(self):
        def userlist():
            list = 'a1bc_2de3f.g4hi5jk6lm7mn8op9qr_0stuvwx.yz_83e76dvnhdy083adpoy.eqaxvnmkydz.zqeyopmn.gaeh5228hb4qsg901jfw5hbkyrqzvj74.wb_ji75dvbjwqwo_pplmnbxzzaw478.00ourewaj853_37801124xvb.mmsyki689ijgwtyio_.'
            return ''.join(random.choice(list) for i in range(qamar))
            i7 = random.choice(list)
            i1 = random.choice(list)
            i2 = random.choice(list)
            i3 = random.choice(list)
            i4 = random.choice(list)
            vs = i7+i1+i2
        th = []
        while True:
            for cm in range(120):
                Username = userlist()
                t = threading.Thread(target=self.snap,args=(Username,))
                t.start()
                th.append(t)
                time.sleep(1)
            for j in th:
                j.join()

    def snap(self,Username):
        url = 'https://accounts.snapchat.com/accounts/get_username_suggestions'
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '57',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
            'cookie': 'xsrf_token=jRBXY6u7yIGKLWwRe2frOA; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.326554086.1615024660; _gid=GA1.2.1584981554.1615024660; _scid=d6f62e80-98bc-45a0-9c9f-002c5f1297f4; sc_at=v2|H4sIAAAAAAAAAAXBgQ0AIQgDwIlIKKHFdfDVKRj+7xDlHv2Z+NISu6yVZVy6eIfajRkI9Ehxjf/w9oOvMgAAAA==; _sctr=1|1614974400000; web_client_id=09ea2734-ed11-4356-a79a-af4281a9ca13; _gcl_au=1.1.840761591.1615024698; _sca={%22cid%22:%2259eecd59-71ee-482e-94d1-747cf1c583ca%22%2C%22token%22:%22v1.key.2021-03-06_0mryaaW4.iv.VReKUYNbcCtriOX5.C9nWyaCJ1Uj9H2BkL2zjp2bR8kbXUbrVLdKGdKdlWiODqPo3YlIbxmrQCWMc6AorGesmViPdeO7Q6Ynl357GcZeC0ZelDix+Z8PsrXqyRqtZsFeh%22}; _gat_UA-41740027-4=1',
            'origin': 'https://accounts.snapchat.com',
            'referer': 'https://accounts.snapchat.com/',
            'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'same-origin',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        }
        data = {
            'requested_username': Username,
            'xsrf_token': 'jRBXY6u7yIGKLWwRe2frOA'
        }
        re = requests.post(url,headers=headers,data=data)
        if re.status_code == 200:
            da = re.json()
            if da['reference']['status_code'] == "OK":
                print(f'\033[92mNya >> @{Username}')
                with open('User.Nya.txt','a') as f:
                    f.write(Username + '\n')
            else:
                print(f'\033[91m Am Usera Haya >> @{Username}')
        else:
            pass
Snap()


