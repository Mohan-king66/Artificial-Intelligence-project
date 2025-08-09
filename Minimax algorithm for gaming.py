class N:
    def __init__(s,v=0,l=None,r=None): s.v,v; s.l,l; s.r,r
    def __init__(s,v=0,l=None,r=None): s.v,s.l,s.r=v,l,r
root=N(0,N(3),N(0,N(0,N(-3)),N(0,None,N(4))))
def mm(n,maxp=True):
    if not n.l and not n.r: return n.v
    f=max if maxp else min
    return f(mm(n.l,not maxp) if n.l else -1e9 if maxp else 1e9,
             mm(n.r,not maxp) if n.r else -1e9 if maxp else 1e9)
L,R=mm(root.l,0),mm(root.r,0)
print("Minimax value at root:",mm(root,1))
print("Chosen child at root:","left" if L>=R else "right")
print("Left child value:",L," Right child value:",R)
