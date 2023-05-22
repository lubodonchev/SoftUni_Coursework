target = int(input())

total, counter = 0, 1
total_cs, total_cc, cs_count, cc_count = 0, 0, 0, 0

while target > total:
    price = input()

    if price == 'End':
        print('Failed to collect required money for charity.')
        break

    if counter % 2 == 0:
        if int(price) < 10:
            print('Error in transaction!')
        else:
            print('Product sold!')
            total_cc += int(price)
            cc_count += 1
            total += int(price)
    else:
        if int(price) > 100:
            print('Error in transaction!')
        else:
            print('Product sold!')
            total_cs += int(price)
            cs_count += 1
            total += int(price)

    counter += 1

else:
    print(f'Average CS: {total_cs / cs_count:.2f}')
    print(f'Average CC: {total_cc / cc_count:.2f}')
