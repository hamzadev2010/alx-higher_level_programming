#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer data
 * @next: points to the next node
 *
 * Description: Definition of a singly linked list node structure
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
 * Return: The number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint - Adds a new node to the beginning of a linked list.
 * @head: A pointer to the pointer to the head of the list.
 * @n: The integer data to be stored in the new node.
 * Return: A pointer to the newly created node.
 */
listint_t *add_nodeint(listint_t **head, const int n);

/**
 * free_listint - Frees the memory allocated for a linked list.
 * @head: A pointer to the head of the list.
 */
void free_listint(listint_t *head);

/**
 * check_cycle - Checks if a linked list contains a cycle.
 * @list: A pointer to the head of the list.
 * Return: 1 if a cycle is present, 0 otherwise.
 */
int check_cycle(listint_t *list);

#endif /* LISTS_H */
