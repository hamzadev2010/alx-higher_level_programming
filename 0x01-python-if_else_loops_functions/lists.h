#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>

/**
 * struct listint_s - singly linked list
 * @n: Integer data
 * @next: Points to the next node
 *
 * Description: Defines a singly linked list node structure
 * for a Holberton project.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * print_listint - Prints the elements of a linked list.
 * @h: A pointer to the head of the list.
 *
 * Return: The number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - Adds a new node at the end of a linked list.
 * @head: A pointer to the pointer to the head of the list.
 * @n: The integer data to be stored in the new node.
 *
 * Return: A pointer to the newly created node.
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - Frees the memory allocated for a linked list.
 * @head: A pointer to the head of the list.
 */
void free_listint(listint_t *head);

/**
 * insert_node - Inserts a new node into a sorted linked list.
 * @head: A pointer to the pointer to the head of the list.
 * @number: The integer data to be stored in the new node.
 *
 * Return: A pointer to the newly created node.
 */
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
