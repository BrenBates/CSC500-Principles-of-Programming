September_Enchilada_Sales = [5, 8, 3, 6, 11, 3, 5, 7, 12, 13, 0, 0, 2, 3, 1, 6, 8, 4, 13, 8, 3, 2]

cost = 3.65

sales_price = 5.50

enchilada_count = 0

for i in range(len(September_Enchilada_Sales)):

    enchilada_count = enchilada_count + September_Enchilada_Sales[i]

revenue = enchilada_count * (sales_price - cost)

avg_daily_enchiladas = enchilada_count / len(September_Enchilada_Sales)

print('In September, {} total enchiladas were sold.  Each enchilada cost ${} to make, but sold for ${}.  On average, {} enchiladas were sold per day.  Total revenue from enchilada sales was ${}'
      .format(enchilada_count,cost,sales_price,avg_daily_enchiladas,revenue))