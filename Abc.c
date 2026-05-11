#include<stdio.h>

#include<stdlib.h>



struct node

{

    int data;

    struct node *next;

};



struct node *head = NULL;



/* Function Declarations */

void insertFront(int num);

void insertEnd(int num);

void insertAfter(int key, int num);

void insertBefore(int key, int num);



void deleteFirst();

void deleteLast();

void deleteAfter(int key);

void deleteBefore(int key);



void display();

void countNodes();

void searchNode(int n);



int main()

{

    int ch, num, key;



    while(1)

    {

        printf("\n===== MENU =====\n");

        printf("1. Insert at Front\n");

        printf("2. Display\n");

        printf("3. Insert at End\n");

        printf("4. Count No. of Nodes\n");

        printf("5. Search a Number\n");

        printf("6. Insert After a Given Node\n");

        printf("7. Insert Before a Given Node\n");

        printf("8. Delete First Node\n");

        printf("9. Delete Last Node\n");

        printf("10. Delete After a Given Node\n");

        printf("11. Delete Before a Given Node\n");

        printf("12. Exit\n");



        printf("Enter Choice: ");

        scanf("%d", &ch);



        switch(ch)

        {

            case 1:

                printf("Enter Number to Insert at Front: ");

                scanf("%d", &num);

                insertFront(num);

                break;



            case 2:

                display();

                break;



            case 3:

                printf("Enter Number to Insert at End: ");

                scanf("%d", &num);

                insertEnd(num);

                break;



            case 4:

                countNodes();

                break;



            case 5:

                printf("Enter Number to Search: ");

                scanf("%d", &num);

                searchNode(num);

                break;



            case 6:

                printf("Enter Node Value After Which to Insert: ");

                scanf("%d", &key);



                printf("Enter New Number: ");

                scanf("%d", &num);



                insertAfter(key, num);

                break;



            case 7:

                printf("Enter Node Value Before Which to Insert: ");

                scanf("%d", &key);



                printf("Enter New Number: ");

                scanf("%d", &num);



                insertBefore(key, num);

                break;



            case 8:

                deleteFirst();

                break;



            case 9:

                deleteLast();

                break;



            case 10:

                printf("Enter Node Value After Which to Delete: ");

                scanf("%d", &key);



                deleteAfter(key);

                break;



            case 11:

                printf("Enter Node Value Before Which to Delete: ");

                scanf("%d", &key);



                deleteBefore(key);

                break;



            case 12:

                exit(0);



            default:

                printf("Invalid Choice\n");

        }

    }

}



/* Insert at Front */

void insertFront(int num)

{

    struct node *newnode;



    newnode = (struct node*) malloc(sizeof(struct node));



    newnode->data = num;

    newnode->next = head;



    head = newnode;



    printf("Node Inserted at Front\n");

}



/* Insert at End */

void insertEnd(int num)

{

    struct node *newnode, *p;



    newnode = (struct node*) malloc(sizeof(struct node));



    newnode->data = num;

    newnode->next = NULL;



    if(head == NULL)

    {

        head = newnode;

    }

    else

    {

        p = head;



        while(p->next != NULL)

        {

            p = p->next;

        }



        p->next = newnode;

    }



    printf("Node Inserted at End\n");

}



/* Insert After */

void insertAfter(int key, int num)

{

    struct node *p, *newnode;



    p = head;



    while(p != NULL && p->data != key)

    {

        p = p->next;

    }



    if(p == NULL)

    {

        printf("Given Node Not Found\n");

        return;

    }



    newnode = (struct node*) malloc(sizeof(struct node));



    newnode->data = num;

    newnode->next = p->next;



    p->next = newnode;



    printf("Node Inserted After %d\n", key);

}



/* Insert Before */

void insertBefore(int key, int num)

{

    struct node *p, *prev, *newnode;



    if(head == NULL)

    {

        printf("List Empty\n");

        return;

    }



    if(head->data == key)

    {

        insertFront(num);

        return;

    }



    p = head;

    prev = NULL;



    while(p != NULL && p->data != key)

    {

        prev = p;

        p = p->next;

    }



    if(p == NULL)

    {

        printf("Given Node Not Found\n");

        return;

    }



    newnode = (struct node*) malloc(sizeof(struct node));



    newnode->data = num;

    newnode->next = p;



    prev->next = newnode;



    printf("Node Inserted Before %d\n", key);

}



/* Delete First */

void deleteFirst()

{

    struct node *temp;



    if(head == NULL)

    {

        printf("List Empty\n");

        return;

    }



    temp = head;

    head = head->next;



    printf("Deleted Node = %d\n", temp->data);



    free(temp);

}



/* Delete Last */

void deleteLast()

{

    struct node *p, *prev;



    if(head == NULL)

    {

        printf("List Empty\n");

        return;

    }



    if(head->next == NULL)

    {

        printf("Deleted Node = %d\n", head->data);



        free(head);

        head = NULL;



        return;

    }



    p = head;

    prev = NULL;



    while(p->next != NULL)

    {

        prev = p;

        p = p->next;

    }



    prev->next = NULL;



    printf("Deleted Node = %d\n", p->data);



    free(p);

}



/* Delete After a Given Node */

void deleteAfter(int key)

{

    struct node *p, *temp;



    if(head == NULL)

    {

        printf("List Empty\n");

        return;

    }



    p = head;



    while(p != NULL && p->data != key)

    {

        p = p->next;

    }



    if(p == NULL)

    {

        printf("Given Node Not Found\n");

        return;

    }



    if(p->next == NULL)

    {

        printf("No Node Exists After %d\n", key);

        return;

    }



    temp = p->next;



    p->next = temp->next;



    printf("Deleted Node = %d\n", temp->data);



    free(temp);

}



/* Delete Before a Given Node */

void deleteBefore(int key)

{

    struct node *p, *prev, *temp;



    if(head == NULL || head->next == NULL)

    {

        printf("Not Enough Nodes\n");

        return;

    }



    /* Delete first node */

    if(head->next->data == key)

    {

        deleteFirst();

        return;

    }



    prev = head;

    temp = head->next;

    p = head->next->next;



    while(p != NULL && p->data != key)

    {

        prev = temp;

        temp = p;

        p = p->next;

    }



    if(p == NULL)

    {

        printf("Given Node Not Found\n");

        return;

    }



    prev->next = p;



    printf("Deleted Node = %d\n", temp->data);



    free(temp);

}



/* Display */

void display()

{

    struct node *p;



    p = head;



    if(head == NULL)

    {

        printf("List Empty\n");

    }

    else

    {

        printf("Linked List: ");



        while(p != NULL)

        {

            printf("%d ", p->data);

            p = p->next;

        }



        printf("NULL\n");

    }

}



/* Count Nodes */

void countNodes()

{

    struct node *p;

    int cnt = 0;



    p = head;



    while(p != NULL)

    {

        cnt++;

        p = p->next;

    }



    printf("Total Number of Nodes = %d\n", cnt);

}



/* Search */

void searchNode(int n)

{

    struct node *p;



    p = head;



    while(p != NULL)

    {

        if(p->data == n)

        {

            printf("Number Found in the List\n");

            return;

        }



        p = p->next;

    }



    printf("Number Not Found in the List\n");

}

