from django.db import models

#urank:(0:super-admin, 1:admin, 2:ordinary-user)
class users(models.Model):
	uname=models.CharField(max_length=20)
	upass=models.CharField(max_length=50)
	urank=models.IntegerField()

class profile(models.Model):
	puser=models.ForeignKey(users)
	pstuid=models.CharField(max_length=20)
	pclass=models.IntegerField()
	ptel=models.CharField(max_length=20)
	pemail=models.CharField(max_length=50)

class score(models.Model):
	sstuid=models.CharField(max_length=20)
	scname=models.CharField(max_length=50)
	sscore=models.FloatField(max_length=5)
	sweigh=models.IntegerField()
	sstyle=models.CharField(max_length=20)
	sterms=models.IntegerField()

class feedback(models.Model):
	fcontent=models.CharField(max_length=100)

class tasks(models.Model):
	tyear=models.IntegerField()
	tmonth=models.IntegerField()
	tday=models.IntegerField()
	tcontent=models.CharField(max_length=50)
	tuser=models.IntegerField()