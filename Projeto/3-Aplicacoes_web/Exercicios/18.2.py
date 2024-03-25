# 18.2 – Entradas menores: No momento, o método __str__() no modelo Entry
# concatena reticências a todas as instâncias de Entry quando Django exibe uma
# entrada  no  site  de  administração  ou  no  shell.  Acrescente  uma  instrução  if  no
# método __str__() que adicione reticências somente se a entrada tiver mais de 50
# caracteres.  Utilize  o  site  de  administração  para  acrescentar  uma  entrada  com
# menos de 50 caracteres e certifique-se de que ela não contenha reticências quando
# for visualizada.

# class Entry(models.Model):
#     """Algo específico aprendido sobre um assunto."""
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     text = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)
 
#     class Meta:
#         verbose_name_plural = 'entries'
 
#     def __str__(self):
#         """Devolve uma representação em string do modelo."""
#         if (len(self.text) <= 50):
#             return self.text
#         return self.text[:50] + "..."