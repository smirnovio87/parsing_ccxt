
import ccxt
import json

# "binance", "bybit", "coinex", "kraken", "bitget", "ascendex", "bequant", "bigone","binanceusdm", "bingx", "bitbns", "bitfinex"

#name_exchanges = ["binance", "bybit", "coinex", "kraken", "bitget", "ascendex", "bequant", "bigone","binanceusdm", "bingx", "bitbns", "bitfinex"]
name_exchanges = ccxt.exchanges
name_exchanges = ['bitbank',"binance", "bybit", "coinex"]

symbol = 'BTC/USDT'

def price_result(name_exchanges):
    exchanges = {}
    for id in name_exchanges:
        #getattr возврашает значение атрибута по имени этого атрибута. 
        #Т.Е. Вернет обект ccxt с атрибутом binance - ccxt.binance
        exchange = getattr(ccxt, id)
        #Данной строкой записываем в словарь exchanges id {"binance": ccxt.binance} ну и так по всем name_exchanges
        exchanges[id] = exchange()
    print("Результат поверки бирж ", exchanges)

    data = {}

    for id, exchange in exchanges.items():
        try: 
            ticker = exchange.fetch_ticker(symbol)
            data[id] = ticker['last']
        except Exception as err:
        #Записываем в словарь к ключу [id]-название биржы = значение exchange.fetch_ticker(symbol) - "last"
            print(f"Unexpected {err=}, {type(err)=}")    
            data[id] = "НЕ доступна"
        
    return data

result = price_result(name_exchanges)
print("Результат получения ", result)

out_result={}
for key, value in result.items():
    if isinstance(value, float):
        out_result[key]=value

# max(out_result, key=out_result.get)      
max_value = max(out_result, key=out_result.get)
min_value = min(out_result, key=out_result.get )

print("Максимальное значение:", max_value, out_result[max_value])
print("Минимальное значение:", min_value, out_result[min_value])

print("Конечный результат ", out_result)
# print(sorted(out_result, reverse=True))


# data_json=price_result(name_exchanges)
# #Записываем в Json файл
# with open('btc_usdt_courses_12.json', 'w', encoding="utf-8") as json_file:

#     json.dump(data_json, json_file, indent=4, ensure_ascii=False)
# print(data_json)