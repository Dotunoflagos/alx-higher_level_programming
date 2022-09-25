#include "lists.h"
/**
 * check_cycle -linked list cycle
 * @list: the pointer to the struct
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *current2 = list;

	if (list == NULL)
	{
		return (0);
	}

	current2 = current2->next;

	while (current != NULL && current2 != NULL && current2->next != NULL)
	{
		if (current2 == current)
		{
			return (1);
		}
		current2 = current2->next->next;
		current = current->next;
	}
	return (0);
}
