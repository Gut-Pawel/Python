import requests
import json
import csv

listPath = ("/home/pi/work/python/data/crypto_list.csv")
getRaportInCurrency = 'EUR'

def getCurrencyCryptoPrice(cryptoCurrency, currency):
  url = ("https://min-api.cryptocompare.com/data/price")
  header = {'Authorization': 'Apikey 2c978755d04f984134a992d335e09344879898f50e1cd2762335e9ec1b7b205b'}
  params = {'fsym':f'{cryptoCurrency}', 'tsyms':f'{currency}'}
  response = requests.get(url, headers=header, params=params)
  return response

file = open(listPath, "r")
csvReader = csv.reader(file,delimiter=',', quotechar='"')
rowCount = 0
for row in csvReader:
  # Init vars
  cryptoCurrencyName = row[0]
  cryptoCurrencyCount = row[1]
  currencyName = row[2]
  currencyCount = row[3]
  # Send api request
  response = getCurrencyCryptoPrice(cryptoCurrency=cryptoCurrencyName,currency=currencyName).json()
  # Calculate profit
  actualPriceCrypto = response[currencyName]
  calculateActualProfit = (float(actualPriceCrypto) * float(cryptoCurrencyCount)) - float(currencyCount)
  if currencyName == getRaportInCurrency:
    print(cryptoCurrencyName + ": Profit = " + str(calculateActualProfit) + " " +str(currencyName))
  else:
    response2 = getCurrencyCryptoPrice(cryptoCurrency=currencyName,currency=getRaportInCurrency).json()
    calculateActualProfit2 = float(calculateActualProfit) * float(response2[getRaportInCurrency])
    # print(cryptoCurrencyName + ": TEST = " + str(calculateActualProfit) + " " +str(currencyName))
    print(cryptoCurrencyName + ": Profit = " + str(calculateActualProfit2) + " " + str(getRaportInCurrency))
file.close()