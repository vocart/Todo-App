from django.db import models


class Todo(models.Model):
	title = models.CharField(max_length = 100)
	message = models.TextField(max_length = 300)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-date']

