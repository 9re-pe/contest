ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())

# f(x,y)=0形式の直線の方程式は、イルカのジャンプで求めた式を変形すれば求められる
def f_ac(x, y):
    """
    A,Cを通る直線の方程式
    f(X, Y) = (cy - ay)X - (cx - ax)Y + (cx - ax)ay - (cy - ay)ax
    """
    return (cy - ay)*x - (cx - ax)*y + (cx - ax)*ay - (cy - ay)*ax


def f_bc(x, y):
    """
    B,Dを通る直線の方程式
    f(X, Y) = (dy - by)X - (dx - bx)Y + (dx - bx)by - (dy - by)bx
    """
    return (dy - by)*x - (dx - bx)*y + (dx - bx)*by - (dy - by)*bx


"""
四角形が凸
⇔ 対角線が交わる
⇔ 2本の対角線について、対角線に使われない2点が対角線を延長した直線の異なる側にある

(x1, y1), (x2, y2)が直線f(x, y)=0の異なる側にある
⇔ f(x1, y1)とf(x2, y2)の符号が異なる
"""
if f_ac(bx, by) * f_ac(dx, dy) < 0 and f_bc(ax, ay) * f_bc(cx, cy) < 0:
    print('Yes')
else:
    print('No')

