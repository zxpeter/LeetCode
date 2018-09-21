#RT:RightTop
#LB:LeftBottom
def IOU(rectangle A, rectangleB):
    W = min(A.RT.x, B.RT.x) - max(A.LB.x, B.LB.x)
    H = min(A.RT.y, B.RT.y) - max(A.LB.y, B.LB.y)
    if W <= 0 or H <= 0:
        return 0;
    SA = (A.RT.x - A.LB.x) * (A.RT.y - A.LB.y)
    SB = (B.RT.x - B.LB.x) * (B.RT.y - B.LB.y)
    cross = W * H
    return cross/(SA + SB - cross)

边界条件
if min(A.RT.x, B.RT.x) >= max(A.LB.x, B.LB.x) and min(A.RT.y, B.RT.y) >= max(A.LB.y, B.LB.y) 
当两个矩形相交

---------------------

两个矩形相交的条件:两个矩形的重心距离在X和Y轴上都小于两个矩形长或宽的一半之和.这样,分两次判断一下就行了.
bool CrossLine(Rect r1,RECT r2)
{
  if(abs((r1.x1+r1.x2)/2-(r2.x1+r2.x2)/2)<((r1.x2+r2.x2-r1.x1-r2.x1)/2) && abs((r1.y1+r1.y2)/2-(r2.y1+r2.y2)/2)<((r1.y2+r2.y2-r1.y1-r2.y1)/2))
    return true;
  return false;
}
