# Input same amout and calculate discount based on the amount and given discount rate in Python.

# The discount rates are:

#     Amount              Discount
#     0-5000              5%
#     5000-15000          12%
#     15000-25000         20%
#     above 25000         30%


def calculate_discount_function(amt):
    disc=0
    if(amt>0):
        if amt <= 5000:
            disc = amt*0.05
        elif amt<=15000:
            disc=amt*0.12
        elif amt<=25000:
            disc=amt*0.2
        else:
            disc=0.3*amt

        # print("Discount : ", disc)
        # print("Net Pay :", amt-disc)

    else:
        print("Invalid Amount")

    return disc

calculate_discount_function(10000)