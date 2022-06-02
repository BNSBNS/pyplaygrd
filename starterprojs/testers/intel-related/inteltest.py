from sklearn.preprocessing import StandardScaler

StdSc = StandardScaler()

StdSc = StdSc.fit(X_data)

X_scaled = StdSc.transform(X_data)