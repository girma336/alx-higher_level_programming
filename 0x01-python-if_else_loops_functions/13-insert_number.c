#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new, *prv;
  prv = *head;
  new = malloc(sizeof(listint_t));
  if (new == 0)
    return (NULL);
  
  new->n = number;
  new->next = NULL;

  if (*head == NULL)
    {
      (*head) = new;
      return (*head);
    }
  if ((*head)->n >= number)
    {
      new->next = *head;
      *head = new;
      return (*head);
    }

  while(prv)
    {
      if (prv->n >= number)
	{
	  new->next = prv;
	  prv = new;
	  return (prv);
	}
      else if (prv->n < number && prv->next->n > number)
	{
	  new->next = prv->next;
	  prv->next = new;
	  return (prv);
	}
      else if (prv->next == NULL)
	{
	  prv->next = new;
	  return (prv);
	}
      prv = prv->next;
   if (prv->next == NULL && prv->n <= number)
    {
      prv->next = new;
      return (prv);
    }
    }
  return (*head);
}
	       
