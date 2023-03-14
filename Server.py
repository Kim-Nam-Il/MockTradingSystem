import socket
import json
import random

class Stock:
    def __init__(self, symbol, name, price):
        self.symbol = symbol
        self.name = name
        self.price = price

class TradingSystem:
    def __init__(self):
        self.stocks = [
            Stock("AAPL", "Apple Inc.", 124.85),
            Stock("GOOGL", "Alphabet Inc.", 2089.50),
            Stock("MSFT", "Microsoft Corporation", 232.38),
            Stock("AMZN", "Amazon.com, Inc.", 3074.96),
        ]
    
    def get_stock_price(self, symbol):
        stock = next((x for x in self.stocks if x.symbol == symbol), None)
        if stock is None:
            return None
        return round(stock.price * (1 + random.uniform(-0.1, 0.1)), 2)

def main():
    system = TradingSystem()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 8888))
    print("Server started...")
    while True:
        data, addr = server_socket.recvfrom(1024)
        symbol = data.decode().strip()
        price = system.get_stock_price(symbol)
        response = {
            "symbol": symbol,
            "price": price,
        }
        server_socket.sendto(json.dumps(response).encode(), addr)

if __name__ == '__main__':
    main()
