def fip(ind):
    if ind <= 1:
        return ind
    else:
        return fip(ind-1) + fip(ind-2)
    
print(fip(3))