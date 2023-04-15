#include<stdio.h>
#include<graphics.h>
#include<conio.h>
int main()
{
int gdriver = DETECT, gmode;
int L,R,T,B; // sides Left,Right..ect..
initgraph(&gdriver,&gmode,"C:\\Turboc3\\BGI");
// traslation
L=150;
T=150;
R=450;
B=450;
cleardevice();
printf("orginal..");
rectangle(100,100,350,350);
getch();
cleardevice();
//traslation
printf("translation..");
rectangle(200,200,350,350);
getch();
cleardevice();
// scale
printf("Scalled..");
rectangle(200,200,50,50);
getch();
cleardevice();
return 0;
// im trying but rotation and along everthigs making its complex,,,
}
