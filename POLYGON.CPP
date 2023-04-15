#include<graphics.h>
#include<stdio.h>
#include<conio.h>
int main()
{
int gdriver= DETECT, gmode;
initgraph(&gdriver,&gmode,"C:\\Turboc3\\BGI");
printf("Before Cliping..");
rectangle(100,100,300,300);
line(150,150,450,150);
line(150,150,300,300);
line(450,150,300,300);
getch();
cleardevice();
//after
printf("After Clipping..");
rectangle(100,100,300,300);
line(150,150,300,150);
line(150,150,300,300);
//line(450,150,300,300);
getch();
closegraph();
return 0;
}
