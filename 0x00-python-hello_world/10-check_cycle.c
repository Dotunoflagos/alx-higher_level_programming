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
        if (current == current2)
            return 1;
        current = current->next;
        current2 = current->next;
    }
            return 0;
}
