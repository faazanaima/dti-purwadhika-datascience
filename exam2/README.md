# **Strategic Marketing Analysis: Data-Driven Insights for High-Impact Promotions Across Customers, Products, and Campaigns**
Presented by: Faaza Naima

**🧠 BUSINESS UNDERSTANDING**

🎯 Objective
Identify the most effective promotional strategy using the Pareto Principle (80/20) to maximize revenue impact.

💾 Dataset Overview
1. People: Demographics, income, family status
2. Products: Product categories and spending
3. Promotions: Campaign & discount responses
4. Place: Purchase channels

****🔍 CAMPAIGN VS DISCOUNT PERFORMANCE****
| Strategy   | Acceptance Rate (%) | Revenue     |
|------------|----------------------|-------------|
| cmp1       | 6.44%                | $213,440     |
| cmp2       | 1.34%                | $39,230      |
| cmp3       | 7.29%                | $117,448     |
| cmp4       | 7.47%                | $190,902     |
| cmp5       | 7.24%                | $261,573     |
| **last_cmp** | **14.93%**         | **$329,789** |
| **deals_buy** | **97.94%**        | **$1,298,249** |

✅ Discounts outperform campaigns significantly (97.9% vs 7.4%)

🧨 ROOT CAUSE: LOW CAMPAIGN SUCCESS
Customers
1.No clear demographic targeting
2. No retention tracking
3. Over-targeting one segment
Products
1. No bundling strategy
2. Poor timing, product mix, & channel choice
3. Over-reliance on discounts
Strategy
1. No clear campaign metrics
2. Weak historical analysis
3. Lack of re-engagement

🌟 SCQA Framework:
1. Situation
Over the past two years (2012-2014), data reveals that Boomers with low working income are the biggest spenders. The company is actively looking for the best promotion method to increase revenue. However, there is a lack of detailed historical data to guide these efforts.
3. Complication ⚠
The current marketing strategy is heavily reliant on discounts and campaigns. However, it's unclear if these tactics are effectively contributing to revenue growth in a meaningful way. This uncertainty complicates decision-making, as the company doesn’t know whether to continue with the existing strategy or pivot to something more effective. 🤔
2. Question
To resolve this issue and make informed decisions, the key questions are:
1. What marketing strategy would be most effective in driving revenue?
2. Which customer segment should be the main focus to maximize impact?
3. Which products should be prioritized to generate the highest returns?
4. When is the optimal time to implement the strategy?
5. Which sales channel is the most effective to target?
Answer 
To effectively drive revenue, use Pareto Analysis (80/20) to focus on the 20% of products and customers that generate 80% of the revenue. This analysis will allow the company to:
- Prioritize the most valuable customer segments, such as Boomers with low working income.
- Focus on the top 20% of products that contribute to the bulk of the revenue.
- Target optimal times for promotions based on purchasing patterns.
- Determine the most effective sales channels (e.g., online, in-store, etc.) to reach the right customers.

📊 DATA UNDERSTANDING
- Average age: 55 years
- Average income: $52,247
- Days since last purchase: 49 days
- Top product: Wine, followed by Meat
- Favorite channel: In-store
- Promo engagement: Low

🛠️ DATA PREPARATION
1. Cleaning: Median imputation (MCAR), formatting, no duplicates
Outliers:
Income (right-skewed): 0.36%
Year of Birth (left-skewed): 0.135%

2. Feature Engineering:
Age, IsParent, TotalCampaignsAcc
Education, family status, generation classification

📈 DATA VISUALIZATION INSIGHTS
- Gen X has highest spending
- Wine is the favorite across generations
- Household status “Together” contributes 48% of total spending
- In-store is the top channel for Boomers & Gen X
- At Risk & Can’t Lose segments need urgent re-engagement

🤖 MODELING INSIGHTS
1. Customer & Spending
Retained: 60.54% | Churned: 39.46%
High-Value Customers: 19.91%
Avg Order Value: $48.30
Avg Orders: 12.5

2. Campaign Performance
Avg campaign acceptance: 7.45%
Last campaign: best performance at 14.9%
Deals buyers: highest response at 97.95%

3. Channel Usage
In-store purchases dominate

💰 CUSTOMER SEGMENTATION
Income Class vs Product Preference
Middle Class: 75.3%
Lower-income prefers Meat
Sweet Products: lowest across all classes

🧮 CUSTOMER LIFETIME VALUE (CLV)
Formula:
CLV = (Customer Value × 5) / (1 + Churn Rate)
High-value customers: 19.91%

📊 COHORT & RFM ANALYSIS
RFM Segmentation:
| Segment            | %       | Insight                            |
|--------------------|---------|-------------------------------------|
| At Risk            | 16.07%  | Previously active, now declining    |
| Hibernating        | 16.38%  | No longer active                    |
| Potential Loyalist | 15.54%  | Recently active, good potential     |
| Loyal              | 15.45%  | Consistently engaged                |
| Champions          | 7.50%   | Most engaged & profitable           |
| Can’t Lose Them    | 7.01%   | High-value, must retain             |
| Promising/New      | ~10%    | New customers showing potential     |

---

🛒 MARKET BASKET ANALYSIS
Use Association Rules for product bundling
Bundle ideas:
1. Wine + Meat for: Loyal, Champions, Can’t Lose segments
2. Cross-selling opportunities (e.g., wine + gold)

📉 DISCOUNT IMPACT ANALYSIS
Discount users:
- Lower spending
- Less loyal long-term
- Overuse of discounts may reduce lifetime value

✅ FINAL RECOMMENDATIONS
