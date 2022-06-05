#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
void reverse(listint_t **head);
int compareList(listint_t *head, listint_t *new);
void reverse(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *current = *head, *nex_t;
  while (current != NULL)
    {
      nex_t = current->next;
      current->next = prev;
      prev = current;
      current = nex_t;
    }
  *head = prev;
}

int compareList(listint_t *head, listint_t *new)
{
  listint_t *temp1 = head;
  listint_t *temp2 = new;
  while (temp1 != NULL && temp2 != NULL)
    {
      if (temp1->n == temp2->n)
	{
	  temp1 = temp1->next;
	  temp2 = temp2->next;
	}
      else
	return (0);
    }
  if (temp1 == NULL && temp2 == NULL)
    return (1);
  return (0);
}
	  

int is_palindrome(listint_t **head)
{
  int res = 1;
  listint_t *slow = *head, *prv_slow = *head, *sec_half;
  listint_t *fast = *head, *mid = NULL;

  if (*head != NULL && (*head)->next != NULL)
    {
      while (fast != NULL && fast->next != NULL)
	{
	  fast = fast->next->next;
	  prv_slow = slow;
	  slow = slow->next;
	}
      if (fast != NULL)
	{
	  mid = slow;
	  slow = slow->next;
	}
      sec_half = slow;

      prv_slow->next = NULL;
      reverse(&sec_half);
      res = compareList(*head, sec_half);

      /*reverse(&sec_half);*/

      if (mid != NULL)
	{
	  prv_slow->next = mid;
	  mid->next = sec_half;
	}
      else
	prv_slow->next = sec_half;
    }
  return (res);
}
