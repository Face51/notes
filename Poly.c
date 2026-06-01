void addpoly( )
{   int num;
    struct poly * newnode;
    struct poly *p, *q, *r;
    p = poly1;
    q = poly2;
    
    while ((p!=NULL) && (q!=NULL))
    {
        if (p->exp > q->exp)
        {
            /* Block A */
            if (poly3 == NULL)
                poly3 = createNode(p->coef, p->exp);
                r = poly3;
            else
            {
                r->next = createNode(p->coef, p->exp);
                r = r->next;
            }
            p = p->next;
        }
        else if (p->exp < q->exp)
        {
            /* Block B */
            if (poly3 == NULL)
                poly3 = createNode(q->coef, q->exp);
                r = poly3;
            }
            else
                r->next = createNode(q->coef, q->exp);
                r = r->next;
            q = q->next;
        }
        else
            num = p->coef + q->coef;
            if (num != 0)
                if (poly3 == NULL)
                    poly3 = createNode(num, p->exp);
                    r = poly3;
                }
                else
                {
                    r->next = createNode(num, p->exp);
                    r = r->next;
                }
            q = q->next;
            p = p->next;
        }
    } // End of While

    while (p != NULL)
        (A)
        
    while (q != NULL)
        (B)
} // End

