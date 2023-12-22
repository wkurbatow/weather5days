import requests
from bs4 import BeautifulSoup
import pprint


API_KEY = 'a0eeb99afacf0df6d2c11a0765325031'

def get_data(place, forecast_days):
    url = f'https://api.openweathermap.org/geo/1.0/direct?q={place}&limit=5&appid={API_KEY}'
    content_country = requests.get(url).json()
    lat = content_country[0]["lat"]
    lon = content_country[0]['lon']
    country = content_country[0]['country']
    url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
    content_country = requests.get(url).json()["list"]
    content_country = content_country[0:forecast_days*8]
    data_line = [data["dt_txt"] for data in content_country]
    
    return data_line, content_country, country
    # return dates, temperatures

# if __name__ == "__main__":
#     d, t , c = get_data('Москва', 1,1)
#     print(c)

def parse_img():
    url_icon = 'https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2'
    html_cont = requests.get(url_icon)
    soup = BeautifulSoup(html_cont.text,"html.parser")
    tanles_soup = soup.find_all("table" , class_="table table-bordered")
    cod_table = []
    src_table = []
    for table in tanles_soup[1:]:
        all_td_in_one_table = table.find_all("td")
        # tr_table.append(table.find_all("td"))
        for td in all_td_in_one_table[::4]:
            
            cod_table.append(td.text.strip())
        for td in all_td_in_one_table[3::4]:
            
            src_table.append(td.img['src'])
    res = dict(zip(cod_table, src_table))
   
    return res 





if __name__ == "__main__":
    x = parse_img(['804', '803', '802', '802', '803'])
    # pprint.PrettyPrinter(width=40).pprint(x)
    # print(type(x['621']))
    print(x)

   
    