#include<stdio.h>
#include<stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *head = NULL;

void insert_front();
void insert_last();
void insert_before(int val);
void insert_after(int val);
void delete_first();
void delete_last();
void delete_before(int val);
void delete_after(int val);
void delete_node(int val);
void display();
int count();
void search(int val);
void reverse();

void insert_front()
{
    struct node *newnode;
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d",&newnode->data);

    if(head==NULL)
    {
        newnode->next=NULL;
        head=newnode;
    }
    else
    {
        newnode->next=head;
        head=newnode;
    }
}

void insert_last()
{
    struct node *newnode,*p;
    newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d",&newnode->data);
    newnode->next=NULL;

    if(head==NULL)
    {
        head=newnode;
    }
    else
    {
        p=head;
        while(p->next!=NULL)
            p=p->next;
        p->next=newnode;
    }
}

void insert_before(int val)
{
    struct node *newnode,*p,*q;
    if(head==NULL){ printf("List is empty\n"); return; }

    newnode=(struct node*)malloc(sizeof(struct node));
    printf("Enter data: ");
    scanf("%d",&newnode->data);

    if(head->data==val)
    {
        newnode->next=head;
        head=newnode;
    }
    else
    {
        p=head; q=NULL;
        while(p!=NULL && p->data!=val)
        {
            q=p; p=p->next;
        }

        if(p==NULL) printf("Value not found\n");
        else
        {
            q->next=newnode;
            newnode->next=p;
        }
    }
}

void insert_after(int val)
{
    struct node *newnode,*p;

    if(head==NULL){ printf("List is empty\n"); return; }

    p=head;
    while(p!=NULL && p->data!=val)
        p=p->next;

    if(p==NULL) printf("Value not found\n");
    else
    {
        newnode=(struct node*)malloc(sizeof(struct node));
        printf("Enter data: ");
        scanf("%d",&newnode->data);

        newnode->next=p->next;
        p->next=newnode;
    }
}

void delete_first()
{
    if(head==NULL)
        printf("List is empty\n");
    else
        head=head->next;
}

void delete_last()
{
    struct node *p;

    if(head==NULL)
        printf("List is empty\n");
    else if(head->next==NULL)
        head=NULL;
    else
    {
        p=head;
        while(p->next->next!=NULL)
            p=p->next;
        p->next=NULL;
    }
}

void delete_before(int val)
{
    struct node *p,*q;

    if(head==NULL || head->next==NULL)
        printf("Not possible\n");
    else if(head->data==val)
        printf("No node before head\n");
    else
    {
        p=head; q=NULL;

        while(p->next!=NULL && p->next->data!=val)
        {
            q=p;
            p=p->next;
        }

        if(p->next==NULL)
            printf("Value not found\n");
        else if(q==NULL)
            head=p->next;
        else
            q->next=p->next;
    }
}

void delete_after(int val)
{
    struct node *p;

    if(head==NULL)
        printf("List is empty\n");
    else
    {
        p=head;

        while(p!=NULL && p->data!=val)
            p=p->next;

        if(p==NULL)
            printf("Value not found\n");
        else if(p->next==NULL)
            printf("No node after given value\n");
        else
            p->next=p->next->next;
    }
}

void delete_node(int val)
{
    struct node *p,*q;

    if(head==NULL)
        printf("List is empty\n");
    else if(head->data==val)
        head=head->next;
    else
    {
        p=head; q=NULL;

        while(p!=NULL && p->data!=val)
        {
            q=p; p=p->next;
        }

        if(p==NULL)
            printf("Value not found\n");
        else
            q->next=p->next;
    }
}

void display()
{
    struct node *p;

    if(head==NULL)
        printf("List is empty\n");
    else
    {
        p=head;
        while(p!=NULL)
        {
            printf("%d ",p->data);
            p=p->next;
        }
        printf("\n");
    }
}

int count()
{
    struct node *p;
    int c=0;

    p=head;
    while(p!=NULL)
    {
        c++;
        p=p->next;
    }
    return c;
}

void search(int val)
{
    struct node *p=head;

    while(p!=NULL && p->data!=val)
        p=p->next;

    if(p==NULL) printf("Value not found\n");
    else printf("Value found\n");
}

void reverse()
{
    struct node *prev,*curr,*next;

    prev=NULL;
    curr=head;

    while(curr!=NULL)
    {
        next=curr->next;
        curr->next=prev;
        prev=curr;
        curr=next;
    }

    head=prev;
}

int main()
{
    int ch,val;

    while(1)
    {
        printf("\n1.Insert Front");
        printf("\n2.Insert Last");
        printf("\n3.Insert Before");
        printf("\n4.Insert After");
        printf("\n5.Delete First");
        printf("\n6.Delete Last");
        printf("\n7.Delete Before");
        printf("\n8.Delete After");
        printf("\n9.Delete Node");
        printf("\n10.Display");
        printf("\n11.Count");
        printf("\n12.Search");
        printf("\n13.Reverse");
        printf("\n14.Exit");

        printf("\nEnter Choice: ");
        scanf("%d",&ch);

        switch(ch)
        {
            case 1: insert_front(); break;
            case 2: insert_last(); break;
            case 3:
                printf("Enter value: ");
                scanf("%d",&val);
                insert_before(val);
                break;
            case 4:
                printf("Enter value: ");
                scanf("%d",&val);
                insert_after(val);
                break;
            case 5: delete_first(); break;
            case 6: delete_last(); break;
            case 7:
                printf("Enter value: ");
                scanf("%d",&val);
                delete_before(val);
                break;
            case 8:
                printf("Enter value: ");
                scanf("%d",&val);
                delete_after(val);
                break;
            case 9:
                printf("Enter value: ");
                scanf("%d",&val);
                delete_node(val);
                break;
            case 10: display(); break;
            case 11: printf("Total Nodes = %d\n",count()); break;
            case 12:
                printf("Enter value: ");
                scanf("%d",&val);
                search(val);
                break;
            case 13: reverse(); break;
            case 14: exit(0);
            default: printf("Invalid Choice\n");
        }
    }
}
