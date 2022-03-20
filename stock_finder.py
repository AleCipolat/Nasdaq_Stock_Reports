from nasdaq.nasdaq_finder import NasdaqFinder
import pathlib

if __name__ == "__main__":    
    logo = open("logo.txt", "r")
    print(logo.read())
    print("Welcome to Stock report Generator\n")
    print("by Alejandro Cipolat 2022\n")
    finder=NasdaqFinder("credentials.txt")
    ticker=str(input("Please write the ticker: "))
    path=pathlib.Path(__file__).parent.resolve()
    print("\n")
    print("Searching "+ticker+"......")
    filename=finder.create_stock_report(ticker,path)
    print("[SUCCESS] Report Created="+filename)
    
 


