import importlib
import machineid
import cloudscraper
from selenium import webdriver
from pygame import mixer
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from time import sleep
from random import randint
import undetected_chromedriver as uc
import itertools
import PySimpleGUI as sg
import os
import sys
import datetime
import re
from python3_anticaptcha import ImageToTextTask
import requests
import json
from twocaptcha import TwoCaptcha
from selenium_stealth import stealth

solver = TwoCaptcha('4c4554f32ffcf0c497dda6d6497349de')
config = {
            'server':           '2captcha.com',
            'apiKey':           '4c4554f32ffcf0c497dda6d6497349de',
            'softId':            123,
            'callback':         'https://parsa.icu',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }

sg.theme('light grey1')
ROOT_PATH = './'
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def find_regex_1(k, s):
    reg = f'{k}\s*=\s*(\S+.*)'
    return re.search(reg, s).group(1)

def read_configs(config_file):
        with open(config_file, "r") as f:
            content = f.read()
            visa_type = find_regex_1('Visa Type', content)
            name = find_regex_1('Name', content)
            last_name = find_regex_1('Last Name', content)
            gender = find_regex_1('Gender', content)
            birth_date = find_regex_1('Date of Birth', content)
            birth_place = find_regex_1('Place of Birth', content)
            birth_country = find_regex_1('Country of Birth', content)
            c_nationality = find_regex_1('Current Nationality', content)
            o_nationality = find_regex_1('Original Nationality', content)
            m_status = find_regex_1('Marital Status', content)
            passport_num = find_regex_1('Passport Number', content)
            issue_date = find_regex_1('Date of Issue', content)
            valid_date = find_regex_1('Valid until', content)
            issue_auth = find_regex_1('Issuing Authority', content)
            country = find_regex_1('Country', content)
            state = find_regex_1('State', content)
            city = find_regex_1('City', content)
            address = find_regex_1('Address', content)
            postal_code = find_regex_1('Postal Code', content)
            email = find_regex_1('E-mail', content)
            mobile = find_regex_1('Mobile', content)
            entries_num = find_regex_1('Number of Entries', content)
            duration = find_regex_1('Duration of Stay', content)
            travel_date = find_regex_1('Intended date of journey', content)
            ref_num = find_regex_1('Application Reference Number', content)
            guarantor_lastname = find_regex_1('Guarantor Surname', content)
            guarantor_name = find_regex_1('Guarantor First Name', content)
            guarantor_nationality = find_regex_1('Guarantor Nationality', content)
            guarantor_state = find_regex_1('Guarantor State', content)
            guarantor_city = find_regex_1('Guarantor City', content)
            guarantor_address = find_regex_1('Guarantor Address', content)
            guarantor_zip_code = find_regex_1('Guarantor Zip Code', content)
            license_code = find_regex_1('LICENSE CODE', content)
            activation_code = find_regex_1('ACTIVATION CODE ', content)
        return visa_type, name, last_name, gender, birth_date, birth_place, birth_country, c_nationality, o_nationality, m_status, passport_num, issue_date, valid_date, issue_auth, country, state, city, address, postal_code, email, mobile, entries_num, duration, travel_date, ref_num, guarantor_lastname, guarantor_name, guarantor_nationality, guarantor_state, guarantor_city, guarantor_address, guarantor_zip_code, license_code, activation_code

visa_type, name, last_name, gender, birth_date, birth_place, birth_country, c_nationality, o_nationality, m_status, passport_num, issue_date, valid_date, issue_auth, country, state, city, address, postal_code, email, mobile, entries_num, duration, travel_date, ref_num, guarantor_lastname, guarantor_name, guarantor_nationality, guarantor_state, guarantor_city, guarantor_address, guarantor_zip_code, license_code, activation_code  = read_configs('form.txt')
def custom_meter_example():
    layout = [[sg.Text('Validating your License and Machine ', justification='left', font=("iranyekan"))],
              [sg.ProgressBar(1, orientation='h', size=(35, 20), key='progress')],
              [sg.Cancel('Close')]]
    now = datetime.datetime.now()
    future = now + datetime.timedelta(seconds=5)
    window = sg.Window('License Validating', layout ,font=("iranyekan"), icon="logo.ico", element_justification='l')
    progress_bar = window['progress']
    while True:
        delta = future - datetime.datetime.now()
        sec_left = delta.seconds
        event, values = window.read(timeout=100)
        progress_bar.update_bar(5-sec_left, 5)
        if event in (None, 'Close') or sec_left <= 0:
            break
    window.close()

custom_meter_example()
while True:
    try:
        requests.get('https://www.google.com/').status_code
        break
    except:
        sg.popup('You have to be connected to the internet for license validation, make sure you are connected to internet and re-open the application')
        break
