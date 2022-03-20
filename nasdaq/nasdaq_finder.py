import nasdaqdatalink

class NasdaqFinder:

  def __init__(self, api_key):
    nasdaqdatalink.read_key(api_key)

  def __get_stock_data(self,ticker):
    return nasdaqdatalink.get_table('SHARADAR/SEP', ticker=ticker)

  def create_stock_report(self, ticker,path):
    self.file_name=f"{path}\\{ticker}.xlsx"
    self.data= self.__get_stock_data(ticker)
    self.data.to_excel(self.file_name)
    return self.file_name
    
