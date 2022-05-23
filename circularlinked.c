#include<stdio.h>
#include<stdlib.h>
struct me{
    int val;
    struct me *next;
};
int main(){
    struct me *head,*t,*n;
    int k;
    scanf("%d",&k);
    head=0;
    while(k--)
    {
        t=(struct me*)malloc(sizeof(struct me));
        printf("Enter the elements:");
        scanf("%d",&t->val);
        t->next=0;
        if (head==0)
        {
            head=n=t;
        }
        else{
            n->next=t;
            n=t;
        }
    }
    n->next=head;
    t=head;
    printf("The first value is:");
    printf("%d\n",t->val);
    while(t->next!=head)
    {
        printf("\tThe value is:\n");
        printf("%d\t",t->val);
        t=t->next;
    }
    // printf("%d",t->val);
    // printf("\n%d\n",n->next);
    // printf("%d",head);
    return 0;
}