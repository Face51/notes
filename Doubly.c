#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *prev;
    struct Node *next;
};

struct Node *head = NULL;
struct Node *tail = NULL;

// Insert at beginning
void insertFront(int value)
{
    struct Node *newNode;

    newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->data = value;
    newNode->prev = NULL;
    newNode->next = head;

    if(head == NULL)
    {
        head = tail = newNode;
    }
    else
    {
        head->prev = newNode;
        head = newNode;
    }
}

// Insert at end
void insertEnd(int value)
{
    struct Node *newNode;

    newNode = (struct Node*)malloc(sizeof(struct Node));

    newNode->data = value;
    newNode->next = NULL;
    newNode->prev = tail;

    if(tail == NULL)
    {
        head = tail = newNode;
    }
    else
    {
        tail->next = newNode;
        tail = newNode;
    }
}

// Delete from beginning
void deleteFront()
{
    if(head == NULL)
    {
        printf("List is empty\n");
        return;
    }

    struct Node *temp = head;

    if(head == tail)
    {
        head = tail = NULL;
    }
    else
    {
        head = head->next;
        head->prev = NULL;
    }

    free(temp);
}

// Delete from end
void deleteEnd()
{
    if(tail == NULL)
    {
        printf("List is empty\n");
        return;
    }

    struct Node *temp = tail;

    if(head == tail)
    {
        head = tail = NULL;
    }
    else
    {
        tail = tail->prev;
        tail->next = NULL;
    }

    free(temp);
}

// Display forward
void displayForward()
{
    struct Node *temp = head;

    printf("Forward: ");

    while(temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }

    printf("\n");
}

// Display backward
void displayBackward()
{
    struct Node *temp = tail;

    printf("Backward: ");

    while(temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->prev;
    }

    printf("\n");
}

// Main function
int main()
{
    insertFront(20);
    insertFront(10);

    insertEnd(30);
    insertEnd(
