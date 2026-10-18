#7.3 Problem 3: Product catalog with dictionary

products= {
	"Pokeball" : 200,
	"Superball" : 600,
	"Ultraball" : 800
}
print (products)
while True:
    try:
        product_name = input("Type a product name: ").strip()
        quantity = int (input ("Type the quantity: "))
        if product_name in products:
            total_price = products[product_name]*quantity
            print (f"Unit price: {products[product_name]}")
            print (f"Quantity: {quantity}")
            print (f"Total: {total_price}")
        else:
            print ("Error: product not found")
    except ValueError:
        print ("Please type a valid value")
    



