def grouping_dishes(dishes):
    ls = []
    d = {}
    for j, i in enumerate(dishes):
        for k in i[1:]:
            if k not in d:
                d[k] = [i[0]]
            else:
                d[k].append(i[0])
    
    result = []
    for k, v in d.items():
        res = []
        if len(v) >= 2:
            res.append(k)
            res.append(sorted(v))
            result.append(res)
            
    return sorted(result)


dish = [["Salad","Tomato","Cucumber","Salad","Sauce"], 
 ["Pizza","Tomato","Sausage","Sauce","Dough"], 
 ["Quesadilla","Chicken","Cheese","Sauce"], 
 ["Sandwich","Salad","Bread","Tomato","Cheese"]]

result = grouping_dishes(dish)
print(result)
