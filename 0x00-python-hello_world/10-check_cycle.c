#include "lists.h"

/**
  * check_cycle - Checks if a singly linked list has cycle
  * @list: Pointer to the head
  *
  * Return: 0 if no cycle and 1 if there is a cycle
  */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;

	while (slow != NULL && fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
