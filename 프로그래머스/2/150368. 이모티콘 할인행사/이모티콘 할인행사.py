from itertools import product

def solution(users, emoticons):
    max_subscribers, max_revenue = 0, 0
    n = len(emoticons)
    discount_rate = [10,20,30,40]
    
    for discounts in product(discount_rate, repeat = n):
        subscribers, revenue = 0,0
        for min_discount, max_price in users:
            total_cost = 0
            for emoticon_price, discount_rate in zip(emoticons, discounts):
                if discount_rate >= min_discount:
                    total_cost += emoticon_price / 100 * (100 - discount_rate )
        
            if total_cost >= max_price :
                subscribers += 1
            else : revenue += total_cost
    
        if subscribers > max_subscribers or (subscribers == max_subscribers and max_revenue < revenue) :
            max_subscribers , max_revenue = subscribers  , revenue
    return [max_subscribers , max_revenue]