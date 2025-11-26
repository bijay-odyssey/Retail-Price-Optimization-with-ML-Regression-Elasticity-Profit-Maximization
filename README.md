# Retail Price Optimization with Machine Learning, Elasticity & Profit Maximization

---

> This repository contains a **complete end-to-end price optimization system** built using **Machine Learning regression**, **competition-adjusted elasticity**, and **profit-curve simulation**.
> The goal is to help retailers determine **profit-maximizing prices** for products based on demand behavior, competitive positioning, and customer sensitivity to price changes.

---

## Project Highlights

* **Gradient Boosting / Random Forest regression** for demand prediction
* **Competition-adjusted price elasticity estimation**
* **Price simulations (+/−10%)** to test sensitivity
* **Profit curve construction** for individual products
* **Optimal price selection** that maximizes predicted profit
* **Feature importance & SHAP interpretability**
* **Hyperparameter tuning with Optuna**
* **Fully documented Jupyter Notebook**

---

## Business Problem

Retailers often struggle with:

* Setting the **right price**
* Understanding **customer sensitivity**
* Reacting to **competitor prices**
* Maximizing **profit without losing demand**

> This project provides a **data-driven pricing engine** that replaces intuition with **ML-based price optimization**.

---

## Technical Workflow

### **1. Data Preparation**

* Handling missing values
* Feature engineering
* Creation of competition-based variables
* Lag price and moving averages

---

### **2. Machine Learning Demand Model**

A tree-based regression model predicts **quantity sold** using:

* Product price
* Competitor price
* Category
* Brand
* Promo status
* Time variables

**Pipeline includes:**

* Preprocessing pipeline
* Train/validation/test split
* Optuna hyperparameter optimization
* Evaluation with **RMSE** & **R²**

---

### **3. Competition-Adjusted Price Elasticity**

Elasticity is computed using a **1% price change simulation**:

[
\text{Elasticity} = \frac{\Delta Q / Q}{\Delta P / P}
]

**Findings:**

* Average elasticity: *–0.45 (inelastic)*
* Some products highly elastic (up to *–7*)
* Some products unresponsive (*0 elasticity*)

---

### **4. Price Simulation (+/−10%)**

Demand is predicted at:

* Price × 0.9
* Price × 1.1

> This helps validate **model responsiveness** and **elasticity realism**.

---

### **5. Profit Curve Simulation**

For a selected product:

* Prices simulated from **20 → 350**
* Demand predicted at each point
* Revenue calculated
* Profit computed using:

[
\text{Profit} = (\text{Price} - \text{Cost}) \times \text{Quantity}
]

> This produces a **profit curve**, showing the **profit-maximizing price**.

---

### **6. Optimal Price Detection**

Example output:

| Metric         | Value      |
| -------------- | ---------- |
| Optimal Price  | $350.00    |
| Optimal Demand | 1.27 units |
| Optimal Profit | $296.25    |
| Current Price  | $45.95     |
| Current Profit | –$88.19    |

* **Profit Swing:** +$384.44
* **Transformation:** From losses → positive profit

---

## Key Insights

* Demand is **mostly inelastic** → retailers have margin room
* Competitive price positioning strongly affects sales
* Lag effects show customers react to price jumps
* Optimal prices are often **higher than current prices**
* ML-based profit optimization generates **substantial uplift**

---

## Future Improvements

* Multi-product cross-elasticity modeling
* Dynamic daily pricing engine
* Reinforcement learning for automated re-pricing
* Promotion/POS uplift modeling

---

## Author

**Bijay @ bijay-odyssey**
ML enthusiast specializing in retail analytics, pricing science, and demand forecasting.

--
