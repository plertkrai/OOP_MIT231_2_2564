# Recursion Function

def tri_recursion(k):
    if k >0:
        result = k + tri_recursion(k-1)
        print(result)
    else:
        result =0
    return result

# calling funciton
tri_recursion(10)

