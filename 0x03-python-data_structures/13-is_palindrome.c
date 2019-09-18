#include "lists.h"
#include <stdio.h>

/**
 * _is_palindrome - compares the head and tail of a list
 * @head: reference to a singly linked list of integers
 * @tail: singly linked list of integers
 *
 * Return: If list is a palindrome 1, if not 0
 */
int _is_palindrome(listint_t **head, listint_t *tail)
{
	if (tail == NULL || (*head)->n == tail->n)
		return (1);
	if ((_is_palindrome(head, tail->next)) == 1)
		return (0);

	if ((*head)->n != tail->n)
		return (0);
	*head = (*head)->next;

	return (1);
}

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: reference to a singly linked list of integers
 *
 * Return: If list is a palindrome 1, if not 0
 */
int is_palindrome(listint_t **head)
{
	return (_is_palindrome(head, *head));
}
