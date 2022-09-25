#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
int check_cycle(listint_t *list)
{
    listint_t *current;
    listint_t *current2;

    current = list;
    while (current != NULL)
    {
        current = current->next;
        while (current2 != NULL)
        {
            current2 = current->next;
            if (current == current2)
                return 1;
        }
    }
    return 0;
}