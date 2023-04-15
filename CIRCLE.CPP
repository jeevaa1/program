#include<graphics.h>
#include<conio.h>
int main()
{
int gdriver = DETECT, gmode;
int x=200,y=200,x_r=100,y_r=60;
int start_angle=80,end_angle=40;
initgraph(&gdriver,&gmode,"C:\\Turboc3\\BGI");
ellipse(x,y,start_angle,end_angle,x_r,y_r);
getch();
closegraph();
return 0;
}