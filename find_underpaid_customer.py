def underpaid_customer():
    """go through every line in the log to find underpaid customer"""

    melon_cost = 1

    the_file = open("customer-orders.txt")

    for line in the_file:
        tokens = line.split("|")
        customer_name = tokens[1]
        customer_melon = tokens[2]
        customer_paid = tokens[3]
        customer_expected = customer_melon * melon_cost
        if customer_expected != customer_paid:
            customer_paid = float(customer_paid)
            customer_expected = float(customer_expected)
            print customer_name, "paid {:.2f}, expected {:.2f}".format(customer_paid, customer_expected)


underpaid_customer()
