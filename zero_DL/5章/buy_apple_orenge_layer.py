from layer_naive import *

apple = 100
orange = 150
apple_num = 2
orange_num = 3
tax = 1.1

#layer
mul_apple_layer = MulLayer()
mul_orange_layer = MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

#forword
apple_price =mul_apple_layer.forword(apple,apple_num)
orange_price = mul_orange_layer.forword(orange,orange_num)
apple_orange_price = add_apple_orange_layer.forword(apple_price,orange_price)
price = mul_tax_layer.forword(apple_orange_price,tax)

print(price)

#backword
dprice = 1
dapple_orange_price,dtax = mul_tax_layer.backword(dprice)
dapple_price,dorange_price = add_apple_orange_layer.backword(dapple_orange_price)
dapple,dapple_num = mul_apple_layer.backword(dapple_price)
dorange,dorange_num = mul_orange_layer.backword(dorange_price)

print(dapple_num,dapple,dorange,dorange_num,dtax)
