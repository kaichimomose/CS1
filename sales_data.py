def loadWord():
    with open("sales_data.txt", 'r') as f:
        salesLists = list(f.readlines())
    f.close()

    lists_A = []

    for salesList in salesLists:
        lists_A.append(salesList.replace("\n", ''))

    lists_B = []

    for list_A in lists_A:
        lists_B.append(list_A.split('\t'))

    money = []

    for list_B in lists_B:
        for item in list_B:
            if "$" in item:
                money.append(item.replace("$", ''))

    total = 0

    for bill in money:
        total += float(bill)

    # print(total)

    def filter_key(keyword, salesLists):
        sales_roster = []
        for salesList in salesLists:
            for item in salesList:
                if keyword in item:
                    if keyword == "1/":
                        if "11/" not in item:
                            sales_roster.append(salesList)
                    elif keyword == "2/":
                        if "12/" not in item:
                            sales_roster.append(salesList)
                    else:
                        sales_roster.append(salesList)
        return sales_roster

    """What are the total amount of sales contained in this data set?"""

    total_amount = 0

    salesLists_each_city = []

    for salesList in salesLists:
        n = salesList.replace("\n", '')
        t = n.split('\t')
        salesLists_each_city.append(t)
        for item in t:
            if "$" in item:
                money = item.replace("$", '')
                total_amount += float(money)

    # print(salesLists_each_city)
    print(total_amount)

    """Which city had the highest sales in February?"""

    city_roster = []
    feb_sales = []
    total_amount_each_city = {}

    for salesList in salesLists_each_city:
        city_name = salesList[0]
        if city_name not in city_roster:
            city_roster.append(city_name)

    for salesList in salesLists_each_city:
        for item in salesList:
            if "2/" in item:
                if "12/" not in item:
                    feb_sales.append(salesList)

    for city in city_roster:
        total_amount_each_city[city] = 0
        for feb_sale in feb_sales:
            if city in feb_sale:
                for item in feb_sale:
                    if "$" in item:
                        money = item.replace("$", '')
                        total_amount_each_city[city] += float(money)

    # print(total_amount_each_city)

    def largest_amount(dic):
        largest_amount = 0
        for key in dic:
            amount = dic[key]
            if amount > largest_amount:
                largest_amount = amount
            else:
                largest_amount = largest_amount
        for key in dic:
            if dic[key] == largest_amount:
                print("%s %s" % (key, largest_amount))
            else:
                pass

    largest_amount(total_amount_each_city)

    """Out of the entire data set, what is the total amount of money
 people have paid in cash?"""

    payment_way_roster = []

    for salesList in salesLists_each_city:
        payment_way = salesList[2]
        if payment_way not in payment_way_roster:
            payment_way_roster.append(payment_way)
    # print(payment_way_roster)

    cash_roster = []
    credit_roster = []

    for salesList in salesLists_each_city:
        for item in salesList:
            if "Cash" in item:
                cash_roster.append(salesList)
            else:
                credit_roster.append(salesList)

    total_amount_with_cash = 0

    for cash in cash_roster:
        for item in cash:
            if "$" in item:
                money = item.replace("$", '')
                total_amount_with_cash += float(money)
    print(total_amount_with_cash)

    """What is the most popular payment type in Oakland in March?"""

    total_amount_each_way = {}

    for a_way in payment_way_roster:
        total_amount_each_way[a_way] = 0
        for salesList in filter_key(a_way, filter_key("5/", filter_key("Oakland", salesLists_each_city))):
            for item in salesList:
                if "$" in item:
                    money = item.replace("$", '')
                    total_amount_each_way[a_way] += float(money)

    largest_amount(total_amount_each_way)

    """How many sales were made on 4/20, and which city had the highest sales value?"""

    total_amount_each_city_4_20 = {}

    for city in city_roster:
        total_amount_each_city_4_20[city] = 0
        for salesList in filter_key("4/20", filter_key(city, salesLists_each_city)):
            for item in salesList:
                if "$" in item:
                    money = item.replace("$", '')
                    total_amount_each_city_4_20[city] += float(money)
    # print(total_amount_each_city_4_20)

    largest_amount(total_amount_each_city_4_20)

    """What is the average sales amount for credit card purchases?"""

    credit_total_amount = 0

    for salesList in filter_key("Credit", salesLists_each_city):
        for item in salesList:
            if "$" in item:
                money = item.replace("$", '')
                credit_total_amount += float(money)

    print(credit_total_amount)

    """How many purchases were made by bartering with baseball cards?"""

    print(len(filter_key("Baseball Cards", salesLists_each_city)))


loadWord()
