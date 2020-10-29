invoce = '''
0....6........................40..........52....55..........
1909 Pimoroni PiBrella            $17.50      3      $52.50
1489 6mm Tactile Switch x 20      $4.95       2      $9.90
1510 Panavise Jr . - PV-201       $28.00      1      $28.00
1601 PiTFT Mini Kit 320x240       $34.95      1      $34.95
'''
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNITY_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)
line_items = invoce.split('\n')[2:]
for item in line_items:
    print(item[UNITY_PRICE], item[DESCRIPTION])  