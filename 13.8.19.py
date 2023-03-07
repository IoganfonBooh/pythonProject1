# Вариант 1

# junior_tickets = input("Количество билетов для лиц младше 18 лет: ")
# middle_tickets = input("Количество билетов для лиц от 18 до 25 лет: ")
# senior_tickets= input("Количество билетов для лиц старше 25 лет: ")
# all_tickets = int(int(junior_tickets) + int(middle_tickets) + int(senior_tickets))
# print("Общее количество билетов: ", all_tickets)
# total_cost = int(middle_tickets)*990 + int(senior_tickets)*1390
# if all_tickets > 3:
#     total_cost = total_cost*0.9
# print("Общая стоимость билетов: ", total_cost, "руб")


# Вариант 2

# price_all = 0
# while True:
#     try:
#         ticket_number = input("Общее количество билетов: ")
#         ticket_number = int(ticket_number)
#         if type(ticket_number) == int:
#             break
#     except ValueError:
#         print('Введите целое число')
# for i in range(ticket_number):
#     i += 1
#     while True:
#         try:
#             age_for_ticket =  input(f"Для какого возраста билет № {i}?")
#             age_for_ticket = int(age_for_ticket)
#             if age_for_ticket < 18:
#                 print('Билет бесплатный')
#             elif 25 > age_for_ticket >= 18:
#                 price_all += 990
#                 print('Стоимость билета: 990 руб.')
#             else:
#                 price_all += 1390
#                 print('Стоимость билета: 1390 руб.')
#             if type(age_for_ticket) == int:
#                 break
#         except ValueError:
#             print('Введите целое число')
# if ticket_number > 3:
#     price_all = price_all * 0.9
#     print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой скидки')
# else:
#     print(f'Сумма к оплате {price_all} руб.')




