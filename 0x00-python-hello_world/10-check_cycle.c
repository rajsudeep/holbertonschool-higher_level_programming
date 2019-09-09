#include "lists.h"

/**
 * _find_listint_loop - finds the start of the loop
 * @head: pointer to the list with a loop
 * @marker: marked node where loop was certified
 *
 * Return: Address of the node where the loop starts
 */
listint_t *_find_listint_loop(listint_t *head, listint_t *marker)
{
	listint_t *curr = head;

	while (curr != marker)
	{
		curr = curr->next;
		marker = marker->next;
	}
	return (curr);
}

/**
 * find_listint_loop - detects for a loop in a list
 * @head: pointer to a list of numbers
 *
 * Return: Address of the node where loop starts
 * NULL if no loop exists
 */
listint_t *find_listint_loop(listint_t *head)
{
	listint_t *marker = head, *next = head;

	while (marker != NULL && next != NULL && next->next != NULL)
	{
		marker = marker->next;
		next = next->next->next;
		if (marker == next)
			return (_find_listint_loop(head, marker));
	}
	return (NULL);
}

/**
 * check_cycle - check if singly linked list has a cycle
 * @list: linked list to check in
 *
 * Return: 0 if there is none, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	if (find_listint_loop(list) == NULL)
		return (0);
	else
		return (1);
}
