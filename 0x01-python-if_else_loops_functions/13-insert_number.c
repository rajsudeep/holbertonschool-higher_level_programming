#include "lists.h"

/**
 * insert_node - inserts a number into a sorted list
 * @head: sorted list
 * @number: number to add in list
 *
 * Return: address of the new node, NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next != NULL &&
	       current->next->n < new->n)
		current = current->next;
	new->next = current->next;
	current->next = new;

	return (new);
}
