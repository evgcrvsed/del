import customtkinter
import json
import time
import os
from fake_useragent import UserAgent
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tg_bot import tg_msg
from functions import *

nicknames = [
    'машинистка пылесоса',
    'отдамся за 5 рублей',
    'Яша Лава',
    '-= [СаМаЯ] VREDna_Я =-',
    'пули от бабули',
    '•●•DиkаЯ_k0шkА♥РыЖеЙ_МаSтИ•●•',
    'Лошадь Ильича',
    'oderjimaya_героinom',
    'Девочка с характером',
    '_MaTЬ_ ПyTuHa',
    '*** К@пRизЮ/\ьk@ ***',
    'укладка на лобке',
    'Dо3а_dlya_pOnOsa',
    'SOS_ok на каблуке',
    '3a6aBHa9I',
    'мурчу стииральной машине',
    'супер-пупер падла',
    'Ťéтя Ŧwìx',
    'Моча_Авроры',
    'МаЛеНьКая_ХуЛиГаНкА',
    'наездница швабры',
    'ŤøПoВåЯ_ȚяHõЧķä',
    'Принцесса твоего очка',
    'Блоха в скафандре',
    'виртуальная сопля',
    '✬••٠·♥[в] O}I{иD@НиИ 4уD@♥••٠·✬',
    'Ляськи_Масяськи',
    'Анальная_букашка',
    '.•°*” ˜Ѽ♥$oOoLNЫ$I{o-Я ♥Ѽ ˜”*°•.',
    'разведчица раковины',
    'MOXnata_ya_kniginya',
    'geroin_nya',
    'Ҹёፐкȧя Мандმрūԋҟმ',
    'подполковник подпивас',
    'уборщик подвижного состава',
    'АгентПивасик1337',
    'жoпа в тумане',
    'He_TTpugyMaJl_Huk',
    'страхую яички',
    'коллекционер баребухов',
    '7he Дудец',
    'кунилингус за 50 тенге',
    'унитазный элементаль228',
    'AKTuBHbIu_roMeC',
    'сектор пудж',
    'дальнобойщик по губам',
    'Детиш люх',
    'Злобный_бульбулятор',
    'зашил туз',
    'СИСЬКАПЛЮЙ',
    'улиточная простата',
    'MaMkuH_DpAHuк',
    'увлажнитель мальчиков12',
    'Pa3฿aJluHа',
    'Носок судьбы15',
    'армированный армянин',
    'аистогусевая пчела',
    'СвяТой_ТапоК',
    'эскалатор на полставки',
    'мистер пенис',
    'Я ТуТ_Ты_ТрУп0_0',
    'Высоковольтный Майонез',
    'Kacnuuckuu_moHcTp',
    'Карманный Блоходав',
    'кожаный механик',
    'НОСИЛЬНИК МАМОНТОВ',
    'KoTuk 400kg',
    '0ЧКoДАВ',
    'ẴℕᎶỄŁ ༗ Ễб/\ӥ',
    'Я Hy6uK Tы Tpynuk',
    'лысая мембрана',
    'музыкальная вонь',
    'Ăристан♛♠Jlюбит♠►Свободу',
    'олежа трансмиссия',
    'рычаг для яйца',
    'двойной фанат спецоперации',
    'ВсЕ УмРуТ а Я гРеЙфРуКт',
    'пушащий денчик',
    'директор платного туалета',
    'под3aлyпная шмаль',
    'шиноби скрытого пула',
    'гей для душа',
    'пузо для арбуза',
    'славянский шкаф',
    'нюхач бебры',
    'экстракт кала',
    '2pac nakur',
    'пивная цистерна',
    'восставший из зада',
    '?Попа ищет ПрИкЛюченИй•',
    'стограмович32',
    'аннигилятор простаты',
    'горячий туалетный ершик',
    'мохнатый мотороллер',
    'хранительница чешки',
    'буханка пива',
    'черепашка-сиська',
    'анальная мозоль',
    'OG booba',
    'селедошный муравей',
    'женский сочник',
    'рядовой личинка',
    'осанка_бобра91',
    'анальный досмотр',
    'алкогольный конденсатор',
    'полноприводная мaндaвошка',
    'дегустатор сосков',
    'пт на клизму',
    'пт на силу(ю) детей',
    'бамбуча173',
    'Туалетная недостаточность',
    'чудовищный oбъeбoc',
    'волосатый трaxoдром',
    'батон под спайсом',
    'подзаборная eлдa',
    'курю чай',
    'дима ножик',
    'умер перед абортом',
    'mr.PeRforator'
]

def start_farm():
    with open('data/launched_accounts.json', 'w', encoding='utf=8') as file:
        null = {}
        json.dump(null, file, indent=4)
    with open('data/accounts.json', 'r') as file:
        data = json.load(file)
    for key in data.keys():
        print(key, 'this key')
        # password = get_password_by_key(key)  # worked
        # steam_id = get_id_by_key(key)  # worked
        nickname = random.choice(nicknames)
        research_accounts(key, nickname)
    print('Farm is done!')
    tg_msg('Farm is done!')


