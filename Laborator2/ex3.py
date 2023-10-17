def list_opp(a,b):
    intersection=list(set(a) & set(b))
    union=list(set(a)|set(b))
    A_diff_B=list(set(a)-set(b))
    B_diff_A=list(set(b)-set(a))
    return intersection,union,A_diff_B,B_diff_A

a=[22,33,40,55,63,71]
b=[22,21,56,98,44,63]
opp=list_opp(a,b)
print("A inter B =",opp[0])
print("A u B =",opp[1])
print("A \ B =",opp[2])
print("B \ A =",opp[3])
     