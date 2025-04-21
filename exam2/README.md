# **STRATEGIC MARKETING ANALYSIS: DATA-DRIVEN INSIGHTS FOR HIGH-IMPACT PROMOTIONS ACROSS CUSTOMERS, PRODUCTS, AND CAMPAIGNS**
Presented by: Faaza Naima

---

## **🧠 BUSINESS UNDERSTANDING**

### 🎯 Objective
Identify the most effective promotional strategy using the Pareto Principle (80/20) to maximize revenue impact.

### 💾 Dataset Overview
- **People:** Demographics, income, family status
- **Products:** Product categories and spending
- **Promotions:** Campaign & discount responses
- **Place:** Purchase channels

---

## **🔍 CAMPAIGN VS DISCOUNT PERFORMANCE**
| Strategy     | Acceptance Rate (%) | Revenue     |
|--------------|---------------------|-------------|
| cmp1         | 6.44%               | $213,440    |
| cmp2         | 1.34%               | $39,230     |
| cmp3         | 7.29%               | $117,448    |
| cmp4         | 7.47%               | $190,902    |
| cmp5         | 7.24%               | $261,573    |
| **last_cmp** | **14.93%**          | **$329,789**|
| **deals_buy**| **97.94%**          | **$1,298,249**|

✅ **Findings:** Discounts outperform campaigns significantly (97.9% vs 7.4%).

---

## **🧨 ROOT CAUSE: LOW CAMPAIGN SUCCESS**

### **Customers:**
- No clear demographic targeting
- No retention tracking
- Over-targeting one segment

### **Products:**
- No bundling strategy
- Poor timing, product mix, & channel choice
- Over-reliance on discounts

### **Strategy:**
- No clear campaign metrics
- Weak historical analysis
- Lack of re-engagement strategies

---

## **🌟 SCQA Framework**

### **1. Situation 🌟**
Over the past two years (2012-2014), data shows that Boomers with low working income are the biggest spenders. The company is looking for the best promotional method to increase revenue. However, there is a lack of detailed historical data to guide these efforts.

### **2. Complication ⚠**
The current marketing strategy is heavily reliant on discounts and campaigns. However, it’s unclear if these tactics are effectively contributing to revenue growth in a meaningful way. This uncertainty complicates decision-making, as the company doesn’t know whether to continue with the existing strategy or pivot to something more effective. 🤔

### **3. Question ❓**
To resolve this issue and make informed decisions, the key questions are:
- What marketing strategy would be most effective in driving revenue?
- Which customer segment should be the main focus to maximize impact?
- Which products should be prioritized to generate the highest returns?
- When is the optimal time to implement the strategy?
- Which sales channel is the most effective to target?

### **4. Answer ✅**
To effectively drive revenue, use **Pareto Analysis (80/20)** to focus on the 20% of products and customers that generate 80% of the revenue. This analysis will allow the company to:
- Prioritize the most valuable customer segments, such as Boomers with low working income.
- Focus on the top 20% of products that contribute to the bulk of the revenue.
- Target optimal times for promotions based on purchasing patterns.
- Determine the most effective sales channels (e.g., online, in-store, etc.) to reach the right customers.

---

## **📊 DATA UNDERSTANDING**

- **Average age:** 55 years
- **Average income:** $52,247
- **Days since last purchase:** 49 days
- **Top product:** Wine, followed by Meat
- **Favorite channel:** In-store
- **Promo engagement:** Low

---

## **🛠️ DATA PREPARATION**

### 1. **Cleaning:**
- Median imputation (MCAR), formatting, no duplicates
- Outliers:
  - Income (right-skewed): 0.36%
  - Year of Birth (left-skewed): 0.135%

### 2. **Feature Engineering:**
- Age, IsParent, TotalCampaignsAcc
- Education, family status, generation classification

---

## **📈 DATA VISUALIZATION INSIGHTS**
- **Gen X** has the highest spending
- **Wine** is the favorite product across generations
- **Household status “Together”** contributes 48% of total spending
- **In-store** is the top channel for Boomers & Gen X
- **At Risk & Can’t Lose** segments need urgent re-engagement

---

