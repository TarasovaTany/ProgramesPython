per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Ввведите сумму, которую планируете положить под процент:"))
list_percent = list(per_cent.values())
deposit = [list_percent*money/100 for list_percent in (map(float, list_percent))]
print(deposit)
print(str("Максимальная сумма, которую вы можете заработать — ") + str(max(deposit)))