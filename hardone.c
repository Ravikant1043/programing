#include <stdio.h>
int main()
{
    int n, t, i, j,k=1,o;
    scanf("%d", &n);
    t = n * 2 - 1;
    o=t;
    int a[t][t];
    while (n >= 1)
    {
        for (i = k; i <= t; i++)
        {
            for (j = k; j <= t; j++)
            {
                if (i == k || j == k || i == t || j == t)
                a[i][j]=n;
                // printf("%d", n);
            }
        }
        k++;t--;n--;
    }
    for(i=1;i<=o;i++)
    {
        for(j=1;j<=o;j++)
        {
            printf("%d",a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
