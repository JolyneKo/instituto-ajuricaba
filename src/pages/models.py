"""
================
     Models
================
"""

from django.db import models

class Evento(models.Model):
	imagem = models.ImageField(upload_to='Eventos')
	titulo = models.CharField(max_length=100)
	data = models.CharField(max_length=100)
	texto = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.titulo

