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

  if (head == NULL || *head == NULL)
    {
      (*head) = new;
      return (*head);
    }
   
  while(prv)
    {
      if (prv->n > number)
	{
	  new->next = prv;
	  prv = new;
	  return (prv);
	}
      if (prv->n < number && prv->next->n > number)
	{
	  new->next = prv->next;
	  prv->next = new;
	  return (prv);
	}
      if (prv->next == NULL)
	{
	  prv->next = new;
	  return (prv);
	}
      if (prv->n == number)
	{
	  prv->next = new;
	  new->next = prv->next->next;
	}
      prv = prv->next;
    }
  return (*head);
}
	       
