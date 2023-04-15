#include<stdio.h>
#include<conio.h>
#include<math.h>
#define MAX(a,b)(a>b?a:b)
#define MIN(a,b)(a<b?a:b)
void rgbtohsv(float r,float g,float b,float *h,float *s,float *v)
{
float max = MAX(r,(g,b));
float min = MIN(r,MIN(g,b));
float delta= max - min;
*v=max;
if(max!=0.0) {
*s=delta/max;
if(r==max)
*h=(g-b)/delta;
else if(g==max)
*h=2+(b-r)/delta;
else if(b==max)
*h=4+(b-r)/delta;
*h*=60.0; if(*h<0)
*h+=360.0;
*h/=360.0;
}
}
void main()
{
float r,g,b,h=0,s=0,v=0;
clrscr();
printf("Enter the value of R,G,B\n:");
scanf("%f%f%f",&r,&g,&b);
rgbtohsv(r,g,b,&h,&s,&v); printf("H=%f, S=%f ,V=%f",h,s,v);
getch(); }