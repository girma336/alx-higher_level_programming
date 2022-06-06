#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
void reverse(listint_t **head);
int compareList(listint_t *head, listint_t *new);
void reverse(listint_t **head)
{
  listint_t *new;
    listint_t *new2;
  listint_t *new3 = NULL;
  new = *head;
  
  while (new != NULL)
    {
      new2 = new->next;
      new->next = new3;
      new3 = new;
      new = new2;
    }
  *head = new3;
}
  
int compareList(listint_t *head, listint_t *new)
{
  listint_t *t1 = head;
  listint_t *t2 = new;
  while (t1 != NULL && t2 != NULL)
    {
      if (t1->n == t2->n)
	{
	  t1 = t1->next;
	  t2 = t2->next;
	}
      else
	return (0);
    }
  if (t1 == NULL && t2 == NULL)
    return (1);

      return(0);
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
      prv_slow->next = NULL;
      sec_half = slow;
      reverse(&sec_half);
      res = compareList(*head, sec_half);

      /**reverse(sec_half);**/


      if (mid != NULL)
	{
	  prv_slow->next = mid;
	  mid->next = sec_half;
	}
      else
	prv_slow->next = sec_half;
    }
  return res;
}


      
      

 
