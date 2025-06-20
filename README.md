# 📈 Matcha Case Analyzation Study 
## Analyzing Uji, Japan's Agricultural Output to Inform Supply Chain and Demand Planning Decisions 

## What is Matcha?

**Matcha is a high-grade green tea from Japan** that is ground into a powdered form. Recently, it's become very popular abroad to serve it iced or mixed with milk as a latte. Matcha's great taste as well as its health benefits has led to a demand surge during the pandemic as people searched out health alternatives. According to Forbes, the matcha market is expected to hit about $5 billion by 2028, equating to a 10.39% compound annual growth rate from 2023 to 2028. This has led to a **matcha shortage**, where there is currently not enough of it to go around. 


## Why Matcha from Uji, Kyoto?

Using Python, SQL, and Tableau, data from the official "Kyoto Prefecture Public Relations" was used to analyze agricultural output of different green tea leaves from Uji, Kyoto (Japan). Uji's matcha data was used for these primary reasons:

1. Uji, Kyoto is the primary producer of high-quality matcha and also the birthplace / gold standard of matcha. 
2. Currently in 2024/2025, the shortage of unattainable matcha refers to the matcha from Uji, Kyoto. It is possible to easily attain lower quality matcha from regions outside of Uji, Kyoto and even countries outside of Japan such as China. 
3. The data from "Kyoto Prefecture Public Relations" on Uji, Kyoto is not only reliable, but it is powerful, showing authentic data from 2003-2024.


## Key Insights Summary

1. U.S. interest in matcha has grown over 4x since 2020, with projections indicating potential 10x growth by 2030
2. Matcha prices have remained relatively flat despite surging global popularity
3. Aracha production has remained relatively flat, with **other green tea outputs reduced to prioritize Matcha production**
4. There is a wide gap between Matcha supply and demand, raising **important questions for pricing strategy and agricultural planning**

---

# Overview

## Data Pulling and Understanding 