def research_accounts(key, nickname):
    login = key
    password = get_password_by_key(login)

    bot_nick = nickname
    real_name = 'Витюшенька'

    biogr = 'Просто аккаунт, что такого?'

    script_directory = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(script_directory, 'chromedriver2\chromedriver.exe')
    s = Service(executable_path=driver_path)

    user_agent = UserAgent.random
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')


    try:

        browser = webdriver.Chrome(service=s, options=options)
        browser.delete_all_cookies()
        browser.minimize_window()
        browser.get('https://store.steampowered.com/login/?redir=%3Fl%3Drussian&redir_ssl=1&snr=1_4_4__global-header')
        wait = WebDriverWait(browser, 60)

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'newlogindialog_TextInput_2eKVn')))
        inputs = browser.find_elements(By.CLASS_NAME, 'newlogindialog_TextInput_2eKVn')
        inputs[0].send_keys(login)
        inputs[1].send_keys(password)

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'newlogindialog_SubmitButton_2QgFE')))
        browser.find_element(By.CLASS_NAME, 'newlogindialog_SubmitButton_2QgFE').click()

        # guard
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'segmentedinputs_Input_HPSuA')))
        inputs = browser.find_elements(By.CLASS_NAME, 'segmentedinputs_Input_HPSuA')
        guard = getcode(get_shared_secret_by_key(login))
        for i in range(len(str(guard))):
            inputs[i].send_keys(str(guard)[i])

        # аватарка
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'miniprofile_hover')))
        browser.get(f'https://steamcommunity.com/profiles/{get_id_by_key(login)}/edit/avatar')

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'avatarcollection_AvatarPreview_29CGQ')))
        browser.find_element(By.CLASS_NAME, 'avatarcollection_AvatarPreview_29CGQ').click()

        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'DialogButton')))
        btns = browser.find_elements(By.CLASS_NAME, 'DialogButton')
        btns[2].click()
        time.sleep(0.5)

        # имя профиля, настоящее имя, личная ссылка, о себе
        browser.get(f'https://steamcommunity.com/profiles/{get_id_by_key(login)}/edit/info')

        wait.until(EC.presence_of_element_located((By.NAME, 'personaName')))
        inputs = browser.find_elements(By.NAME, 'personaName')
        inputs[0].clear()
        inputs[0].send_keys(bot_nick)

        inputs = browser.find_elements(By.NAME, 'real_name')
        inputs[0].clear()
        inputs[0].send_keys(real_name)

        inputs = browser.find_elements(By.NAME, 'summary')
        inputs[0].clear()
        inputs[0].send_keys(biogr)

        btns = browser.find_elements(By.CLASS_NAME, 'DialogButton')
        btns[0].click()

        # приватность ProfilePrivacyDropDown
        #browser.get(f'https://steamcommunity.com/profiles/{get_id_by_key(login)}/edit/settings')

        #select.select_by_index(1)

        time.sleep(0)
        print('end')
        browser.quit()
    except Exception as ex:
        tg_msg(ex)

    time.sleep(15)
    return

def check_ma_files():
    try:
        with open('data/accounts_without_ma_file.json', 'w', encoding='utf=8') as ohhh:
            null = {}
            json.dump(null, ohhh, indent=4)
        with open('data/accounts.json', 'r') as file:
            with_ma_files = []
            data = json.load(file)
            keys = data.keys()
            for key in keys:
                founded = False
                for filename in os.listdir('data/maFiles/'):
                    file_path = os.path.join('data/maFiles/', filename)
                    with open(file_path, encoding='utf-8') as file:
                        src = file.read()
                        data = json.loads(src)
                        account_name = data["account_name"]
                        if account_name == key:
                            founded = True
                if founded:
                    with_ma_files.append(key)
                else:
                    with open('data/accounts_without_ma_file.json', 'r') as ohh:
                        datass = json.load(ohh)
                    with open('data/accounts_without_ma_file.json', 'w', encoding='utf=8') as ohhh:
                        datass[key] = 'Without ma_file!'
                        json.dump(datass, ohhh, indent=4)
        if len(keys) == len(with_ma_files):
            print('All is good!')
            tg_msg('All is good!')
            installed_accs = ''
            tg_msg('Full installed Accounts:')
            for key in keys:
                installed_accs = installed_accs + key + ', '
            tg_msg(installed_accs)
            print('')
        else:
            tg_msg(datass)
            print('Founded Errors, check json!')
    except Exception as ex:
        tg_msg(ex)


def accounts_get():
    print('xd')
    pass

class MainWindow:
    def __init__(self):
        self.window_size = '400x130'
        root = customtkinter.CTk()
        root.resizable(width=False, height=False)
        root.iconbitmap('files/ui/icon.ico')
        root.geometry(self.window_size)
        root.title('Steam Manager')
        frame = customtkinter.CTkFrame(master=root)
        frame.pack(pady=20, padx=20, fill='both', expand=True)

        send_all_btn = customtkinter.CTkButton(master=frame, text="Update profiles", command=start_farm)
        send_all_btn.place(x=10, y=10)

        send_one_btn = customtkinter.CTkButton(master=frame, text="Scan valid Accounts", command=check_ma_files)
        send_one_btn.place(x=10, y=50)

        # entry = customtkinter.CTkEntry(master=frame, width=190, placeholder_text="example@mail.com")
        # entry.place(x=160, y=50)

        root.mainloop()