def activate_license(license_key):
  machine_fingerprint = machineid.hashed_id('example-app')
  validation = requests.post(
    "https://api.keygen.sh/v1/accounts/d1f000c1-8f6a-4b57-ad04-f630d15740f3/licenses/actions/validate-key",
    headers={
      "Content-Type": "application/vnd.api+json",
      "Accept": "application/vnd.api+json"
    },
    data=json.dumps({
      "meta": {
        "scope": { "fingerprint": machine_fingerprint },
        "key": license_code
      }
    })
  ).json()
  # If the license is valid for the current machine, that means it has
  # already been activated. We can return early.
  if validation["meta"]["valid"]:
    sg.Popup('Congrats! your License and Machine match our criteria')
    chromedriver_path = './chromedriver.exe'
    options = webdriver.ChromeOptions()
    # options.add_extension('./auto-click.crx')
    options.add_argument("--disable-blink-features")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = uc.Chrome(options=options, executable_path=chromedriver_path)
    driver.maximize_window()
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    def mode1_submit():
        main_layout = [
            [sg.Text('Please provide your Application Details with uppercase', justification='center', font='arial')],
            [sg.Text('Personal Details', size=(20, 1), justification='left', font='arial 14 bold')],
            [sg.Text('First Name', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-IN_NAME-', size=(25, 1), default_text=name),
             sg.Text('Visa Type', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['Elective Residence', 'Exchange Program (ERASMUS)', 'Family Reunion', 'Family Visit',
                 'Long Term Medical Treatment', 'Long Term Research', 'PHD', 'Re-entry', 'Salaried Employment',
                 'Self-Employed Freelance', 'Self-Employment Businessowner', 'Self-Employment Corporate Role',
                 'Self-Employment Sport Activity', 'Short Research', 'Transport', 'University Enrollment',
                 'University Pre-enrollment'], key="vtype", size=(25, 1), default_value=visa_type)],
            [sg.Text('Last Name', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-IN_LAST-', size=(25, 1), default_text=last_name),
             sg.Text('Gender', size=(15, 1), justification='left', font='arial'),
             sg.Combo(['Male', 'Female'], key="-Gender-", size=(25, 1), default_value=gender)],
            [sg.Text('Birth Country', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA',
                 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA',
                 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL',
                 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
                 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD',
                 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS',
                 'CONGO, DEMOCRATIC REPUBLIC OF THE', 'CONGO, REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA',
                 "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'Curacao', 'DENMARK', 'DJIBOUTI',
                 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA',
                 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND',
                 'FRANCE', 'FRENCH GUIANA', 'FRENCH METROPOLITAN', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES',
                 'GABON', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE',
                 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS',
                 'HOLY SEE (VATICAN CITY)', 'HONDURAS', 'HONG KONG (SAR)', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA',
                 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA',
                 'KIRIBATI', 'KOREA, NORTH', 'KOREA, SOUTH', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON',
                 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO',
                 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI',
                 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO',
                 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT',
                 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES',
                 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND',
                 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA',
                 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN ISLANDS', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR',
                 'REPUBLIC OF KOSOVO', 'REUNION', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT HELENA',
                 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT PIERRE AND MIQUELON',
                 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA',
                 'SENEGAL', 'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE',
                 'SLOVAK REPUBLIC', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA',
                 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA',
                 'STATE OF PALESTINE', 'STATELESS', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN ISLANDS', 'SWAZILAND',
                 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'THE GAMBIA',
                 'TIBET', 'TOGO', 'TOKELAU', 'TONGA', 'TRAVEL DOCUMENT ISSUED BY INDIA',
                 'TRAVEL DOCUMENT ISSUED BY OTHERS', 'TRAVEL DOCUMENT ISSUED BY USA', 'TRINIDAD AND TOBAGO', 'TUNISIA',
                 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE',
                 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS',
                 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 'VIRGIN ISLANDS (UK)',
                 'VIRGIN ISLANDS (US)', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZAIRE', 'ZAMBIA', 'ZIMBABWE'],
                key='bcountry', default_value=birth_country, size=(25, 1))
                , sg.Text('Place of Birth', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-IN_BIRTH_PLACE-', size=(25, 1), default_text=birth_place)],
            [sg.Text('Date of Birth', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-IN_BIRTH-', size=(25, 1), default_text=birth_date),
             sg.Text('Current Nationality', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA',
                 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA',
                 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL',
                 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
                 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD',
                 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS',
                 'CONGO, DEMOCRATIC REPUBLIC OF THE', 'CONGO, REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA',
                 "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'Curacao', 'DENMARK', 'DJIBOUTI',
                 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA',
                 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND',
                 'FRANCE', 'FRENCH GUIANA', 'FRENCH METROPOLITAN', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES',
                 'GABON', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE',
                 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS',
                 'HOLY SEE (VATICAN CITY)', 'HONDURAS', 'HONG KONG (SAR)', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA',
                 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA',
                 'KIRIBATI', 'KOREA, NORTH', 'KOREA, SOUTH', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON',
                 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO',
                 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI',
                 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO',
                 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT',
                 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES',
                 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND',
                 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA',
                 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN ISLANDS', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR',
                 'REPUBLIC OF KOSOVO', 'REUNION', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT HELENA',
                 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT PIERRE AND MIQUELON',
                 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA',
                 'SENEGAL', 'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE',
                 'SLOVAK REPUBLIC', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA',
                 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA',
                 'STATE OF PALESTINE', 'STATELESS', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN ISLANDS', 'SWAZILAND',
                 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'THE GAMBIA',
                 'TIBET', 'TOGO', 'TOKELAU', 'TONGA', 'TRAVEL DOCUMENT ISSUED BY INDIA',
                 'TRAVEL DOCUMENT ISSUED BY OTHERS', 'TRAVEL DOCUMENT ISSUED BY USA', 'TRINIDAD AND TOBAGO', 'TUNISIA',
                 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE',
                 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS',
                 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 'VIRGIN ISLANDS (UK)',
                 'VIRGIN ISLANDS (US)', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZAIRE', 'ZAMBIA', 'ZIMBABWE'],
                key='cnationality', default_value=c_nationality, size=(25, 1))],
            [sg.Text('Example Format:', size=(15, 0), justification='left', font='arial'),
             sg.Text('1995-JUL-09 (YYYY-MMM-DD)', size=(25, 0), justification='left', font='arial', text_color='red'),
             sg.Text('Original Nationality', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA',
                 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA',
                 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL',
                 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
                 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD',
                 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS',
                 'CONGO, DEMOCRATIC REPUBLIC OF THE', 'CONGO, REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA',
                 "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'Curacao', 'DENMARK', 'DJIBOUTI',
                 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA',
                 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND',
                 'FRANCE', 'FRENCH GUIANA', 'FRENCH METROPOLITAN', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES',
                 'GABON', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE',
                 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS',
                 'HOLY SEE (VATICAN CITY)', 'HONDURAS', 'HONG KONG (SAR)', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA',
                 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA',
                 'KIRIBATI', 'KOREA, NORTH', 'KOREA, SOUTH', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON',
                 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO',
                 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI',
                 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO',
                 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT',
                 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES',
                 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND',
                 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA',
                 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN ISLANDS', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR',
                 'REPUBLIC OF KOSOVO', 'REUNION', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT HELENA',
                 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT PIERRE AND MIQUELON',
                 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA',
                 'SENEGAL', 'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE',
                 'SLOVAK REPUBLIC', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA',
                 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA',
                 'STATE OF PALESTINE', 'STATELESS', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN ISLANDS', 'SWAZILAND',
                 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'THE GAMBIA',
                 'TIBET', 'TOGO', 'TOKELAU', 'TONGA', 'TRAVEL DOCUMENT ISSUED BY INDIA',
                 'TRAVEL DOCUMENT ISSUED BY OTHERS', 'TRAVEL DOCUMENT ISSUED BY USA', 'TRINIDAD AND TOBAGO', 'TUNISIA',
                 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE',
                 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS',
                 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 'VIRGIN ISLANDS (UK)',
                 'VIRGIN ISLANDS (US)', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZAIRE', 'ZAMBIA', 'ZIMBABWE'],
                key='onationality', default_value=o_nationality, size=(25, 1))],
            [sg.Text('Marital Status', size=(15, 1), justification='left', font='arial'),
             sg.Combo(['SINGLE', 'MARRIED', 'SEPERATED', 'DIVORCED', 'WIDOW'], key="mstatus", size=(25, 1),
                      default_value=m_status)],
            [sg.Text('Passport Details', size=(20, 1), justification='left', font='arial 14 bold')],
            [sg.Text('Passport Number', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-Passport-', size=(25, 1), default_text=passport_num),
             sg.Text('Issuing Authority', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-Issue_auth-', size=(25, 1), default_text=issue_auth)],
            [sg.Text('Date of Issue', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-date_issue-', size=(25, 1), default_text=issue_date),
             sg.Text('Valid Until', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-v_date-', size=(25, 1), default_text=valid_date)],
            [sg.Text('Example Format:', size=(15, 0), justification='left', font='arial'),
             sg.Text('1995-JUL-09 (YYYY-MMM-DD)', size=(25, 0), justification='left', font='arial', text_color='red'),
             sg.Text('Example Format:', size=(15, 0), justification='left', font='arial'),
             sg.Text('1995-JUL-09 (YYYY-MMM-DD)', size=(25, 0), justification='left', font='arial', text_color='red')],
            [sg.Text('Address and Contact Details', size=(30, 1), justification='left', font='arial 14 bold')],
            [sg.Text('Country', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA',
                 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA',
                 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL',
                 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
                 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD',
                 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS',
                 'CONGO, DEMOCRATIC REPUBLIC OF THE', 'CONGO, REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA',
                 "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'Curacao', 'DENMARK', 'DJIBOUTI',
                 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR',
                 'EQUATORIAL GUINEA', 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)',
                 'FAROE ISLANDS', 'FIJI', 'FINLAND', 'FRANCE', 'FRENCH GUIANA', 'FRENCH METROPOLITAN',
                 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES', 'GABON', 'GEORGIA', 'GERMANY', 'GHANA',
                 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE', 'GUAM', 'GUATEMALA', 'GUINEA',
                 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS', 'HOLY SEE (VATICAN CITY)',
                 'HONDURAS', 'HONG KONG (SAR)', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'IRELAND',
                 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA', 'KIRIBATI', 'KOREA, NORTH',
                 'KOREA, SOUTH', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYA',
                 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF',
                 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI', 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE',
                 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO', 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA',
                 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT', 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA',
                 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES', 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA',
                 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND', 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN',
                 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA', 'PARAGUAY', 'PERU', 'PHILIPPINES',
                 'PITCAIRN ISLANDS', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR', 'REPUBLIC OF KOSOVO', 'REUNION',
                 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT HELENA', 'SAINT KITTS AND NEVIS', 'SAINT LUCIA',
                 'SAINT PIERRE AND MIQUELON', 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO',
                 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA', 'SENEGAL', 'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES',
                 'SIERRA LEONE', 'SINGAPORE', 'SLOVAK REPUBLIC', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA',
                 'SOUTH AFRICA', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA',
                 'STATE OF PALESTINE', 'STATELESS', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN ISLANDS',
                 'SWAZILAND', 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND',
                 'THE GAMBIA', 'TIBET', 'TOGO', 'TOKELAU', 'TONGA', 'TRAVEL DOCUMENT ISSUED BY INDIA',
                 'TRAVEL DOCUMENT ISSUED BY OTHERS', 'TRAVEL DOCUMENT ISSUED BY USA', 'TRINIDAD AND TOBAGO',
                 'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE',
                 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS',
                 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 'VIRGIN ISLANDS (UK)',
                 'VIRGIN ISLANDS (US)', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZAIRE', 'ZAMBIA',
                 'ZIMBABWE'], key='country', disabled=True, default_value=country, size=(25, 1)),
             sg.Text('State', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-state-', size=(25, 1), default_text=state)],
            [sg.Text('City', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-city-', size=(25, 1), default_text=city), sg.Text(
                'Type your (State) and (City) like how you select on the website Otherwise the app select the nearest match by dropdown',
                size=(50, 0), justification='left', font='arial 12', text_color='red')],
            [sg.Text('Address', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-address-', size=(70, 3), default_text=address)],
            [sg.Text('Postal Code', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-postal_code-', size=(25, 1), default_text=postal_code),
             sg.Text('Email', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-email-', size=(25, 3), default_text=email)],
            [sg.Text('Mobile (+98)', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-mobile-', size=(25, 3), default_text=mobile)],
            [sg.Text('Visa Details', size=(20, 1), justification='left', font='arial 14 bold')],
            [sg.Text('Number of Entries', size=(15, 1), justification='left', font='arial'),
             sg.Combo(['SINGLE', 'TWO', 'MULTIPLE'], key="-entry_num-", size=(25, 1), default_value=entries_num),
             sg.Text('Duration of Stay', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-duration-', size=(25, 3), default_text=duration)],
            [sg.Text('Date of journey', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-travel-date-', size=(25, 1), default_text=travel_date)],
            [sg.Text('Example Format:', size=(15, 0), justification='left', font='arial'),
             sg.Text('1995-JUL-09 (YYYY-MMM-DD)', size=(25, 0), justification='left', font='arial', text_color='red')],
            [sg.Submit('Submit Form', font='arial'), sg.Submit('Use Current Data', font='arial'),
             sg.Cancel('Cancel', font='arial')]]
        layout = [[sg.Column(main_layout, element_justification='l', scrollable=True, vertical_scroll_only=True,
                             size=(755, 500))]]
        window = sg.Window('Form Submission', layout, font='arial', resizable=True, element_justification='l',
                           size=(755, 500))
        input_key_list = [key for key, values in window.key_dict.items()
                          if isinstance(values, sg.InputText)]
        event, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            driver.quit()
            sys.exit()
        if event == 'Use Current Data':
            if all(map(str.strip, [values[key] for key in input_key_list])):
                sg.Popup(f'Alright We Try to Bypass Cloudflare Security Now')
            else:
                sg.Popup(f'All Fields are Required')

            window.close()
        elif event == 'Submit Form':
            if all(map(str.strip, [values[key] for key in input_key_list])):
                form_name = values['-gname-']
                read_configs('form.txt')
                formm = "form.txt"
                with open(formm, 'r+') as f:
                    text = f.read()
                    text = re.sub(form_name, name, text)
                    f.seek(0)
                    f.write(text)
                    f.truncate()
            else:
                sg.Popup(f'All Fields are Required')
            window.close()
        window.close()

    def mode1_submit_guarantor():
        main_layout = [
            [sg.Text('Please provide your Application Details with uppercase', justification='center', font='arial')],
            [sg.Text('Personal Details', size=(20, 1), justification='left', font='arial 14 bold')],
            [sg.Text('First Name', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-gname-', size=(25, 1), default_text=name),
             sg.Text('Visa Type', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['Elective Residence', 'Exchange Program (ERASMUS)', 'Family Reunion', 'Family Visit',
                 'Long Term Medical Treatment', 'Long Term Research', 'PHD', 'Re-entry', 'Salaried Employment',
                 'Self-Employed Freelance', 'Self-Employment Businessowner', 'Self-Employment Corporate Role',
                 'Self-Employment Sport Activity', 'Short Research', 'Transport', 'University Enrollment',
                 'University Pre-enrollment'], key="vtype", size=(25, 1), default_value=visa_type)],
            [sg.Text('Last Name', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='glastname', size=(25, 1), default_text=last_name),
             sg.Text('Gender', size=(15, 1), justification='left', font='arial'),
             sg.Combo(['Male', 'Female'], key="-Gender-", size=(25, 1), default_value=gender)],
            [sg.Text('Birth Country', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA',
                 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA',
                 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL',
                 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
                 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD',
                 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS',
                 'CONGO, DEMOCRATIC REPUBLIC OF THE', 'CONGO, REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA',
                 "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'Curacao', 'DENMARK', 'DJIBOUTI',
                 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA',
                 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND',
                 'FRANCE', 'FRENCH GUIANA', 'FRENCH METROPOLITAN', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES',
                 'GABON', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE',
                 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS',
                 'HOLY SEE (VATICAN CITY)', 'HONDURAS', 'HONG KONG (SAR)', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA',
                 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA',
                 'KIRIBATI', 'KOREA, NORTH', 'KOREA, SOUTH', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON',
                 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO',
                 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI',
                 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO',
                 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT',
                 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES',
                 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND',
                 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA',
                 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN ISLANDS', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR',
                 'REPUBLIC OF KOSOVO', 'REUNION', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT HELENA',
                 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT PIERRE AND MIQUELON',
                 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA',
                 'SENEGAL', 'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE',
                 'SLOVAK REPUBLIC', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA',
                 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA',
                 'STATE OF PALESTINE', 'STATELESS', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN ISLANDS', 'SWAZILAND',
                 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'THE GAMBIA',
                 'TIBET', 'TOGO', 'TOKELAU', 'TONGA', 'TRAVEL DOCUMENT ISSUED BY INDIA',
                 'TRAVEL DOCUMENT ISSUED BY OTHERS', 'TRAVEL DOCUMENT ISSUED BY USA', 'TRINIDAD AND TOBAGO', 'TUNISIA',
                 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE',
                 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS',
                 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 'VIRGIN ISLANDS (UK)',
                 'VIRGIN ISLANDS (US)', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZAIRE', 'ZAMBIA', 'ZIMBABWE'],
                key='bcountry', default_value=birth_country, size=(25, 1))
                , sg.Text('Place of Birth', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-IN_BIRTH_PLACE-', size=(25, 1), default_text=birth_place)],
            [sg.Text('Date of Birth', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-IN_BIRTH-', size=(25, 1), default_text=birth_date),
             sg.Text('Current Nationality', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA',
                 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA',
                 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL',
                 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
                 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD',
                 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS',
                 'CONGO, DEMOCRATIC REPUBLIC OF THE', 'CONGO, REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA',
                 "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'Curacao', 'DENMARK', 'DJIBOUTI',
                 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA',
                 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND',
                 'FRANCE', 'FRENCH GUIANA', 'FRENCH METROPOLITAN', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES',
                 'GABON', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE',
                 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS',
                 'HOLY SEE (VATICAN CITY)', 'HONDURAS', 'HONG KONG (SAR)', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA',
                 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA',
                 'KIRIBATI', 'KOREA, NORTH', 'KOREA, SOUTH', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON',
                 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO',
                 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI',
                 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO',
                 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT',
                 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES',
                 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND',
                 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA',
                 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN ISLANDS', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR',
                 'REPUBLIC OF KOSOVO', 'REUNION', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT HELENA',
                 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT PIERRE AND MIQUELON',
                 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA',
                 'SENEGAL', 'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE',
                 'SLOVAK REPUBLIC', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA',
                 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA',
                 'STATE OF PALESTINE', 'STATELESS', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN ISLANDS', 'SWAZILAND',
                 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'THE GAMBIA',
                 'TIBET', 'TOGO', 'TOKELAU', 'TONGA', 'TRAVEL DOCUMENT ISSUED BY INDIA',
                 'TRAVEL DOCUMENT ISSUED BY OTHERS', 'TRAVEL DOCUMENT ISSUED BY USA', 'TRINIDAD AND TOBAGO', 'TUNISIA',
                 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE',
                 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS',
                 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 'VIRGIN ISLANDS (UK)',
                 'VIRGIN ISLANDS (US)', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZAIRE', 'ZAMBIA', 'ZIMBABWE'],
                key='cnationality', default_value=c_nationality, size=(25, 1))],
            [sg.Text('Example Format:', size=(15, 0), justification='left', font='arial'),
             sg.Text('1995-JUL-09 (YYYY-MMM-DD)', size=(25, 0), justification='left', font='arial', text_color='red'),
             sg.Text('Original Nationality', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA',
                 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA',
                 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL',
                 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
                 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD',
                 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS',
                 'CONGO, DEMOCRATIC REPUBLIC OF THE', 'CONGO, REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA',
                 "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'Curacao', 'DENMARK', 'DJIBOUTI',
                 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA',
                 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND',
                 'FRANCE', 'FRENCH GUIANA', 'FRENCH METROPOLITAN', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES',
                 'GABON', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE',
                 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS',
                 'HOLY SEE (VATICAN CITY)', 'HONDURAS', 'HONG KONG (SAR)', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA',
                 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA',
                 'KIRIBATI', 'KOREA, NORTH', 'KOREA, SOUTH', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON',
                 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO',
                 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI',
                 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO',
                 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT',
                 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES',
                 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND',
                 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA',
                 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN ISLANDS', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR',
                 'REPUBLIC OF KOSOVO', 'REUNION', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT HELENA',
                 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT PIERRE AND MIQUELON',
                 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA',
                 'SENEGAL', 'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE',
                 'SLOVAK REPUBLIC', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA',
                 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA',
                 'STATE OF PALESTINE', 'STATELESS', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN ISLANDS', 'SWAZILAND',
                 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'THE GAMBIA',
                 'TIBET', 'TOGO', 'TOKELAU', 'TONGA', 'TRAVEL DOCUMENT ISSUED BY INDIA',
                 'TRAVEL DOCUMENT ISSUED BY OTHERS', 'TRAVEL DOCUMENT ISSUED BY USA', 'TRINIDAD AND TOBAGO', 'TUNISIA',
                 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE',
                 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS',
                 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 'VIRGIN ISLANDS (UK)',
                 'VIRGIN ISLANDS (US)', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZAIRE', 'ZAMBIA', 'ZIMBABWE'],
                key='onationality', default_value=o_nationality, size=(25, 1))],
            [sg.Text('Marital Status', size=(15, 1), justification='left', font='arial'),
             sg.Combo(['SINGLE', 'MARRIED', 'SEPERATED', 'DIVORCED', 'WIDOW'], key="mstatus", size=(25, 1),
                      default_value=m_status)],
            [sg.Text('Passport Details', size=(20, 1), justification='left', font='arial 14 bold')],
            [sg.Text('Passport Number', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-Passport-', size=(25, 1), default_text=passport_num),
             sg.Text('Issuing Authority', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-Issue_auth-', size=(25, 1), default_text=issue_auth)],
            [sg.Text('Date of Issue', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-date_issue-', size=(25, 1), default_text=issue_date),
             sg.Text('Valid Until', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-v_date-', size=(25, 1), default_text=valid_date)],
            [sg.Text('Example Format:', size=(15, 0), justification='left', font='arial'),
             sg.Text('1995-JUL-09 (YYYY-MMM-DD)', size=(25, 0), justification='left', font='arial', text_color='red'),
             sg.Text('Example Format:', size=(15, 0), justification='left', font='arial'),
             sg.Text('1995-JUL-09 (YYYY-MMM-DD)', size=(25, 0), justification='left', font='arial', text_color='red')],
            [sg.Text('Address and Contact Details', size=(30, 1), justification='left', font='arial 14 bold')],
            [sg.Text('Country', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA',
                 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA',
                 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL',
                 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
                 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD',
                 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS',
                 'CONGO, DEMOCRATIC REPUBLIC OF THE', 'CONGO, REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA',
                 "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'Curacao', 'DENMARK', 'DJIBOUTI',
                 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR',
                 'EQUATORIAL GUINEA', 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)',
                 'FAROE ISLANDS', 'FIJI', 'FINLAND', 'FRANCE', 'FRENCH GUIANA', 'FRENCH METROPOLITAN',
                 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES', 'GABON', 'GEORGIA', 'GERMANY', 'GHANA',
                 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE', 'GUAM', 'GUATEMALA', 'GUINEA',
                 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS', 'HOLY SEE (VATICAN CITY)',
                 'HONDURAS', 'HONG KONG (SAR)', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA', 'IRAN', 'IRAQ', 'IRELAND',
                 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA', 'KIRIBATI', 'KOREA, NORTH',
                 'KOREA, SOUTH', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON', 'LESOTHO', 'LIBERIA', 'LIBYA',
                 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF',
                 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI', 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE',
                 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO', 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA',
                 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT', 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA',
                 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES', 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA',
                 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND', 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN',
                 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA', 'PARAGUAY', 'PERU', 'PHILIPPINES',
                 'PITCAIRN ISLANDS', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR', 'REPUBLIC OF KOSOVO', 'REUNION',
                 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT HELENA', 'SAINT KITTS AND NEVIS', 'SAINT LUCIA',
                 'SAINT PIERRE AND MIQUELON', 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO',
                 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA', 'SENEGAL', 'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES',
                 'SIERRA LEONE', 'SINGAPORE', 'SLOVAK REPUBLIC', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA',
                 'SOUTH AFRICA', 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA',
                 'STATE OF PALESTINE', 'STATELESS', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN ISLANDS',
                 'SWAZILAND', 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND',
                 'THE GAMBIA', 'TIBET', 'TOGO', 'TOKELAU', 'TONGA', 'TRAVEL DOCUMENT ISSUED BY INDIA',
                 'TRAVEL DOCUMENT ISSUED BY OTHERS', 'TRAVEL DOCUMENT ISSUED BY USA', 'TRINIDAD AND TOBAGO',
                 'TUNISIA', 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE',
                 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS',
                 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 'VIRGIN ISLANDS (UK)',
                 'VIRGIN ISLANDS (US)', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZAIRE', 'ZAMBIA',
                 'ZIMBABWE'], key='country', disabled=True, default_value=country, size=(25, 1)),
             sg.Text('State', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-state-', size=(25, 1), default_text=state)],
            [sg.Text('City', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-city-', size=(25, 1), default_text=city), sg.Text(
                'Type your (State) and (City) like how you select on the website Otherwise the app select the nearest match by dropdown',
                size=(50, 0), justification='left', font='arial 12', text_color='red')],
            [sg.Text('Address', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-address-', size=(70, 3), default_text=address)],
            [sg.Text('Postal Code', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-postal_code-', size=(25, 1), default_text=postal_code),
             sg.Text('Email', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-email-', size=(25, 3), default_text=email)],
            [sg.Text('Mobile (+98)', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-mobile-', size=(25, 3), default_text=mobile)],
            [sg.Text('Visa Details', size=(20, 1), justification='left', font='arial 14 bold')],
            [sg.Text('Number of Entries', size=(15, 1), justification='left', font='arial'),
             sg.Combo(['SINGLE', 'TWO', 'MULTIPLE'], key="-entry_num-", size=(25, 1), default_value=entries_num),
             sg.Text('Duration of Stay', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-duration-', size=(25, 3), default_text=duration)],
            [sg.Text('Date of journey', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-travel-date-', size=(25, 1), default_text=travel_date)],
            [sg.Text('Example Format:', size=(15, 0), justification='left', font='arial'),
             sg.Text('1995-JUL-09 (YYYY-MMM-DD)', size=(25, 0), justification='left', font='arial', text_color='red')],
            [sg.Text('Guarantor Details', size=(20, 1), justification='left', font='arial 14 bold')],
            [sg.Text('Guarantor First Name', size=(16, 1), justification='left', font='arial'),
             sg.InputText(key='-gname2-', size=(25, 1), default_text=guarantor_name),
             sg.Text('Guarantor Nationality', size=(15, 1), justification='left', font='arial'), sg.Combo(
                ['AFGHANISTAN', 'ALAND ISLANDS', 'ALBANIA', 'ALGERIA', 'AMERICAN SAMOA', 'ANDORRA', 'ANGOLA',
                 'ANGUILLA', 'ANTARCTICA', 'ANTIGUA AND BARBUDA', 'ARGENTINA', 'ARMENIA', 'ARUBA', 'AUSTRALIA',
                 'AUSTRIA', 'AZERBAIJAN', 'BAHAMAS', 'BAHRAIN', 'BANGLADESH', 'BARBADOS', 'BELARUS', 'BELGIUM',
                 'BELIZE', 'BENIN', 'BERMUDA', 'BHUTAN', 'BOLIVIA', 'BOSNIA', 'BOTSWANA', 'BOUVET ISLAND', 'BRAZIL',
                 'BRITISH INDIAN OCEAN TERRITORY', 'BRUNEI DARUSSALAM', 'BULGARIA', 'BURKINA FASO', 'BURUNDI',
                 'CAMBODIA', 'CAMEROON', 'CANADA', 'CAPE VERDE', 'CAYMAN ISLANDS', 'CENTRAL AFRICAN REPUBLIC', 'CHAD',
                 'CHILE', 'CHINA', 'CHRISTMAS ISLAND', 'COCOS (KEELING) ISLANDS', 'COLOMBIA', 'COMOROS',
                 'CONGO, DEMOCRATIC REPUBLIC OF THE', 'CONGO, REPUBLIC OF THE', 'COOK ISLANDS', 'COSTA RICA',
                 "COTE D'IVOIRE", 'CROATIA', 'CUBA', 'CYPRUS', 'CZECH REPUBLIC', 'Curacao', 'DENMARK', 'DJIBOUTI',
                 'DOMINICA', 'DOMINICAN REPUBLIC', 'EAST TIMOR', 'ECUADOR', 'EGYPT', 'EL SALVADOR', 'EQUATORIAL GUINEA',
                 'ERITREA', 'ESTONIA', 'ETHIOPIA', 'FALKLAND ISLANDS (MALVINAS)', 'FAROE ISLANDS', 'FIJI', 'FINLAND',
                 'FRANCE', 'FRENCH GUIANA', 'FRENCH METROPOLITAN', 'FRENCH POLYNESIA', 'FRENCH SOUTHERN TERRITORIES',
                 'GABON', 'GEORGIA', 'GERMANY', 'GHANA', 'GIBRALTAR', 'GREECE', 'GREENLAND', 'GRENADA', 'GUADELOUPE',
                 'GUAM', 'GUATEMALA', 'GUINEA', 'GUINEA-BISSAU', 'GUYANA', 'HAITI', 'HEARD ISLAND AND MCDONALD ISLANDS',
                 'HOLY SEE (VATICAN CITY)', 'HONDURAS', 'HONG KONG (SAR)', 'HUNGARY', 'ICELAND', 'INDIA', 'INDONESIA',
                 'IRAN', 'IRAQ', 'IRELAND', 'ISRAEL', 'ITALY', 'JAMAICA', 'JAPAN', 'JORDAN', 'KAZAKHSTAN', 'KENYA',
                 'KIRIBATI', 'KOREA, NORTH', 'KOREA, SOUTH', 'KUWAIT', 'KYRGYZSTAN', 'LAOS', 'LATVIA', 'LEBANON',
                 'LESOTHO', 'LIBERIA', 'LIBYA', 'LIECHTENSTEIN', 'LITHUANIA', 'LUXEMBOURG', 'MACAO',
                 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF', 'MADAGASCAR', 'MALAWI', 'MALAYSIA', 'MALDIVES', 'MALI',
                 'MALTA', 'MARSHALL ISLANDS', 'MARTINIQUE', 'MAURITANIA', 'MAURITIUS', 'MAYOTTE', 'MEXICO',
                 'MICRONESIA, FEDERATED STATES OF', 'MOLDOVA', 'MONACO', 'MONGOLIA', 'MONTENEGRO', 'MONTSERRAT',
                 'MOROCCO', 'MOZAMBIQUE', 'MYANMAR', 'NAMIBIA', 'NAURU', 'NEPAL', 'NETHERLANDS', 'NETHERLANDS ANTILLES',
                 'NEW CALEDONIA', 'NEW ZEALAND', 'NICARAGUA', 'NIGER', 'NIGERIA', 'NIUE', 'NORFOLK ISLAND',
                 'NORTHERN MARIANA ISLANDS', 'NORWAY', 'OMAN', 'PAKISTAN', 'PALAU', 'PANAMA', 'PAPUA NEW GUINEA',
                 'PARAGUAY', 'PERU', 'PHILIPPINES', 'PITCAIRN ISLANDS', 'POLAND', 'PORTUGAL', 'PUERTO RICO', 'QATAR',
                 'REPUBLIC OF KOSOVO', 'REUNION', 'ROMANIA', 'RUSSIA', 'RWANDA', 'SAINT HELENA',
                 'SAINT KITTS AND NEVIS', 'SAINT LUCIA', 'SAINT PIERRE AND MIQUELON',
                 'SAINT VINCENT AND THE GRENADINES', 'SAMOA', 'SAN MARINO', 'SAO TOME AND PRINCIPE', 'SAUDI ARABIA',
                 'SENEGAL', 'SERBIA', 'SERBIA AND MONTENEGRO', 'SEYCHELLES', 'SIERRA LEONE', 'SINGAPORE',
                 'SLOVAK REPUBLIC', 'SLOVENIA', 'SOLOMON ISLANDS', 'SOMALIA', 'SOUTH AFRICA',
                 'SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS', 'SOUTH SUDAN', 'SPAIN', 'SRI LANKA',
                 'STATE OF PALESTINE', 'STATELESS', 'SUDAN', 'SURINAME', 'SVALBARD AND JAN MAYEN ISLANDS', 'SWAZILAND',
                 'SWEDEN', 'SWITZERLAND', 'SYRIA', 'TAIWAN', 'TAJIKISTAN', 'TANZANIA', 'THAILAND', 'THE GAMBIA',
                 'TIBET', 'TOGO', 'TOKELAU', 'TONGA', 'TRAVEL DOCUMENT ISSUED BY INDIA',
                 'TRAVEL DOCUMENT ISSUED BY OTHERS', 'TRAVEL DOCUMENT ISSUED BY USA', 'TRINIDAD AND TOBAGO', 'TUNISIA',
                 'TURKEY', 'TURKMENISTAN', 'TURKS AND CAICOS ISLANDS', 'TUVALU', 'UGANDA', 'UKRAINE',
                 'UNITED ARAB EMIRATES', 'UNITED KINGDOM', 'UNITED STATES', 'UNITED STATES MINOR OUTLYING ISLANDS',
                 'URUGUAY', 'UZBEKISTAN', 'VANUATU', 'VENEZUELA', 'VIETNAM', 'VIRGIN ISLANDS (UK)',
                 'VIRGIN ISLANDS (US)', 'WALLIS AND FUTUNA', 'WESTERN SAHARA', 'YEMEN', 'ZAIRE', 'ZAMBIA', 'ZIMBABWE'],
                key='gnationality', default_value=guarantor_nationality, size=(25, 1))],
            [sg.Text('Guarantor Last Name', size=(16, 1), justification='left', font='arial'),
             sg.InputText(key='-glastname2-', size=(25, 1), default_text=guarantor_lastname),
             sg.Text('State', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-gstate-', size=(25, 1), default_text=guarantor_state)],
            [sg.Text('Zip Code', size=(16, 1), justification='left', font='arial'),
             sg.InputText(key='-gzipcode2-', size=(25, 1), default_text=guarantor_zip_code),
             sg.Text('City', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-gcity-', size=(25, 1), default_text=guarantor_city)],
            [sg.Text('Address', size=(15, 1), justification='left', font='arial'),
             sg.InputText(key='-gaddress2-', size=(70, 3), default_text=guarantor_address)],
            [sg.Submit('Submit Form', font='arial'), sg.Submit('Use Current Data', font='arial'),
             sg.Cancel('Cancel', font='arial')]]
        layout = [[sg.Column(main_layout, element_justification='l', scrollable=True, vertical_scroll_only=True,
                             size=(755, 500))]]
        window = sg.Window('Form Submission', layout, font='arial', resizable=True, finalize=True,
                           element_justification='l', size=(755, 500))
        input_key_list = [key for key, values in window.key_dict.items()
                          if isinstance(values, sg.InputText)]
        event, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            driver.quit()
            sys.exit()
        if event == 'Use Current Data':
            if all(map(str.strip, [values[key] for key in input_key_list])):
                sg.Popup(f'Alright We Try to Bypass Cloudflare Security Now')
            else:
                sg.Popup(f'All Fields are Required')

            window.close()
        elif event == 'Submit Form':
            if all(map(str.strip, [values[key] for key in input_key_list])):
                form_name = values['-gname-']
                read_configs('form.txt')
                formm = "form.txt"
                with open(formm, 'r+') as f:
                    text = f.read()
                    text = re.sub(form_name, name, text)
                    f.seek(0)
                    f.write(text)
                    f.truncate()
            else:
                sg.Popup(f'All Fields are Required')
            window.close()
        window.close()

    def mode1_form_type():
        layout = [[sg.Text('Do You Have A Guarantor that need to Specify in your Submission Form?', size=(30, 3),
                           justification='center', font='arial 18')],
                  [sg.Button('YES I HAVE', size=(35, 1))],
                  [sg.Button("NO I DON'T", size=(35, 1))]]
        window = sg.Window('Guarantor', layout, font="arial", element_justification='center')
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            driver.quit()
            sys.exit()
        if event == 'YES I HAVE':
            window.close()
            mode1_submit_guarantor()
        if event == "NO I DON'T":
            window.close()
            mode1_submit()
        window.close()

    def mode2_submit():
        main_layout = [
            [sg.Text('Please provide your Application Details with uppercase', justification='center', font='arial')],
            [sg.Text('Retrieve Application', size=(20, 1), justification='left', font='arial 14 bold')],
            [sg.Text('Application Reference Number', size=(25, 1), justification='left', font='arial'),
             sg.InputText(key='-ref-number-', size=(25, 1), default_text=ref_num)],
            [sg.Text('Passport Number', size=(25, 1), justification='left', font='arial'),
             sg.InputText(key='-Passport-no-', size=(25, 1), default_text=passport_num)],
            [sg.Text('Date of Birth', size=(25, 1), justification='left', font='arial'),
             sg.InputText(key='-m2bdate-', size=(25, 1), default_text=birth_date)],
            [sg.Text('Example Format:', size=(25, 0), justification='left', font='arial'),
             sg.Text('1995-JUL-09 (YYYY-MMM-DD)', size=(25, 0), justification='left', font='arial', text_color='red')],
            [sg.Submit('Submit Form', font='arial'), sg.Submit('Use Current Data', font='arial'),
             sg.Cancel('Cancel', font='arial')]]
        layout = [[sg.Column(main_layout, element_justification='l')]]
        window = sg.Window('Form Submission', layout, font='arial', resizable=True, element_justification='l')
        input_key_list = [key for key, values in window.key_dict.items()
                          if isinstance(values, sg.InputText)]
        event, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            driver.quit()
            sys.exit()
        if event == 'Use Current Data':
            if all(map(str.strip, [values[key] for key in input_key_list])):
                sg.Popup(f'Alright We Try to Bypass Cloudflare Security Now')
            else:
                sg.Popup(f'All Fields are Required')

            window.close()
        elif event == 'Submit Form':
            mode2_ref_no = values['-ref-number-']
            read_configs('form.txt')
            formm = "form.txt"
            with open(formm, 'r+') as f:
                text = f.read()
                text = re.sub(ref_num, mode2_ref_no, text)
                f.seek(0)
                f.write(text)
                f.truncate()
            mode2_pass_no = values['-Passport-no-']
            read_configs('form.txt')
            formm = "form.txt"
            with open(formm, 'r+') as f:
                text = f.read()
                text = re.sub(mode2_pass_no, passport_num, text)
                f.seek(0)
                f.write(text)
                f.truncate()
            mode2_bdate = values['-m2bdate-']
            read_configs('form.txt')
            formm = "form.txt"
            with open(formm, 'r+') as f:
                text = f.read()
                text = re.sub(mode2_bdate, birth_date, text)
                f.seek(0)
                f.write(text)
                f.truncate()
            if all(map(str.strip, [values[key] for key in input_key_list])):
                sg.Popup(f'Alright We Try to Bypass Cloudflare Security Now')
            else:
                sg.Popup(f'All Fields are Required')
            window.close()
        window.close()

    def passport_error():
        try:
            current_application = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/a[3]")
            current_application.click()
            sleep(1)
            current_application_submit = driver.find_element("xpath", "/html/body/div[2]/div/div/div/div[2]/div/a[5]")
            current_application_submit.click()
            sleep(2)
            alert = driver.switch_to.alert
            alert.accept()
        except:
            pass

    def form_fill():
        sleep(randint(2, 3))
        driver.get('https://www.ckgsir.com/apply-for-visa')
        sleep(randint(1, 2))
        try:
            closebtn = driver.find_element_by_css_selector(
                "body > div.mfp-wrap.mfp-close-btn-in.mfp-auto-cursor.my-mfp-slide-bottom.mfp-ready > div > div > div > button")
            closebtn.click()
        except NoSuchElementException:
            closebtn2 = driver.find_element("xpath", "/html/body/div[2]/div/div/div/button")
            closebtn2.click()
        sleep(randint(2, 3))
        try:
            closebtn3 = driver.find_element("xpath", "/html/body/footer/div[4]/div/span/a")
            closebtn3.click()
        except:
            pass
        try:
            Individual1 = driver.find_element("xpath",
                                              "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[2]/div/div/div/label/div")
            Individual1.click()
        except NoSuchElementException:
            Individual2 = driver.find_element_by_css_selector(
                "#search-widget > div.box-content.apply-for-visa-content > div > div.form-group.row.highltd-blu > div.col-md-7.col-sm-7.col-mobi-12.col-xs-6 > div > div > div > label > div")
            Individual2.click()
        sleep(randint(2, 3))
        # driver.execute_script("document.body.style.zoom='90%'")

        uni_enroll_b = driver.find_element("xpath",
                                           "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[1]/div/div[2]/button").click()
        uni_enroll = driver.find_element("xpath",
                                         "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[1]/div/div[2]/div/div/input")
        uni_enroll.send_keys(visa_type)
        uni_enroll.send_keys(Keys.ENTER)
        sleep(randint(1, 2))

        lastname = driver.find_element("xpath",
                                       "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[3]/input")
        lastname.send_keys(last_name)

        firstname = driver.find_element("xpath",
                                        "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[4]/input")
        firstname.send_keys(name)

        if gender == 'Male':
            gendermale = driver.find_element("xpath",
                                             "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[6]/div/label[1]")
            gendermale.click()
        elif gender == 'Female':
            genderfemale = driver.find_element("xpath",
                                               "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[6]/div/label[2]")
            genderfemale.click()

        bdate = driver.find_element("xpath",
                                    "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[7]/div/span[1]/input")
        driver.execute_script("window.scrollBy(0, 400)")
        driver.execute_script("arguments[0].removeAttribute('readonly')", bdate)
        bdate.send_keys(birth_date)

        bplace = driver.find_element("xpath",
                                     "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[8]/input")
        bplace.send_keys(birth_place)

        b_country_b = driver.find_element("xpath",
                                          "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[10]/div/div[2]/button").click()
        b_country = driver.find_element("xpath",
                                        "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[10]/div/div[2]/div/div/input")
        b_country.send_keys(birth_country)
        b_country.send_keys(Keys.ENTER)

        current_nationality_b = driver.find_element("xpath",
                                                    "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[11]/div/div[2]/button").click()
        current_nationality = driver.find_element("xpath",
                                                  "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[11]/div/div[2]/div/div/input")
        current_nationality.send_keys(c_nationality)
        current_nationality.send_keys(Keys.ENTER)

        original_nationality_b = driver.find_element("xpath",
                                                     "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[12]/div/div[2]/button").click()
        original_nationality = driver.find_element("xpath",
                                                   "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[12]/div/div[2]/div/div/input")
        original_nationality.send_keys(o_nationality)
        original_nationality.send_keys(Keys.ENTER)

        marrage_b = driver.find_element("xpath",
                                        "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[14]/div/div[2]/button").click()
        marrage = driver.find_element("xpath",
                                      "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[1]/div[14]/div/div[2]/div/div/input")
        marrage.send_keys(m_status)
        marrage.send_keys(Keys.ENTER)
        sleep(1)
        passport_number = driver.find_element("xpath",
                                              "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[2]/div[2]/div/input")
        passport_number.send_keys(passport_num)
        sleep(1)

        idate = driver.find_element("xpath",
                                    "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[2]/div[3]/div/span[1]/input")
        driver.execute_script("window.scrollBy(0, 400)")
        driver.execute_script("arguments[0].removeAttribute('readonly')", idate)
        idate.send_keys(issue_date)
        sleep(1)

        vdate = driver.find_element("xpath",
                                    "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[2]/div[4]/div/div/span[1]/input")
        driver.execute_script("window.scrollBy(0, 400)")
        driver.execute_script("arguments[0].removeAttribute('readonly')", vdate)
        vdate.send_keys(valid_date)
        sleep(1)

        validator_c = driver.find_element("xpath",
                                          "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[2]/div[6]/input")
        validator_c.send_keys(issue_auth)

        address_state_b = driver.find_element("xpath",
                                              "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[3]/div[3]/div/div[2]/button").click()
        address_state = driver.find_element("xpath",
                                            "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[3]/div[3]/div/div[2]/div/div/input")
        address_state.send_keys(state)
        address_state.send_keys(Keys.ENTER)

        address_city_b = driver.find_element("xpath",
                                             "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[3]/div[4]/div/div[2]/button").click()
        address_city = driver.find_element("xpath",
                                           "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[3]/div[4]/div/div[2]/div/div/input")
        address_city.send_keys(city)
        address_city.send_keys(Keys.ENTER)

        address_input = driver.find_element("xpath",
                                            "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[3]/div[5]/input")
        address_input.send_keys(address)

        postalcode = driver.find_element("xpath",
                                         "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[3]/div[6]/input")
        postalcode.send_keys(postal_code)

        mail = driver.find_element("xpath",
                                   "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[4]/div[2]/div/input")
        mail.send_keys(email)

        phone = driver.find_element("xpath",
                                    "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[4]/div[3]/div/div[2]/div/input")
        phone.send_keys(mobile)

        entries_b = driver.find_element("xpath",
                                        "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[5]/div[2]/div/div[2]/button").click()
        entries = driver.find_element("xpath",
                                      "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[5]/div[2]/div/div[2]/div/div/input")
        entries.send_keys(entries_num)
        entries.send_keys(Keys.ENTER)

        s_duration = driver.find_element("xpath",
                                         "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[5]/div[3]/input")
        s_duration.send_keys(duration)

        travel_d = driver.find_element("xpath",
                                       "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[1]/div[6]/div[2]/div[5]/div[4]/div/span[1]/input")
        driver.execute_script("window.scrollBy(0, 400)")
        driver.execute_script("arguments[0].removeAttribute('readonly')", travel_d)
        travel_d.send_keys(travel_date)
        sleep(1)
        captcha = driver.find_element("xpath", '//*[@id="LoginCaptcha_CaptchaImage"]')
        captcha_image = captcha.screenshot_as_png
        with open('image.png', 'wb') as f:
            f.write(captcha_image)
        ANTICAPTCHA_KEY = 'f351f00037dfa7f5176700791bfac753'
        captcha_file = "image.png"
        result = ImageToTextTask.ImageToTextTask(anticaptcha_key=ANTICAPTCHA_KEY).captcha_handler(
            captcha_file=captcha_file)
        captcha_text = result['solution']['text']
        captcha_input = driver.find_element("xpath",
                                            "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div[8]/div[2]/div/div/div/input")
        captcha_input.send_keys(captcha_text)

        continuebtn = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[2]/div/form/div[2]/div/button")
        continuebtn.click()

    def formfill_rest():
        refer = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/p/b").get_attribute('innerHTML')
        print(refer)
        read_configs('form.txt')
        fm = "form.txt"
        with open(fm, 'r+') as f:
            text = f.read()
            text = re.sub(ref_num, refer, text)
            f.seek(0)
            f.write(text)
            f.truncate()

        accept_rules = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[2]/div[2]/div[2]/label/input")
        accept_rules.click()

        proceed_b1 = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/a[2]")
        proceed_b1.click()

        form_select1 = driver.find_element("xpath",
                                           "/html/body/div[1]/div[3]/div/div[2]/div/form/div[1]/div/div/ul/li[2]/div/a")
        form_select1.click()
        sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        sleep(2)
        proceed_b2 = driver.find_element("xpath", "/html/body/div[1]/div[3]/div/div[2]/div[1]/div[1]/a")
        proceed_b2.click()

        close_btn_loop = driver.find_element("xpath", "/html/body/div[2]/div/div/div/button")
        close_btn_loop.click()
        sleep(10)

    def check_slots():
        for x in itertools.count(start=1):
            driver.refresh()
            sleep(1)
            close_btn_loop = driver.find_element("xpath", "/html/body/div[2]/div/div/div/button")
            close_btn_loop.click()
            sleep(1)
            # openedstyle = driver.find_elements_by_css_selector('td.day.regular')
            # opened1 = openedstyle.find_elements_by_xpath("//*[contains(@innerHTML='25')]")
            # opened = openedstyle.get_attribute('innerHTML',"25")
            opened = EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td.day.regular"), "25")

            if opened:
                layout = [
                    [sg.Text('Attention! The Embassy Slots are opened.', justification="right", font=("iranyekan"))],
                    [sg.Submit('Alright! Lemme Take My Time', font=("iranyekan"))]]

                window = sg.Window('Attention!', layout, font='iranyekan', element_justification='c')
                while True:
                    mixer.init()
                    mixer.music.load('alarm.mp3')
                    mixer.music.play(loops=-1)
                    event, values = window.read()
                    if event == sg.WIN_CLOSED:
                        mixer.music.stop()
                        break
                    if event == 'Alright! Lemme Take My Time':
                        mixer.music.stop()
                        break
                window.close()
                sleep(20)
                break
            else:
                print('Element not found')
                sleep(300)

    def mode2():
        sleep(randint(2, 3))
        driver.get("https://www.ckgsir.com/bluestrip-widget")
        sleep(randint(45, 60))
        idcloudflare = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div/input[1]')
        codecloudflare = driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div/div/input[2]')
        # idcloudflare.get_attribute("type").replace('hidden','show')
        # codecloudflare.get_attribute("type").replace('hidden','show')
        try:
            result = solver.turnstile(
                sitekey='0x4AAAAAAAAjq6WYeRDKmebM',
                url='https://www.ckgsir.com/bluestrip-widget',
            )

        except Exception as e:
            sys.exit(e)

        else:
            print('result: ' + str(result))

        # response_cloudflare = result.split('&')
        #
        # captchaid = response_cloudflare[0].split('=')[1]
        #
        # captchacode = response_cloudflare[1].split('=')[1]
        #
        # print(captchaid)
        # print(captchacode)
        #
        # sleep(randint(2, 3))
        # idcloudflare.send_keys(captchaid)
        # codecloudflare.send_keys(captchacode)
        sleep(randint(2, 3))
        try:
            closebtn_widget = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                                                "body > div.mfp-wrap.mfp-close-btn-in.mfp-auto-cursor.my-mfp-slide-bottom.mfp-ready > div > div > div > button")))
            # closebtn_widget = driver.find_element_by_css_selector("body > div.mfp-wrap.mfp-close-btn-in.mfp-auto-cursor.my-mfp-slide-bottom.mfp-ready > div > div > div > button")
            closebtn_widget.click()
        # except NoSuchElementException:
        #   closebtn_widget2 = driver.find_element("xpath","/html/body/div[2]/div/div/div/button")
        #  closebtn_widget2.click()
        except:
            pass
        try:
            closebtn3 = driver.find_element("xpath", "/html/body/footer/div[4]/div/span/a")
            closebtn3.click()
        except:
            pass
        sleep(randint(1, 2))
        reference_widget = driver.find_element("xpath",
                                               "/html/body/div[1]/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div[2]/input")
        reference_widget.send_keys(ref_num)

        bdate_widget = driver.find_element("xpath",
                                           "/html/body/div[1]/div[2]/div/div[2]/div/form/div[1]/div/div[3]/div[2]/div/span/input")
        driver.execute_script("window.scrollBy(0, 400)")
        driver.execute_script("arguments[0].removeAttribute('readonly')", bdate_widget)
        bdate_widget.send_keys(birth_date)

        passport_widget = driver.find_element("xpath",
                                              "/html/body/div[1]/div[2]/div/div[2]/div/form/div[1]/div/div[4]/div[2]/input")
        passport_widget.send_keys(passport_num)
        driver.find_element("xpath",
                            "/html/body/div[1]/div[2]/div/div[2]/div/form/div[1]/div/div[6]/div[2]/input").click()
        sleep(1)
        captcha_widget = driver.find_element("xpath", '//*[@id="LoginCaptcha_CaptchaImage"]')
        captcha_image_widget = captcha_widget.screenshot_as_png
        with open('image.png', 'wb') as f:
            f.write(captcha_image_widget)
        ANTICAPTCHA_KEY = 'f351f00037dfa7f5176700791bfac753'
        captcha_file_widget = "image.png"
        result_widget = ImageToTextTask.ImageToTextTask(anticaptcha_key=ANTICAPTCHA_KEY).captcha_handler(
            captcha_file=captcha_file_widget)
        captcha_text_widget = result_widget['solution']['text']
        captcha_input_widget = driver.find_element("xpath",
                                                   "/html/body/div[1]/div[2]/div/div[2]/div/form/div[1]/div/div[6]/div[2]/input")
        captcha_input_widget.send_keys(captcha_text_widget)

        continuebtn_widget = driver.find_element("xpath",
                                                 "/html/body/div[1]/div[2]/div/div[2]/div/form/div[2]/div/button")
        continuebtn_widget.click()

        def check_slots_widget():
            for y in itertools.count(start=1):
                driver.refresh()
                sleep(1)
                close_btn_loop = driver.find_element("xpath", "/html/body/div[2]/div/div/div/button")
                close_btn_loop.click()
                sleep(1)
                openedstyle = driver.find_elements_by_css_selector('td.day.regular')
                opened = openedstyle.find_elements_by_xpath("//*[contains(@innerHTML='range(22,31)')]")
                # opened = openedstyle.get_attribute('innerHTML',"25")
                # opened = EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td.day.regular"), "25")
                if opened:
                    layout = [
                        [sg.Text('Attention! The Embassy Slots are opened.', justification="right",
                                 font=("iranyekan"))],
                        [sg.Submit('Alright! Lemme Take My Time', font=("iranyekan"))]]

                    window = sg.Window('Attention!', layout, font='iranyekan', element_justification='c')
                    while True:
                        mixer.init()
                        mixer.music.load('alarm.mp3')
                        mixer.music.play(loops=-1)
                        event, values = window.read()
                        if event == sg.WIN_CLOSED:
                            mixer.music.stop()
                            sys.exit()
                        if event == 'Alright! Lemme Take My Time':
                            mixer.music.stop()
                            sys.exit()
                    window.close()
                    sleep(20)
                    break
                else:
                    print('Element not found')
                    sleep(300)

        check_slots_widget()

    def mode1_detect():
        try:
            form_fill()
            formfill_rest()
            check_slots()
        except NoSuchElementException:
            passport_error()
            form_fill()
            formfill_rest()
            check_slots()

    def mode3_detect():
        try:
            form_fill()
        except NoSuchElementException:
            passport_error()
            form_fill()

    layout = [[sg.Text('Welcome to CKGS Appointment Robot', size=(40, 1), justification='center')],
              [sg.Text(
                  'This app only automate the process of Appointment for saving time and its not illegal in any case, '
                  'This bot will need to access your IP Address & Machine fingerprint (hardware ID) just like any other commercial application for licencing'
                  ',if you do not want to proceed you can click cancel button and close the app, continue using app if you are agree to provide such information,'
                  ' your form submission details will be saved in installed folder as a text file named form.txt please do not edit this file since the app use it as regex formula'
                  ', any attempt to break copyright of the app or piracy will be an subject of violating the copyright law',
                  size=(61, 11), justification="left justified", font="courier 13", text_color='gray')],
              [sg.Text('Your provided information WILL NOT BE SAVED anywhere other than your system', size=(45, 2),
                       justification="center", text_color='red', font="arial 14 bold")],
              [sg.Text('Make sure all the information you provide are correct and precisely matches the examples',
                       size=(40, 2), justification="center", font="arial 14 bold")],
              [sg.Text('DO NOT intervene in the Chrome Process in any case During Progress', size=(60, 1),
                       justification="center", font="arial 14 bold", text_color='red')],
              [sg.Submit('Agree and Continue', font="arial"), sg.Cancel('Cancel', font="arial")],
              [sg.Text('©2021 Parsa Vandy All Rights Reserved', justification='center', font='arial 11')],
              [sg.Text('Happy Traveling', justification='center', font='arial 11')]],
    window = sg.Window("Copyright and privacy Note", layout, font="arial", element_justification="c")
    event, value = window.read()
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        driver.quit()
        sys.exit()
    window.close()

    layout = [[sg.Text('Please select the Mode', size=(30, 1), justification='center', font='arial 18')],
              [sg.Combo(['Mode 1', 'Mode 2', 'Mode 3', 'Mode 4'], key="-mode1b-", size=(35, 1),
                        default_value='Mode 1')],
              [sg.Text('Mode 1: ', font='arial 11 bold', text_color='red', size=(7, 2)),
               sg.Text('Fills up the Form by Your Info then Goes to Calender and Checks the Slots', size=(35, 2),
                       justification="center", font="arial 11 bold")],
              [sg.Text('Mode 2: ', font='arial 11 bold', text_color='red', size=(7, 2)),
               sg.Text('It will go to Calendar by Your Reference Number and Checks the Slots', size=(35, 2),
                       justification="center", font="arial 11 bold")],
              [sg.Text('Mode 3: ', font='arial 11 bold', text_color='red', size=(7, 2)),
               sg.Text('Only Fills up the Form and Leave the Rest to You', size=(35, 2), justification="center",
                       font="arial 11 bold")],
              [sg.Text('Mode 4: ', font='arial 11 bold', text_color='red', size=(7, 2)),
               sg.Text('Create Account & Login and book the Appointment automatically (Full Process) ', size=(35, 2),
                       justification="center", font="arial 11 bold")],
              [sg.Submit('Submit', font='arial')]]
    window = sg.Window('Mode', layout, font="arial", element_justification='center')
    event, values = window.read()
    window.disappear()
    window.close()

    mode_button = values['-mode1b-']

    if mode_button == 'Mode 1':
        # mode1_form_type()
        mode1_submit()
        mode1_detect()
    if mode_button == 'Mode 2':
        mode2_submit()
        mode2()
    if mode_button == 'Mode 3':
        mode3_detect()

  # Otherwise, we need to determine why the current license is not valid,
  # because in our case it may be invalid because another machine has
  # already been activated, or it may be invalid because it doesn't
  # have any activated machines associated with it yet and in that case
  # we'll need to activate one.
  if "errors" in validation:
      errs = validation["errors"]
      layout = [[sg.Text('Please insert License and Activation code', justification=("left"), font='iranyekan')],
                [sg.Text('License Code:', size=(15, 1), justification=("left"), font='iranyekan'),
                 sg.InputText(key='-INPUT-', size=(40, 1))],
                [sg.Text('Activation Code:', size=(15, 1), justification=("left"), font='iranyekan'),
                 sg.InputText(key='-INPUT2-', size=(40, 1))],
                [sg.Submit('Submit', font='iranyekan'), sg.Cancel('Cancel', font='iranyekan')]]
      window = sg.Window('Invalid License', layout, font='iranyekan', element_justification='l')

      while True:
          event, values = window.read()
          if event == 'Cancel' or event == sg.WIN_CLOSED:
              sys.exit()  # exit button clicked
          inp = window['-INPUT-'].get().strip()
          if event == 'Submit' and inp == '':
              sg.popup(f"License Code required")
          inp2 = window['-INPUT2-'].get().strip()
          if event == 'Submit' and inp2 == '':
              sg.popup(f"Activation Code required")
          else:
              license_input = values['-INPUT-']
              read_configs('form.txt')
              lic = "form.txt"
              with open(lic, 'r+') as f:
                  text = f.read()
                  text = re.sub(license_code, license_input, text)
                  f.seek(0)
                  f.write(text)
                  f.truncate()
              activation_input = values['-INPUT2-']
              read_configs('form.txt')
              lic = "form.txt"
              with open(lic, 'r+') as f:
                  text = f.read()
                  text = re.sub(activation_code, activation_input, text)
                  f.seek(0)
                  f.write(text)
                  f.truncate()
              sg.popup(f"Please re-open the application")
              sleep(3)
              break
      window.close()
      return False, "license validation failed: {}".format(
          map(lambda e: "{} - {}".format(e["title"], e["detail"]).lower(), errs)
      )
  validation_code = validation["meta"]["code"]
  activation_is_required = validation_code == 'FINGERPRINT_SCOPE_MISMATCH' or \
                           validation_code == 'NO_MACHINES' or \
                           validation_code == 'NO_MACHINE'

  if not activation_is_required:
    sg.Popup('Your Machine need to be activated')
    layout = [[sg.Text('Please insert License and Activation code', justification=("left"), font='iranyekan')],
              [sg.Text('License Code:', size=(15, 1), justification=("left"), font='iranyekan'),
               sg.InputText(key='-INPUT-', size=(40, 1))],
              [sg.Text('Activation Code:', size=(15, 1), justification=("left"), font='iranyekan'),
               sg.InputText(key='-INPUT2-', size=(40, 1))],
              [sg.Submit('Submit', font='iranyekan'), sg.Cancel('Cancel', font='iranyekan')]]
    window = sg.Window('Your License has no Machine linked', layout, font='iranyekan', element_justification='l')

    while True:
        event, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            sys.exit()  # exit button clicked
        inp = window['-INPUT-'].get().strip()
        if event == 'Submit' and inp == '':
            sg.popup(f"License Code required")
        inp2 = window['-INPUT2-'].get().strip()
        if event == 'Submit' and inp2 == '':
            sg.popup(f"Activation Code required")
        else:
            license_input = values['-INPUT-']
            read_configs('form.txt')
            lic = "form.txt"
            with open(lic, 'r+') as f:
                text = f.read()
                text = re.sub(license_code, license_input, text)
                f.seek(0)
                f.write(text)
                f.truncate()
            activation_input = values['-INPUT2-']
            read_configs('form.txt')
            lic = "form.txt"
            with open(lic, 'r+') as f:
                text = f.read()
                text = re.sub(activation_code, activation_input, text)
                f.seek(0)
                f.write(text)
                f.truncate()
            sg.popup(f"Please re-open the application")
            sleep(3)
            break
    window.close()
    return False, "license {}".format(validation["meta"]["detail"])

  # If we've gotten this far, then our license has not been activated yet,
  # so we should go ahead and activate the current machine.
  activation = requests.post(
    "https://api.keygen.sh/v1/accounts/d1f000c1-8f6a-4b57-ad04-f630d15740f3/machines",
    headers={
      "Authorization": "Bearer "+ activation_code,
      "Content-Type": "application/vnd.api+json",
      "Accept": "application/vnd.api+json"
    },
    data=json.dumps({
      "data": {
        "type": "machines",
        "attributes": {
          "fingerprint": machine_fingerprint
        },
        "relationships": {
          "license": {
            "data": { "type": "licenses", "id": validation["data"]["id"] }
          }
        }
      }
    })
  ).json()

  # If we get back an error, our activation failed.
  if "errors" in activation:
    errs = activation["errors"]
    sg.Popup('Machine Activation Failed')
    layout = [[sg.Text('Please insert License and Activation code', justification=("left"), font='iranyekan')],
              [sg.Text('License Code:', size=(15, 1), justification=("left"), font='iranyekan'),
               sg.InputText(key='-INPUT-', size=(40, 1))],
              [sg.Text('Activation Code:', size=(15, 1), justification=("left"), font='iranyekan'),
               sg.InputText(key='-INPUT2-', size=(40, 1))],
              [sg.Submit('Submit', font='iranyekan'), sg.Cancel('Cancel', font='iranyekan')]]
    window = sg.Window('Machine Activation', layout, font='iranyekan', element_justification='l')

    while True:
        event, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            sys.exit()  # exit button clicked
        inp = window['-INPUT-'].get().strip()
        if event == 'Submit' and inp == '':
            sg.popup(f"License Code required")
        inp2 = window['-INPUT2-'].get().strip()
        if event == 'Submit' and inp2 == '':
            sg.popup(f"Activation Code required")
        else:
            license_input = values['-INPUT-']
            read_configs('form.txt')
            lic = "form.txt"
            with open(lic, 'r+') as f:
                text = f.read()
                text = re.sub(license_code, license_input, text)
                f.seek(0)
                f.write(text)
                f.truncate()
            activation_input = values['-INPUT2-']
            read_configs('form.txt')
            lic = "form.txt"
            with open(lic, 'r+') as f:
                text = f.read()
                text = re.sub(activation_code, activation_input, text)
                f.seek(0)
                f.write(text)
                f.truncate()
            sg.popup(f"Please re-open the application")
            sleep(3)
            break
    window.close()
  return False, "license activation failed: {}".format(
      ','.join(map(lambda e: "{} - {}".format(e["title"], e["detail"]).lower(), errs))
  )
  return True, sg.popup("Your License has been Activated on this Machine")
# Run from the command line:
#   python main.py some_license_key
status, msg = activate_license(sys.argv[0])

print(status, msg)
