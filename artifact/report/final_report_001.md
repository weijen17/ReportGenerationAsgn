## **Business Question 1**
The business question: sales performance trend over time. Dimension to be considered is by year, and year plus region.

### **Main Finding**
From 2020 to 2024, BMW's sales performance showed a fluctuating yet generally upward trend. Sales increased from 16,310,843 units in 2020 to a peak of 17,920,946 units in 2022, followed by a decline in 2023 to 16,268,654 units, and a recovery to 17,527,854 units in 2024. This pattern indicates overall growth, with 2023 as an exception due to a dip in sales.

Regionally, Africa, Asia, Europe, and South America mirrored this trend, with growth until 2022, a decline in 2023, and recovery in 2024. Asia showed a steady increase, reaching 3,080,909 units in 2024. The Middle East maintained stable sales with minor fluctuations, peaking in 2022. North America peaked in 2022, followed by a decline in 2023 and a slight decrease in 2024. Most regions peaked in 2022, declined in 2023, and varied in recovery by 2024, reflecting the global sales trend.

### **Supporting Figures**

<p align="center">
    <img src="../plot/bs1_task1.png" alt="Sales Performance Trend by Year" width="400"/>
    <img src="../plot/bs1_task2.png" alt="Sales Performance Trend by Year and Region" width="400"/>
</p>

## **Business Question 2**
The business question: highlight top-performing and underperforming models or markets.

### **Main Finding**
The 7 Series and X6 are the top-performing models, with sales volumes of 8,177,442 and 8,099,240 units, respectively. The M5 and 3 Series also perform well, with sales of 7,807,649 and 7,741,253 units. Conversely, the X5, i3, and M3 models underperform, with lower sales volumes of 7,449,141, 7,544,460, and 7,571,963 units, respectively.

Regionally, Europe is the top-performing market with 14,565,989 units sold, followed by the Middle East with 14,528,396 units. North America also shows strong performance with 14,301,712 units sold. Africa and Asia have moderate sales volumes, while South America is the underperforming market with 13,643,807 units.

Overall, the 7 Series and X6 lead in sales, while Europe and the Middle East are the top markets. The X5, i3, and M3 models, along with South America, are underperforming.

### **Supporting Figures**

<p align="center">
  <img src="../plot/bs2_task1.png" alt="Sales Volume by Model" width="400"/>
  <img src="../plot/bs2_task2.png" alt="Sales Volume by Region" width="400"/>
</p>

## **Business Question 3**
The business question: explore key drivers of sales (e.g., price, market segment, or model type), compare across dimensions. Market segment refers to color, fuel_type, transmission, and engine_size. For price and engine_size, use Price_USD_Category and Engine_Size_L_Category fields.

### **Main Finding**
Key drivers of BMW sales include model type, price range, and market segment attributes. The 7 Series and X6 models have the highest sales volumes, indicating strong demand, while the X5 has the lowest. Mid-range priced models ($50,000-$100,000) have the highest sales, suggesting consumer preference for this price range.

In market segments, Black is the most popular color, followed by Red and White. Hybrid vehicles lead in sales, followed by Electric and Petrol, with Diesel being least favored. Manual transmission slightly edges out Automatic. Smaller engine sizes (0,2.4] and (2.4,3.3]) have higher sales, with a decline as engine size increases beyond 3.3 liters.

Overall, consumer preferences are influenced by model type, price range, and market segment attributes, with mid-range pricing, smaller engines, and hybrid fuel types being significant drivers of demand.

### **Supporting Figures**

<p align="center">
    <img src="../plot/bs3_task1.png" alt="Impact of Model on Sales Volume" width="300"/>
    <img src="../plot/bs3_task2.png" alt="Impact of Price on Sales Volume" width="300"/>
    <img src="../plot/bs3_task4.png" alt="Impact of Fuel Type on Sales Volume" width="300"/>
</p>

## **Business Question 4**
The business question: identify product market fit of each region.

### **Main Finding**
BMW's market performance varies by region. Europe and the Middle East lead in sales volume, with North America also performing well. Africa and Asia have similar sales volumes, while South America has the lowest. The 3 Series and 7 Series are popular in most regions, while the M3 is less favored. Asia has the highest average and median prices, while South America has the lowest. Hybrid and Electric vehicles are prevalent across most regions, with Petrol significant in North and South America.

Transmission preferences are balanced, with a slight edge for manual in Europe and the Middle East. Smaller engines (0 to 2.4 liters) are preferred across all regions. Mileage distribution shows higher mileage vehicles (150,000 to 200,000 km) in most regions, except the Middle East, which favors lower mileage. Black and Grey are popular colors, with regional variations in other color preferences.

Overall, Europe and the Middle East are key markets, with strong sales and distinct preferences. Asia stands out for higher prices, while North and South America prefer Petrol vehicles. Understanding regional preferences is crucial for catering to each market's demands.

### **Supporting Figures**

<p align="center">
    <img src="../plot/bs4_task1.png" alt="Sales Volume by Region" width="300"/>
    <img src="../plot/bs4_task3.png" alt="Price USD Distribution by Region" width="300"/>
    <img src="../plot/bs4_task4.png" alt="Fuel Type Distribution by Region" width="300"/>
</p>

## **Business Question 5**
The business question: shift in consumer preference over time (e.g., model, color, fuel_type, transmission, Engine_Size_L_Category, or Price_USD_Category). Use sales percentage as the main metric.

### **Main Finding**
From 2020 to 2024, consumer preferences for BMW models, colors, fuel types, transmission types, engine sizes, and price categories have shifted. The 7 Series and X5 maintained strong sales, while the X6 gained popularity, and the M3 and 3 Series declined. Color preferences shifted from Silver and Black in 2020 to Blue and Red by 2024. Hybrid and Electric vehicles gained favor, while Diesel and Petrol declined. Manual transmissions became more popular from 2021, maintaining a slight majority over automatic.

Smaller engine categories (0,2.4] and (2.4,3.3]) grew in popularity, while larger engines (3.3,4.1] and (4.1,5.0]) declined. Mid-range vehicle preferences remained stable, with a slight increase for lower-priced vehicles and a decrease for higher-priced ones. These trends highlight a shift towards environmentally friendly options and more affordable, efficient models, reflecting changing consumer priorities.

### **Supporting Figures**

<p align="center">
    <img src="../plot/bs5_task1.png" alt="Shift in Consumer Preference for BMW Models" width="300"/>
    <img src="../plot/bs5_task3.png" alt="Shift in Consumer Preference for Fuel Types" width="300"/>
    <img src="../plot/bs5_task5.png" alt="Shift in Consumer Preference for Engine Size Categories" width="300"/>
</p>

## **Conclusion**
The analysis of BMW's sales data from 2020 to 2024 reveals a generally upward trend in sales, with a notable dip in 2023. The 7 Series and X6 models are top performers, while the X5, i3, and M3 models underperform. Europe and the Middle East are the strongest markets, with South America lagging. Key sales drivers include model type, mid-range pricing, and market segment attributes like color, fuel type, and engine size. Consumer preferences have shifted towards environmentally friendly options and more affordable models, reflecting changing priorities.

## **Actionable Insight**
To capitalize on these findings, BMW should focus on strengthening its presence in Europe and the Middle East, while exploring strategies to boost sales in South America. Emphasizing the production and marketing of top-performing models like the 7 Series and X6, and expanding the range of Hybrid and Electric vehicles, could align with consumer trends. Additionally, offering competitive pricing in the mid-range category and promoting models with smaller engine sizes could further enhance market appeal. Understanding and adapting to regional preferences will be crucial for BMW's continued growth and success.