## **🤖 MODELING INSIGHTS**

### **1. Customer & Spending**
- Retained: 60.54% | Churned: 39.46%
- High-Value Customers: 19.91%
- Avg Order Value: $48.30
- Avg Orders: 12.5

### **2. Campaign Performance**
- Avg campaign acceptance: 7.45%
- Last campaign: best performance at 14.9%
- Deals buyers: highest response at 97.95%

### **3. Channel Usage**
- **In-store** purchases dominate

---

## **💰 CUSTOMER SEGMENTATION**

### **Income Class vs Product Preference**
- **Middle Class:** 75.3%
- **Lower-income** prefers Meat
- **Sweet Products:** lowest across all classes

---

## **🧮 CUSTOMER LIFETIME VALUE (CLV)**

### Formula:
**CLV = (Customer Value × 5) / (1 + Churn Rate)**

- High-value customers: 19.91%

---

## **📊 COHORT & RFM ANALYSIS**

### **RFM Segmentation:**
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

## **🛒 MARKET BASKET ANALYSIS**

Use Association Rules for product bundling:
- **Bundle ideas:**
  - Wine + Meat for: Loyal, Champions, Can’t Lose segments
  - Cross-selling opportunities (e.g., wine + gold)

---

## **📉 DISCOUNT IMPACT ANALYSIS**

### **Discount users:**
- Lower spending
- Less loyal long-term
- Overuse of discounts may reduce lifetime value

---

## **✅ FINAL RECOMMENDATIONS**

## Campaign Effectiveness
The last campaign had the highest success rate (14.93%), proving that targeting campaigns with strong incentives and high-value customer segments leads to better engagement. 🎯

## Customer Segmentation
- **Reengagement:** Focus on **At-Risk** and **Can’t Lose** customers with personalized offers or win-back strategies. 🔄
- **Premium Strategy:** Nurture **Loyal Customers** with exclusive rewards and incentivize **Champions** with referral bonuses to boost advocacy. 🏅

## Revenue Growth
Shift from frequent discount-driven campaigns to **engagement-focused** strategies for long-term revenue growth. 💡  
Discount campaigns tend to attract lower-value segments and do not drive sustained revenue. ❌💸

## Product Bundling
- Bundle **Wine and Meat** for **Loyal Customers** and **Champions** in premium offers to increase basket size. 🍷🥩
- Use **Wine and Meat Regular Bundles** to re-engage **At-Risk** customers with attractive pricing. 💵
- Introduce **Meat/Wine and Gold cross-sells** for luxury-focused promotions. 💎

## Campaign Timing
Launch during the **third quartile**, aligning with key events (e.g., July 4th, Back-to-School) to maximize engagement and sales. 📅🎉

## Sales Channel Optimization
- Prioritize **in-store sales** as it dominates transactions, especially among **Baby Boomers** and **Gen X**. 🏬
- Leverage the **15.5% growth** in e-commerce by enhancing the online experience and targeting the growing number of digital shoppers. 🌐💻

---

## **🎯 TRADE-OFF DECISION STRATEGY: MAXIMIZE AVERAGE SPENDING PER CUSTOMER**

## **Objective:**  
Maximize average spending by prioritizing high-value customer segments and retention-focused campaigns.

## **Campaign Recommendations:**  
1. **cmp1**: Target **Loyal Customers** and **Can’t Lose** for upselling.
2. **cmp5**: Focus on **Loyal** and **Champions** with exclusive rewards.
3. **last_cmp**: Retarget **New**, **Loyal**, and **At Risk** customers.
4. **cmp4**: Reactivate **Hibernating** customers with seasonal offers.

## **Campaign Strategy Options:**

- **Option 1: Broad Campaign**  
  - **Pros**: Wide reach  
  - **Cons**: High cost, lower ROI  

- **Option 2: Focused Campaign**  
  - **Pros**: Higher ROI, better retention  
  - **Cons**: Misses new/dormant customers  

## **80/20 Rule:**  
Target top 20% of customers (Champions, Loyal) for maximum revenue.

## **Final Recommendation:**  

Go with Option 2 for cost-effective, targeted campaigns focused on loyalty and retention.
---

