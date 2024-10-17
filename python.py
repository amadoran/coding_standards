class Items:

    def __init__(self, name, price, qty):
        price_numeric_check = isinstance(price, (float, int))
        qty_numeric_check = isinstance(qty, int)
        print(price_numeric_check, qty_numeric_check)
        if not price_numeric_check or not qty_numeric_check:
            raise TypeError('Price or qty datatype missmatch')

        self.name = name

        self.price = price

        self.qty = qty

        self.category = "general"

        self.env_fee = 0



    def get_total(self):
        if self.category == 'electronics':
            self.env_fee = 5

        return (self.price + self.env_fee) * self.qty

    def get_tmost_prices(self):

        return self.price * self.qty * 0.6



#class to shop

class ShoppingCart:

    def __init__(self):

        self.items = []

        self.tax_rate = 0.08

        self.member_discount = 0.05

        self.big_spender_discount = 10

        self.coupon_discount = 0.15

        self.currency = "USD"



    def add_item(self, item):

#discount added here

        self.items.append(item)



    def calculate_subtotal(self):

#todo: fix this in the future i guess

        subtotal = 0

        for item in self.items:

            subtotal += item.get_total()

        return subtotal



    def apply_discounts(self, subtotal, is_member):

        if is_member == "yes":

            subtotal = subtotal - (subtotal * self.member_discount)

        if subtotal > 100:

            subtotal = subtotal - self.big_spender_discount

        return subtotal



    def calculate_total(self, is_member, has_coupon):

#why i need this? @user

        subtotal = self.calculate_subtotal()

        subtotal = self.apply_discounts(subtotal, is_member)

        total = subtotal + (subtotal * self.tax_rate)

        if has_coupon == "YES":

            total = total - (total * self.coupon_discount)

        return total



def main():

    cart = ShoppingCart()

    item1 = Items("Apple", 1.5, 10)

    item2 = Items("Banana", 0.5, 5)

    item3 = Items("Laptop", "1000", 1)

    item3.category = "electronics"

    cart.add_item(item1)

    cart.add_item(item2)

    cart.add_item(item3)

    is_member = True

    has_coupon = "YES"



    total = cart.calculate_total(is_member, has_coupon)



    if total < 0:

        print("Error in calculation!")

    else:

        print("The total price is: $" + str(int(total)))



if __name__ == "__main__":

    main()
