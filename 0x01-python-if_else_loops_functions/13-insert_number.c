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

  if (head == NULL || *head == NULL)
    {
      new->next = *head;
      (*head) = new;
      return (*head);
    }
   
  while(prv)
    {
      if (prv->n > number)
	{
	  new->next = prv;
	  prv = new;
	  return (*head);
	}
      if (prv->n < number && prv->next->n > number)
	{
	  new->next = prv->next;
	  prv->next = new;
	  return (prv);
	}
      if (prv->next == NULL)
	{
	  new->next = NULL;
	  prv->next = new;
	  return (prv);
	}
      prv = prv->next;
    }
  return (*head);
}
	       
