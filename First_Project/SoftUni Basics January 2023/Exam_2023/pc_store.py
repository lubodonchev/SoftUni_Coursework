dollar_price_processor = float(input())
dollar_price_video = float(input())
dollar_price_ram = float(input())
quantity_ram = int(input())
discount_percent = float(input())

total = 1.57 * ((dollar_price_processor + dollar_price_video) *
                (1 - discount_percent) + quantity_ram * dollar_price_ram)

print(f'Money needed - {total:.2f} leva.')
