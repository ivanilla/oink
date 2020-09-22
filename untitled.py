def solution(S):
    # write your code in Python 3.6
    space_split = S.split('\n')
    
    # Create list of phone customers
    cust_list = []
    cust_set = set(cust_list)
    bills = []
    bills_set = set(bills)
    for i in range(len(space_split)):
        time_num_split = space_split[i].split(',')
        time_count = time_num_split[0]
        phone_num = time_num_split[1].replace('-','')
        entry = [phone_num, time_count]
        cust_list.append(entry)
        hours = int(cust_list[i][1].split(':')[0])
        minutes = int(cust_list[i][1].split(':')[1])
        seconds = int(cust_list[i][1].split(':')[2])
        total_secs = (hours * 60 * 60) + (minutes * 60) + seconds
        
        if len(bills_set) != len(bills):    #Condition for positive tie scenario
            for i in range(len(cust_list)):
                promo_winner_mins = cust_list[-1][1]
                print(promo_winner_mins)
        else:
            if total_secs >= 300:
                if seconds > 0: 
                    price = (150 * (minutes + 1))
                    cust_list[i][1] = price
                else:
                    price = (150 * minutes)
                    cust_list[i][1] = price
            else:
                price = total_secs * 3    
                cust_list[i][1] = price
            bills.append(price)
            cust_set.add(phone_num)
                
    return_value = (max(bills))    
    cust_list.sort()
    print(return_value)
    print(cust_list)



S = '00:01:07,400-234-090\n00:05:01,701-080-080\n00:05:00,400-234-090'

solution(S)