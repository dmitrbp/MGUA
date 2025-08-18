#include<stdio.h>

int main()
{
    int s = 0;
    int i = 1;
    loop:
        if (i < 11) {
            s += i;
            i += 1;
            goto loop;
        }
        else {
            printf("%i", s);
        }
}
