#write functions here, don't add input('') statements here! 
def get_bonus_pay_amount(sales): 
    if sales < 0 or sales > 1999: 
        return 'Invalid argument' 
    elif sales >= 0 and sales < 500: 
        return sales * 0.05 
    elif sales < 1000: 
        return sales * 0.06 
    elif sales < 1500: 
        return sales * 0.07 
    else: # sales is between 1500 and 1999 
        return sales * 0.08 