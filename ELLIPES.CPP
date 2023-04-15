#include<graphics.h>
#include<conio.h>
#include<stdlib.h>
#include<stdio.h>
int main()
{
int gdriver = DETECT, gmode;
int x,y,r;
initgraph(&gdriver,&gmode,"C:\\Turboc3\\BGI");
setcolor(RED);
x=200;
y=200;
r=50;
circle(x,y,r);
getch();
closegraph();
return 0;
}