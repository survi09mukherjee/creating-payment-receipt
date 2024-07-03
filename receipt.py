# Create a product and price for 3 items

p1_name, p1_price="Apples",10.90
p2_name, p2_price="Milk",5.50
p3_name, p3_price="Eggs",7.90

# Create a Company ame and information
company_name= "Survi's World"
company_address="B-Zone"
company_city="Durgapur"

# Declare ending message
Message="Thank you for shopping... Visit again!!   :)"

# Create a top border
print("\t\tRECEIPT")
print("*"*50)

# Print Company information first using format
print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_city))

# Print a line between sections
print("*"*50)

# Print out headers for section of items
print("\t Product Name \t Product Price")
# Create a print statement for each product
print("\t{}\t\t{}".format(p1_name.title(),p1_price))
print("\t{}\t\t{}".format(p2_name.title(),p2_price))
print("\t{}\t\t{}".format(p3_name.title(),p3_price))

# Print a line between sections
print("="*50)
# Print out headers for section for total
print("\t\t\t Total")

# Calculate Total price and print it
total=p1_price+p2_price+p3_price
print("\t\t\t{}".format(total))
# Print a leine between sections
print("="*50)

#Output thank you message
print("\n\n{}\n".format(Message))

# Create a bottom border
print("*"*50)