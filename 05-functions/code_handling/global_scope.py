company_name = "Acme, Inc."
stock_symbol = "ACME"


def create_company():
    return {
        'name': company_name,
        'stock_symbol': stock_symbol
    }


company = create_company()
print(company)
