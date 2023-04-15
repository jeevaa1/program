#include<graphics.h>
#include<stdio.h>
#include<conio.h>
int main()
{
int gdriver = DETECT,gmode;
initgraph(&gdriver,&gmode,"C:\\Turboc3\\BGI");
printf("Window mode..");
rectangle(150,150,450,350);
line(400,300,300,200);
line(200,300,300,200);
line(400,300,200,300);
getch();
cleardevice();
printf("view port..");
rectangle(100,160,550,320);
line(400,300,320,220);
line(200,300,320,220);
line(400,300,200,300);
getch();
closegraph();
return 0;
}
