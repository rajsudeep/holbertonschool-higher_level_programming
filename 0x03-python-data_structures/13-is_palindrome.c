#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: reference to a singly linked list of integers
 *
 * Return: If list is a palindrome 1, if not 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int arr[2056];
	int i, j, k;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	for (i = 0; tmp != NULL; i++, tmp = tmp->next)
		arr[i] = tmp->n;
	j = (--i / 2) +1;
	tmp = *head;
	for (k = 0; k <= j; k++, i--, tmp = tmp->next)
		if (tmp->n != arr[i])
			return (0);
	return (1);
}
