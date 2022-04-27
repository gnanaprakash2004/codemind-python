def compound_interest(principle, rate, time):
 
    # Calculates compound interest
    Amount = principle * (pow((1 + rate / 100), time))
  
    print("%0.2f" %Amount)
p,r,t=map(int,input().split())
compound_interest(p,r,t)