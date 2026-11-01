#Item 1
price = 20
discountedprice = price * 0.10
subtotal = price - discountedprice
gst = subtotal * 0.09
finalprice = subtotal + gst 
print(finalprice)