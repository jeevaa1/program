#include<stdio.h> 
#include<conio.h> 
#include<graphics.h> 
#include<math.h> 
void main() 
{ 
int n,poly[20],poly1[20],poly2[10],sx,poly3[10];
int tx,ty,xr,yr,a,sy,poly4[10],poly5[10],poly6[10],poly7[10]; int i;
int gd=DETECT,gm; 
initgraph(&gd,&gm," "); 
//STEP TO DRAW A POLYGAN 
printf("\nEnter the number of vertices of the polygan.....\n"); scanf("%d",&n); 
printf("\nEnter the X,Y co-ordinates of each vertex....\n"); for(i=0;i<2*n;i++) 
{ scanf("%d",&poly[i]); 
poly[i]=(poly[i])+40; 
poly[i+1]=(poly[i+1])+40; 
poly1[i]=(poly[i]+50)+40; 
poly1[i+1]=(poly[i+1]+50)+40; 
} poly[2*n]=poly[0]; 
poly[2*n+1]=poly[1]; 
poly1[2*n]=poly1[0]; 
poly1[2*n+1]=poly1[1]; 
outtextxy(70,70,"ORIGINAL IMAGE"); 
drawpoly(n+1,poly); 
drawpoly(n+1,poly1); for(i=0;i<2*n;i+=2) 
line(poly[i],poly[i+1],poly1[i],poly1[i+1]); 
getch(); cleardevice(); 
//TRANSLATION 
outtextxy(30,30,"ORIGINAL IMAGE"); 
drawpoly(n+1,poly); 
drawpoly(n+1,poly1); for(i=0;i<2*n;i+=2) 
line(poly[i],poly[i+1],poly1[i],poly1[i+1]); 
getch(); 
outtextxy(10,10,"Enter the Translation factor:"); gotoxy(30,3); 
scanf("%d%d",&tx,&ty); 
for(i=0;i<2*n;i+=2) 
{ poly2[i]=poly[i]+tx; 
poly2[i+1]=poly[i+1]+ty; 
poly3[i]=poly1[i]+tx; 
poly3[i+1]=poly1[i+1]+ty
; 
} 
poly2[2*n]=poly2[0]; 
poly2[2*n+1]=poly2[1]; 
poly3[2*n]=poly3[0]; 
poly3[2*n+1]=poly3[1]; 
drawpoly(n+1,poly2); drawpoly(n+1,poly3); 
for(i=0;i<2*n;i+=2) 
line(poly2[i],poly2[i+1],poly3[i],poly3[i+1]);
getch(); cleardevice(); 
//SCALING 
printf("\n\n\t original image!"); 
drawpoly(n+1,poly); 
drawpoly(n+1,poly1); gotoxy(300,100); 
for(i=0;i<2*n;i+=2) 
line(poly[i],poly[i+1],poly1[i],poly1[i+1]); 
getch(); 
outtextxy(10,10,"Enter the scaling factor:"); 
gotoxy(30,3); scanf("%d",&sx); 
for(i=0;i<2*n;i+=2) { poly4[i]=poly[i]*sx; 
poly4[i+1]=poly[i+1]*sx; 
poly5[i]=poly1[i]*sx; 
poly5[i+1]=poly1[i+1]*sx; 
} poly4[2*n]=poly4[0]; 
poly4[2*n+1]=poly4[1]; 
poly5[2*n]=poly5[0]; 
poly5[2*n+1]=poly5[1]; 
drawpoly(n+1,poly4); drawpoly(n+1,poly5); 
for(i=0;i<2*n;i+=2) 
line(poly4[i],poly4[i+1],poly5[i],poly5[i+1]); 
getch(); cleardevice(); 
//ROTATION 
printf("\n\n\t original image!"); 
drawpoly(n+1,poly); 
drawpoly(n+1,poly1); for(i=0;i<2*n;i+=2) 
line(poly[i],poly[i+1],poly1[i],poly1[i+1]); 
getch(); 
outtextxy(10,10,"Enter the rotation factor"); gotoxy(30,3); 
scanf("%d%d%d",&xr,&yr,&a); 
for(i=0;i<2*n;i+=2) 
{ poly6[i]=xr+((poly[i]-xr)*cos(a))-((poly[i+1]-yr)*sin(a))+70; 
poly6[i+1]=yr+((poly[i+1]-yr)*cos(a))+((poly[i]-xr)*sin(a))+70; 
poly7[i]=xr+((poly[i]-xr)*cos(a))-((poly1[i+1]-yr)*sin(a))+70; 
poly7[i+1]=yr+((poly[i+1]-yr)*cos(a))+((poly1[i]-xr)*sin(a))+70; 
} 
poly6[2*n]=poly6[0]; 
poly6[2*n+1]=poly6[1]; 
poly7[2*n]=poly7[0]; 
poly7[2*n+1]=poly7[1]; 
drawpoly(n+1,poly6); 
drawpoly(n+1,poly7); for(i=0;i<2*n;i+=2) 
line(poly6[i],poly6[i+1],poly7[i],poly7[i+1]);
getch(); cleardevice(); }
    