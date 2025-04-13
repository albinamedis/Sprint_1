types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 


def delete_dublicate():
    for i in range(1,6):
        for n in range(1,6):
            if i !=n and i<n:
                s1 = tickets[i]
                s2 = tickets[n]
                for j in s1:
                    for k in s2:
                        if j==k:
                            s2.remove(k)

                        
def tickets_by_type():
    level_list = {}
    for i in range(1,6):
        level_list[types[i]] = tickets[i]
    print(level_list)

delete_dublicate()
tickets_by_type()