Data from Kyoto Prefecture Public Relations is in japanese with no english, so it was important to translate and understand what data we wanted to use. The key data pulled were values of Aracha, as well as Tencha, Sencha, Kabusecha, and Gyokuro. It is important to note that **Aracha is the unprocessed form of green tea**, and it **makes up** either/only one of **Tencha (Matcha, the value we're focusing on)**, Sencha, Kabusecha, Gyokuto, and Bancha. 

In order to evaluate matcha supply performance, we focused on the following metrics for each of the green teas: **Production Volume in Tons, Production Value in Yen, and Field Size in Hectare**. 

Example of pulling for how much field in hectares is reserved for Tencha/Matcha:

<img width="800" alt="image" src="https://github.com/user-attachments/assets/7c57acb4-e39e-4e41-9115-55a349087e2f" />

> Filepath: Matcha_Analysis/data/raw_pdfs
>
> Kyoto Prefecture Public Relations website: https://www.pref.kyoto.jp/nosan/chagyotokei.html

Example Output of PDF Read Result:
```
[Page 3]
区 分 令和６年度 令和５年度 前年対比
ｔ ｔ ％
荒 茶 生 産 量 2,492.4 2,427.2 102.7
煎 茶 248.4 250.9 99.0
か ぶ せ 茶 141.6 138.8 102.0
玉 露 134.3 135.1 99.5
て ん 茶 1,057.0 944.9 111.9
秋 て ん 茶 *1 591.1 538.1 109.8
番 茶 319.9 419.4 76.3
百万円 百万円 ％
荒 茶 生 産 金 額 8,859.0 7,169.1 123.6
煎 茶 713.5 677.7 105.3
か ぶ せ 茶 438.3 416.4 105.3
玉 露 742.4 702.6 105.7
て ん 茶 6,291.9 4,747.2 132.5
秋 て ん 茶 *1 496.4 413.1 120.1
番 茶 176.6 212.1 83.3
工場 工場 ％
```

Code to Extract Data from Output:
```
match_tencha_field = re.search(r"て\s*ん\s*茶\s*園\s*([\d,]+\.\d+)", text)
                if match_tencha_field:
                    row["tencha_field_ha"] = float(match_tencha_field.group(1).replace(",", ""))
```
> Codepath: Matcha_Analysis/scripts/extract_data.py

## Using Addtional Data from Google Trends

Google Trends was used to search the popularity of Matcha in the US and Japan, as it is the most popular search engine. Although interest does not directly equal demand, there is strong correlation coupled with authentic data from Google that is not offered anywhere else regarding reliable matcha consumerism datasets. 

Example: Because "Matcha" had a score of 100 in 12/2024 and a score of 51 in 05/2025, it means it became twice as popular by 05/2025 compared to 12/2024, relative to the peak popularity within those specific timeframes.


## 

Kyoto Prefecture Public Relations only has **YEARLY** data from 2003 - 2024. Thus, Google Trends Matcha Search Index 01/2003 - 12/2024 (month/year) was our base 1-100 index score.

Google Index data past 12/2024 (from 01/2025 - 05/2025) was used for better data modeling using SARIMA. But first, we needed to convert the 2025 data past the 100 index mark relative to our base indexes as accurately as possible: 

![Screenshot 2025-06-20 at 2 36 28 PM](https://github.com/user-attachments/assets/35a7e59f-5f10-41bc-a16f-08e7ebc84f3e)

> Codepath: Matcha_Analysis/scripts/LinearRegression.py

After we have our new calculated/predicted values 01/2025 - 05/2025, we use these up-to-date values to generate a Matcha trend forecast all the way up to 2030:

![image](https://github.com/user-attachments/assets/41a8ba55-9054-4088-931a-2c2d6ebcd664)

> Codepath: Matcha_Analysis/scripts/forecast.py

### Deeper dive into matcha Price and Demand

Using our government data from Uji, we got the Value of Matcha ¥/lbs (= Tencha/Matcha Product Value ¥ / Tencha/Matcha Production Volume in Tons * 2000 lbs/Tons). We compared that with Google Matcha Trend 1-100 index for the U.S., Japan, and Worldwide during 2004-2024. Because our government data only releases by year, the average of 12 months for every year was used for Google Trend's index to keep time consistency. 

![image](https://github.com/user-attachments/assets/8e6e669b-7196-41de-b98e-d1f3c5819907)

> Tableau Interactive Link: [https://public.tableau.com/views/MatchaAnalysis/Dashboard2?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link](https://public.tableau.com/views/MatchaAnalysis/Dashboard2?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

This leads us to the next question, **if Japan does not raise matcha's price despite its surging popularity**, **what have they done in Supply to meet Demand?**

## Deeper dive into Supply due to Surging Demand

***A common assumption is that Uji, Japan likely expanded land for Aracha production to increase Tencha/Matcha output; however, that is not the case.***

![image](https://github.com/user-attachments/assets/534d0b62-182e-4b8d-90fa-6dddd9095d6c)

> Tableau Interactive Link: https://public.tableau.com/views/MatchaAnalysis/Dashboard3?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

![image](https://github.com/user-attachments/assets/fb46a59a-7362-44ee-8489-ad9c64ea7736)

> Tableau Interactive Link: https://public.tableau.com/views/MatchaAnalysis/Dashboard1?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
> 
> Tableau Interactive Link 2: https://public.tableau.com/views/MatchaAnalysis/Sheet12?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link


## Conclusion & Recommendations
![image](https://github.com/user-attachments/assets/0ad2f475-a6fe-4f77-95b5-2b3d356b0a3a)
![image](https://github.com/user-attachments/assets/9a705eb3-6140-4bc1-ac99-cb22c71f1817)
![image](https://github.com/user-attachments/assets/e9e37b67-78b3-4509-807b-e47f7c27af6e)

