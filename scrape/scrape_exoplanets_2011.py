import requests
from bs4 import BeautifulSoup

def scrape_exoplanets(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        table = soup.find('table', {'class': 'wikitable'})
        
        if table:
            rows = table.find_all('tr')
            
            for row in rows[1:]:  
                columns = row.find_all(['th', 'td'])
                planet_name = columns[0].text.strip()
                discovery_method = columns[1].text.strip()
                discovery_year = columns[2].text.strip()
                radius = columns[3].text.strip()
                period_days = columns[4].text.strip()
                
                print(f"Nama Eksoplanet: {planet_name}, Metode Penemuan: {discovery_method}, Tahun Penemuan: {discovery_year}, Radius Planet: {radius}, Jangka Hari: {period_days}")
        else:
            print("Tabel tidak ditemukan.")
    else:
        print(f"Gagal mengambil halaman web. Kode status: {response.status_code}")
        print(f"URL: {url}")

url_to_scrape = 'https://en.wikipedia.org/wiki/List_of_exoplanets_discovered_in_2011'
scrape_exoplanets(url_to_scrape)
