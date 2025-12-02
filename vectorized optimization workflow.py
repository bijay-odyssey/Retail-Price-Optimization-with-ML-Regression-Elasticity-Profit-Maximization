# Vectorized Price Elasticity (faster)
def compute_elasticity(df, model, pct=0.01):
    df_up = df.copy()
    df_up["unit_price"] = df["unit_price"] * (1 + pct)

    q0 = model.predict(df)
    q1 = model.predict(df_up)

    elasticity = ((q1 - q0) / q0) / pct
    return elasticity

df["elasticity"] = compute_elasticity(df, pipe_final)
df["elasticity"].describe()

# Vectorized Price Simulation (+/–10%)
df_90 = df.copy()
df_90["unit_price"] = df["unit_price"] * 0.90

df_110 = df.copy()
df_110["unit_price"] = df["unit_price"] * 1.10

df["q_minus10"] = pipe_final.predict(df_90)
df["q_plus10"]  = pipe_final.predict(df_110)

# Profit Curve
def simulate_price_curve(row, model, prices):
    temp = pd.DataFrame([row] * len(prices))
    temp["unit_price"] = prices

    qty = model.predict(temp)
    cost = row["avg_comp_price"]   

    revenue = prices * qty
    profit = (prices - cost) * qty

    return pd.DataFrame({
        "price": prices,
        "qty": qty,
        "revenue": revenue,
        "profit": profit
    })
example = df.iloc[0]
prices = np.linspace(20, 350, 70)

pc = simulate_price_curve(example, pipe_final, prices)

# plot
plt.plot(pc["price"], pc["profit"], label="Profit")
plt.plot(pc["price"], pc["revenue"], label="Revenue", linestyle="--")
plt.legend()
plt.title("Profit & Revenue Curve")
plt.xlabel("Price")
plt.ylabel("Value")
plt.show()

# Optimal Price
optimal = pc.loc[pc["profit"].idxmax()]
optimal

# optimal price for all products
def get_optimal_price(row):
    prices = np.linspace(
        row["unit_price"] * 0.5, 
        row["unit_price"] * 1.5, 
        50
    )
    pc = simulate_price_curve(row, pipe_final, prices)
    opt = pc.loc[pc["profit"].idxmax()]
    return opt["price"]

df["optimal_price"] = df.apply(get_optimal_price, axis=1)


