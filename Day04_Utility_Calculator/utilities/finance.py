def simple_interest(p, r, t):
    return (p * r * t) / 100

def emi(principal, rate, time):
    monthly_rate = rate / (12 * 100)
    months = time * 12
    return principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)