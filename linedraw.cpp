#include <conio.h>
#include <graphics.h>
int main()
{
int gdriver = DETECT, gmode;
initgraph(&gdriver, &gmode, "C:\\Turboc3\\BGI");
line(100,200,300,400);
getch();
closegraph();
return 0;
}