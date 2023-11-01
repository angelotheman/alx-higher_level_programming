#include "lists.h"
#include <stdlib.h>

/**
  * insert_node - Inserts a node in a position of the linkedlist
  * @head: the linked list
  * @number: Data to insert
  *
  * Return: New node or NULL if otherwise
  */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new_node;

	curr = *head;
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	while (curr->next != NULL && number > curr->next->n)
		curr = curr->next;

	new_node->next = curr->next;
	curr->next = new_node;

	return (new_node);
}
