from django.db import models

class CondominioDB(models.Model):
    
    nome_condominio = models.TextField(null=False)
    regras_mudanca = models.TextField(null=False)
    diretorio = models.TextField(null=False)
    
    class Meta:
        db_table = 'condominioDB'