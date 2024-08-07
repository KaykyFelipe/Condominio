from django.db import models

class condominio_tabela(models.Model):
    
    nome_condominio = models.TextField()
    regras_mudanca = models.TextField()
    diretorio = models.TextField()

   
    def __str__(self):
        return self.nome_condominio