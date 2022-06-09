from django.db import models
import uuid
from django.utils import timezone
	# Create your models here.

class user(models.Model):
	id=models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
	name=models.CharField(max_length=30)
	password=models.CharField(max_length=200)
	email=models.EmailField()
	def __str__(self):
		return self.name

class Todo(models.Model):
	status_choices=[
		('C','COMPLETED'),
		('F','PENDING')
	]
	priority_choices=[
		('1','1️⃣'),
		('2','2️⃣'),
		('3','3️⃣'),
		('4','4️⃣'),
		('5','5️⃣'),
		('6','6️⃣'),
		('7','7️⃣'),
		('8','8️⃣'),
		('9','9️⃣'),
		('10','🔟'),
	]
	title=models.CharField(max_length=56)
	serial=models.CharField(max_length=100)
	status=models.CharField(max_length=2,choices=status_choices)
	user=models.ForeignKey(user,on_delete=models.CASCADE)
	date=models.DateTimeField(auto_now_add=True)
	priority=models.CharField(max_length=2,choices=priority_choices)
	description=models.TextField(max_length=300)
	def __str__(self):
		return self.title
