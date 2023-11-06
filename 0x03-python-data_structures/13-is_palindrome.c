#include "lists.h"

/**
  * is_palindrome - Checks if the linkedlist is palidrome
  * @head: The linked list to be checked
  *
  * Return: 1 if a palindrome, otherwise 0
  */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int nodeCount, i, j;

	temp = *head;
	nodeCount = 0;

	while (temp != NULL)
	{
		nodeCount++;
		temp = temp->next;
	}

	int arr[nodeCount];

	temp = *head;

	for (i = 0; i < nodeCount; i++)
	{
		arr[i] = temp->n;
		temp = temp->next;
	}

	for (i = 0, j = nodeCount - 1; i < j; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}

	return (1);
}
