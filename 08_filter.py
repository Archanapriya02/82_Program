# filter() function that returns even numbers from a list
def even(x):
    if x%2==0:
        return True
    else:
        return False
z=[int(x) for x in input().split()]
q = list(filter(even, z))
print("From the z the even values are:",q)