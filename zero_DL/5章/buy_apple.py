from layer_naive import MulLayer

apple = 100
apple_num = 2
tax = 1.1

#MulLayer
mul_apple_layer = MulLayer()
mul_tax_layer = MulLayer()

#forword
apple_price = mul_apple_layer.forword(apple,apple_num)
price = mul_tax_layer.forword(apple_price,tax)

print(price)

#backword
dprice = 1
dapple_price,dtax = mul_tax_layer.backword(dprice)
dapple,dapple_num = mul_apple_layer.backword(dapple_price)

print(dapple,dapple_num,dtax)
