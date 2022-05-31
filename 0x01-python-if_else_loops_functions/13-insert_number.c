#include "lists.h"
#include <stdlib.h>
/**listint_t *insert_big(listint_t **head, int number)
{
  listint_t *new, *cur;
  cur = *head;
  new = malloc(sizeof(listint_t));
  new->n = number;
  new->next = cur;
  cur = new;
  return (cur);
}
  
listint_t *insert_end(listint_t **head, int number)
{
  listint_t *new, *cur;
  new = malloc(sizeof(listint_t));
  new->n == number;
  new->next = NULL;
  if (*head == NULL)
    {
      *head = new;
      return (head);
    }
  while (cur->next != NULL)
    {
      cur = cur->next;
    }
  cur->next = new;
  return (*head);
}
**/
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
  if (prv->next == NULL && prv->n <= number)
    {
      prv->next = new;
      return (prv);
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
      
    }
  return (*head);
}
	       
