def convert_str(value):
    price_str = f'R$ {value:.2f}'.replace('.', ',')
    if len(price_str) > 9:
        x = price_str[:-6] + "." + price_str[-6:]
        return x
    else:
        return price_str
