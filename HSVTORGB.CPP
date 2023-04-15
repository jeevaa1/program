#include<stdio.h> 
#include<math.h>
#include<conio.h>
void hsvtorgb(float h,float s,float v,float *r,float *g,float *b)
{
int i; float aa,bb,cc,f; if(s==0)
*r=*g=*b=v; else { if(h==1.0)
h=0; h*=6.0; i=floor(h); f=h-i;
aa=v*(1-s); bb=v*(1-(s*f));
cc=v*(1-(s*(1-f))); switch(i) {
case 0: *r=v; *g=cc; *b=aa; break;
case 1: *r=bb; *g=v; *b=aa; break;
case 2: *r=aa; *g=v; *b=cc; break;
case 3: *r=aa; *g=bb; *b=v; break;
case 4: *r=cc; *g=aa; *b=v; break;
case 5: *r=v; *g=aa; *b=bb; break;
}
} } void
main() {
float h,s,v,r=0,g=0,b=0;
clrscr();
printf("Enter the H,S,V values:\n");
scanf("%f%f%f",&h,&s,&v);
hsvtorgb(h,s,v,&r,&g,&b); printf("The R,G,B values:\n%f %f %f\n",r,g,b);
getch(); }