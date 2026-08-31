import random

def mailing_rand(clients_ot: int, clients_do: int, how: int) -> set:
    list_for_mailing = []
    for i in range(0,how):
        list_for_mailing.append(random.randint(clients_ot, clients_do))
    return list_for_mailing

'''
Маркетолог готовит рассылку: есть список email тех, кто покупал в этом месяце, и список email тех,
кто подписан на новости. Нужно отправить письмо только тем, кто и покупал, и подписан.

Ввод: два списка строк (email).

Вывод: множество email, которым нужно отправить письмо (пересечение)
'''

who_sale = set(mailing_rand(1,31, 10))
who_signet = set(mailing_rand(1,51, 10))

for_mailing = who_sale.intersection(who_signet)

print (who_sale)
print (who_signet)
print (for_mailing)











