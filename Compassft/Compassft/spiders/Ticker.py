import os
import scrapy
import pandas as pd
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup as bs

class TickerSpider(scrapy.Spider):
    name:str = "Ticker"
    allowed_domains:list = ["www.compassft.com"]
    
    def start_requests(self):
        url:str = "https://www.compassft.com/indices"
        yield SplashRequest(url=url, callback=self.parse)
    
    
    def parse(self, response):
        soup = bs(response.text, 'html.parser')
        tables = soup.find_all('table')
        table =  soup.find('table', class_='table sortable PctYearToDate')
        if table == None:
            # In case of airflow deployment, set task to failed at this point
            return None
        # Find all the th (table header) elements within the table's thead
        header_cells = table.find('thead').find_all('th')
        # Extract column names
        column_names = [cell.text.strip().replace('\n',' ') for cell in header_cells]
        df : pd.DataFrame = pd.DataFrame(columns=column_names)
        for row in table.tbody.find_all('tr'):    
            # Find all data for each column
            columns = row.find_all('td')
            if(columns != []):
                row_data = {}
                for col, data in zip(column_names,columns):
                    row_data[col] = data['data-sort-value']
                df = pd.concat([df, pd.DataFrame([row_data])], ignore_index=True)
            if len(df) > 9:
                break
        # 
        df = df[['Ticker','Currency','Last Value','As of']]
        # Translate names 
        df.columns = ['Ticker','Moeda','Valor','Data']
        df['Data'] = pd.to_datetime(df['Data']).dt.strftime("%Y/%m/%d")
        # In case of deployment direct the file saved to prefered cloud storage (for example  in AWS):
        if not os.path.exists(os.path.join(os.getcwd(), '..', '..','..','data/output/')):
            os.makedirs(os.path.join(os.getcwd(), '..', '..','..','data/output/'))
        df.to_csv(os.path.join(os.getcwd(), '..', '..','..','data/output/data.csv'), sep = ';', index=False)
        # In case of airflow deployment, set task to sucess at this point 
            

