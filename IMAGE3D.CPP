#include<stdio.h>
#include<conio.h>
#include<graphics.h>
void top()
{
moveto(100,200); outtext("TOP VIEW");
line(400,200,440,150);
line(400,200,300,150);
line(300,150,340,100);
line(340,100,440,150);
}
void side()
{
moveto(100,200);outtext("SIDE VIEW");
rectangle(500,100,600,200);
}
void front(int wid)
{
moveto(100,200);outtext("FRONT VIEW");
rectangle(400,250,400+wid,350);
rectangle(300,250,400,350);
}
void main()
{
int x =DETECT,y,i,mx,my,wid=40;
initgraph(&x,&y,"");
mx=100;
my=100;
setfillstyle(USER_FILL,3);
moveto(100,250); outtext("3D IMAGE");
bar3d(mx,my,mx+100,my+100,wid,1);
getch();
cleardevice();
top(); getch();
cleardevice();
side();
getch();
cleardevice();
front(wid);
getch();
cleardevice();
bar3d(mx,my,mx+100,my+100,wid,1);
line(400,200,440,150);
line(400,200,300,150);
line(300,150,340,100);
line(340,100,440,150);
rectangle(500,100,600,200);
rectangle(400,250,400+wid,350);
rectangle(300,250,400,350);
getch();
closegraph();
}