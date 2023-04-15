#include<graphics.h>
#include<stdio.h>
#include<conio.h>
int main()
{
int gdriver = DETECT,gmode;
initgraph(&gdriver,&gmode,"C:\\Turboc3\\BGI");
// line clip before
printf("Before line Cliping...");
line(100,200,300,300);
rectangle(150,150,350,350);
getch();
cleardevice();
//end
printf("after line cliping");
line(150,200,300,300);
rectangle(150,150,350,350);
getch();
closegraph();
return 0;
}
