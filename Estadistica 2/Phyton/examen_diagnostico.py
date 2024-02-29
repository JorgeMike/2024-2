from scipy.stats import norm

# Para un nivel de significancia de 0.05, calculamos el cuantil para 1 - alpha/2 = 0.975
alpha = 0.05
quantile_value = norm.ppf(1 - alpha / 2)

print(quantile_value)
