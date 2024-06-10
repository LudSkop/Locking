# Функція для розрахунку податку.
def taxer(base_tax):
    def calculate(money):
        base_tax_1 = base_tax
        if money >= 10_000:
            base_tax_1 = base_tax * 2
        return money - base_tax_1 * money
    return calculate


ukr = taxer(0.01)
norv = taxer(0.04)


money_ukr = ukr(9500)
money_norv = norv(25000)

print(money_ukr)
print(money_norv)