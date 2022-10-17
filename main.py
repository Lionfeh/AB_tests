#1ая функция
def func_amount_of_clients_in_group_1(people):
    return len(people)


#2ая функция
def func_amount_of_clients_in_group_2(people, num):
    return len(people), people[0]


#Функция подсчета суммы чисел
def func_sum_of_num(num):
    coun = 0
    num = int(num)
    while num > 0:
        coun += num % 10
        num //= 10
    return coun


print('Здравствуйте!')
amount_of_clients = int(input('Введите количество клиентов для теста: '))
group_id = {}
#Вводим id клиентов
for i in range(amount_of_clients):
    id = input(f'Введите id {i + 1}го клиента: ')
    group = func_sum_of_num(id)
    #Проверяем есть ли такая группа
    if group in group_id:
        group_id[group].append(id)
    else:
        group_id[group] = [id]

#Работаем с функциями
for group, people in group_id.items():
    #Проверка на сквозную нумерацию
    is_prime = True
    coun = 0
    for id_now_grop in people:
        if coun != int(id_now_grop[0]):
            is_prime = False
            break
        coun += 1
    if is_prime:
        n_custumers = func_amount_of_clients_in_group_1(people)
        print('В группе {} - {} клиентов.'.format(group, n_custumers))
    else:
        n_custumers, n_first_id = func_amount_of_clients_in_group_2(people, 0)
        print('В группе {} - {} клиентов. id 1го - {}.'.format(group, n_custumers, n_first_id))