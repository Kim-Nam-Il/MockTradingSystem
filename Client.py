import socket
import json

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 8888)
    while True:
        symbol = input("Enter a stock symbol (or q to quit): ")
        if symbol == 'q':
            break
        client_socket.sendto(symbol.encode(), server_address)
        data, server_addr = client_socket.recvfrom(1024)
        response = json.loads(data.decode())
        if response["price"] is None:
            print(f"Invalid stock symbol: {response['symbol']}")
        else:
            print(f"Current price of {response['symbol']}: {response['price']} USD")

if __name__ == '__main__':
    main()
