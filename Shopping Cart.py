class ShoppingCart:
    def __init__(keeper, product_name, unit_price, gst, qty):
        keeper.product_name = product_name
        keeper.unit_price = unit_price
        keeper.gst = gst
        keeper.qty = qty
    def get_product_name(keeper):
        return keeper.product_name
    def get_unit_price(keeper):
        return keeper.unit_price
    def get_gst(keeper):
        return keeper.gst
    def get_qty(keeper):
        return keeper.qty

def main():
    GST_DISCOUNT_RATE = 0.05

    products = [
        ShoppingCart("Leather wallet", 1100, 18, 1),
        ShoppingCart("Umbrella", 900, 12, 4),
        ShoppingCart("Cigarette", 200, 28, 3),
        ShoppingCart("Honey", 100, 0, 2)
    ]

    print(f"{'Products':<20} {'Unit Price in Rs':<20} {'GST in %':<10} {'Quantity':<8}")
    for item in products:
        print(f"{item.get_product_name():<20} {item.get_unit_price():<20} {item.get_gst():<10} {item.get_qty():<8}")

    maximum_gst = 0
    max_gst_product = ""

    for item in products:
        gst = item.get_gst()
        price = item.get_unit_price()
        calculate_gst = (gst * price) / 100

        if calculate_gst > maximum_gst:
            maximum_gst = calculate_gst
            max_gst_product = item.get_product_name()

    print("1.Product with maximum GST amount:", max_gst_product)

    total_amount = 0

    for item in products:
        unit_price = item.get_unit_price()
        quantity = item.get_qty()
        discount = 0

        if unit_price >= 500:
            discount = (unit_price * GST_DISCOUNT_RATE)

        gst_amount = (unit_price * item.get_gst()) / 100
        total_amount += ((unit_price - discount + gst_amount) * quantity)

    print("2.Total amount to be paid:", total_amount)


if __name__ == "__main__":
    main()
