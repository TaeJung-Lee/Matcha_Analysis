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

(ENTER IMAGE OF matcha_2024 page 3)
> Filepath: Matcha_Analysis/data/raw_pdfs or Kyoto Prefecture Public Relations website

'''
match_tencha_field = re.search(r"て\s*ん\s*茶\s*園\s*([\d,]+\.\d+)", text)
                if match_tencha_field:
                    row["tencha_field_ha"] = float(match_tencha_field.group(1).replace(",", ""))
'''
> Codepath: Matcha_Analysis/scripts/extract_data.py

## Using Addtional Data from Google Trends

Google Trends was used to search the popularity of Matcha in the US and Japan, as it is the most popular search engine. Although interest does not directly equal demand, there is strong correlation coupled with authentic data from Google that is not offered anywhere else regarding reliable matcha consumerism datasets. 

Example: Because "Matcha" had a score of 100 in 12/2024 and a score of 51 in 05/2025, it means it became twice as popular by 05/2025 compared to 12/2024, relative to the peak popularity within those specific timeframes.


## 

Kyoto Prefecture Public Relations only has **YEARLY** data from 2003 - 2024. Thus, Google Trends Matcha Search Index 01/2003 - 12/2024 (month/year) was our base 1-100 index score.

Google Index data past 12/2024 (from 01/2025 - 05/2025) was used for better data modeling using SARIMA. But first, we needed to convert the 2025 data past the 100 index mark relative to our base indexes as accurately as possible: 

(ENTER TABLE)

(ENTER LINEAR REGRESSION)
R^2 value of .96 is very high and indicates that the vairables in our model does a great job of explaining the changes observed in the dependent variable 

(ENTER RESIDUAL PLOT)
Some of the actual observed values and predicted values by the regression model

Using our 2003-2024 index values coupled with our 2025 calculated values, we were able to generate a Matcha trend forecast all the way up to 2030. 

(INSERT PICTURE)
> Codepath: Matcha_Analysis/scripts/forecast.py

***Key Point 1:***
U.S. interest in matcha has grown over 4x since 2020, with projections indicating potential 10x growth by 2030

This leads us to some questions:
### Deeper dive into matcha Price and Demand

Using our government data from Uji, we got the Value of Matcha ¥/lbs (= Tencha/Matcha Product Value ¥ / Tencha/Matcha Production Volume in Tons * 2000 lbs/Tons). We compared that with Google Matcha Trend 1-100 index for the U.S., Japan, and Worldwide during 2004-2024. Because our government data only releases by year, the average of 12 months for every year was used for Google Trend's index to keep time consistency. 

(PICTURE)
> Tableau Interactive Link: 

***Key Point 2:***
Matcha popularity is increasing exponentially, while the estimated value of Matcha has not changed much. The estimated value had been slowly decreasing until 2020, and is now slowly increasing. 

***Why has matcha prices not risen despite its popularity?***

Unlike most countries that have seen prices steadily rise due to inflation, Japan has not experienced major price increases since the 1990s. From the cost of tuna sashimi to real estate to people's salary, Japan's prices rarely increase. This is due to Japanese culture where companies and consumers alike share a deflationary mindset that makes raising prices socially unacceptable.

However, according to our data, **Matcha's popularity has outpaced the current value of matcha since 2018-2020.**

This leads us to the next question, **if Japan does not raise matcha's price despite its surging popularity**, **what have they done in Supply to meet Demand?**

## Deeper dive into Supply due to Surging Demand

A common assumption is that Uji, Japan likely expanded land for Aracha production to increase Tencha/Matcha output; however, that is not the case.

(DATA PICTURE)
> Tableau Interactive Link: 

Key Point 3:
Aracha production has remained relatively flat, with other green tea outputs reduced to prioritize Matcha production

Once again, Aracha is used to make into Tencha/Matcha, Sencha, Kabusecha, Gyokuto, or Bancha (Only Tencha/Matcha is surging in demand). From our 2003-2024 Kyoto Prefecture Public Relations Data, **land HAS NOT expanded**, instead, **the total amount of land for all Green Teas has been the same**. In order to meet growing demand of Matcha, **Sencha has been increasingly cut in production to convert more of the Aracha into Matcha**. 

(DATA PICTURE)
> Tableau Interactive Link:

***Why hasn’t more land been allocated for matcha production?***

Expanding land for matcha production faces challenges due to its artisan labor intensive and delicate processing to maintain high quality. Space constraints in key regions like Uji and the need to preserve environmental conditions further limit expansion, as not all land is suitable for high grade matcha cultivation. As a result, farmers may focus on improving yield and quality on existing land rather than expanding into less ideal areas.


## Conclusion & Recommendations

***Key Point 4:***
There is a wide gap between Matcha supply and demand, raising **important questions for pricing strategy and agricultural planning**

This study reveals that matcha demand not only in the U.S. but also Worldwide has surged exponentially since 2020, but pricing and agricultural supply have not scaled at the same pace. Matcha prices remain relatively flat, constrained by Japan’s deflationary pricing culture and limited production of Matcha.

With mMtcha demand projected to continue growing strongly through 2030, this widening gap between supply and demand raises key questions for future pricing strategies, agricultural planning, and the sustainable future of Japan’s matcha industry.

### Recommendations: ###

1. Encourage gradual land expansion: Invest into high grade land and processes for Aracha/Matcha cultivation, with government support for proper shading infrastructure, skilled labor training, and financial incentives.

2. Raise international pricing: Create international pricing strategies to gradually adjust export pricing to better reflect demand and production costs. This could not only relieve domestic pricing pressures, but also ensure a healthier supply where global consumers don't bulk buy due to cheap costs but high popularity.

3. Promote sustainability and yield improvement: Invest in agricultural innovation to improve yield and quality on existing land while maintaining Uji’s environmental and cultural heritage.

These steps would help ensure that Japan’s matcha industry remains globally competitive and sustainably meets rising international demand.
