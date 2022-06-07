from requests_html import HTMLSession


class Weather():
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70'}
        self.base_url = f'https://www.google.com/search?q=pogoda+'

    def get_weather(self, city):
        r = self.session.get(self.base_url + str(city), headers=self.headers)
        scraped_weather = [
            city,
            r.html.find('span#wob_tm', first=True).text,
            r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text,
            r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text,

        ]
        return scraped_weather

weather = Weather()
city1 = weather.get_weather('Warszawa')
city2 = weather.get_weather('Kraków')
print(f'{city1} \n{city2}')

