# CKGS appointment scheduling

This bot was vastly used from 2019 to 2022 as a [CKGS](https://www.ckgsir.com) appointment scheduling, form filling, and slot check alarm for saving time and being online at the time of the event.
after removing the OTP option (for lack of maintenance) in 2022 I had lots of requests to complete the process by scheduling appointments fully automatically but I didn't have time.


This is an unfinished project due to a change in the Italian visa application processing partner in July 2023 and I am releasing it for educational purposes

it will bypass Cloudflare and solve any captcha ahead. 

## Installation

install and upgrade pip.

```bash
python -m pip3 install --upgrade pip
```

install requirements.

```bash
pip3 install -r requirements.txt
```

Upgrade [Chromedriver](https://chromedriver.chromium.org/downloads)

## Usage

```bash
python ckgs.py
```
or
```bash
python3 ckgs.py
```
#### Do not edit or replace the files below as they are being read in regex format by the bot
* #### form.txt
* #### license.txt

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
