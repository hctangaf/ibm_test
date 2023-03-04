def look_size(n, stock, num_of_request, request):
    if n<num_of_request:
        return False
    else:
        for requests in request:
            if requests == 'L':
                for stocks in stock:
                    if requests in stocks or requests == stocks[-1]:
                        stock.remove(stocks)
                    else:
                        return False
            elif requests == 'M':
                for stocks in stock:
                    if requests in stocks or stocks == 'L' or stocks[-1] == 'L':
                        stock.remove(stocks)
                    else:
                        return False
            elif requests == 'S':
                for stocks in stock:
                    if requests in stocks or stocks in ['M', 'L'] or stocks[-1] == 'L':
                        stock.remove(stocks)
                    else:
                        return False
            elif requests[-1] == 'S' and requests != 'S':
                for stocks in stock:
                    if requests in stocks or (stocks[-1] == 'S' and len(stocks)<len(requests)):
                        stock.remove(stocks)
                    else:
                        return False
            else:
                return False
    return True

def main():
    if __name__ == 'main':
        x = look_size(5, ['XL', 'XXXXXXXXXL', 'XXS', 'M', 'XXS'], 4, ['L', 'M', 'L', 'XXS'])
        if x is True:
            print('Yes')
        else:
            print('No')
