from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()
    # date = models.DateField()

    def __str__(self):
        return self.name




class Register(models.Model):
    username = models.TextField()
    firstname = models.TextField()
    password = models.TextField(default=0)
    lastname = models.TextField()
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    # upload = models.ImageField(upload_to ='uploads')
    file=models.FileField()

    def __str__(self):
        return self.username




class Roommate(models.Model):
    username = models.TextField()
    firstname = models.TextField()
    lastname = models.TextField()
    birthdate = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    # upload = models.ImageField(upload_to ='uploads')
    file=models.FileField()
    baseaddress = models.TextField()
    birthdate = models.DateField()

    def __str__(self):
        return self.username


state_choice = (
	("Maharashtra", "Maharashtra"),
)
city_choice = (
	("Mumbai", "Mumbai"),
)
area_choice = (
	("Borivali(east)", "Borivali(east)"),
	("Borivali(West)", "Borivali(west)"),
	("Kandivali(east)", "Kandivali(east)"),
	("Kandivali(west)", "Kandivali(west)"),
	("Dahisar(east)", "Dahisar(east)"),
	("Dahisar(West)", "Dahisar(west)"),
	("Miraroad(east)", "Miraroad(east)"),
	("Miraroad(West)", "Miraroad(west)"),
	("Bhaindar(east)", "Bhaindar(east)"),
	("Bhaindar(West)", "Bhaindar(west)"),
	("Naigoan(east)", "Naigoan(east)"),
	("Naigoan(West)", "Naigoan(west)"),
	("Vasairoad(east)", "Vasairoad(east)"),
	("Vasairoad(West)", "Vasairoad(west)"),
	("Nalasopara(east)", "Nalasopara(east)"),
	("Nalasopara(West)", "Nalasopara(west)"),
	("Virar(east)", "Virar(east)"),
	("Virar(West)", "Virar(west)"),
)
no_choice = (
	("0", "0"),
	("1", "1"),
	("2", "2"),
	("3", "3"),
	("4", "4"),
	("5", "5"),
	("6", "6"),
	("7", "7"),
	("8", "8"),
	("9", "9"),
	("10", "10"),
)
class Vacantroom(models.Model):
    username = models.TextField()
    address = models.TextField()
    state = models.TextField(choices = state_choice, default = 'Maharashtra')
    city = models.TextField(choices = city_choice, default = 'Mumbai')
    area = models.TextField(choices = area_choice, default = 'Kandivali(East)')
    room_mate_present = models.IntegerField(choices = no_choice, default = 0)
    room_mate_require = models.IntegerField(choices = no_choice, default = 0)
    name1 = models.TextField(default = 0)
    qualification1 = models.TextField(default = 0)
    name2 = models.TextField(default = 0)
    qualification2 = models.TextField(default = 0)
    name3 = models.TextField(default = 0)
    qualification3 = models.TextField(default = 0)
    name4 = models.TextField(default = 0)
    qualification4 = models.TextField(default = 0)
    name5 = models.TextField(default = 0)
    qualification5 = models.TextField(default = 0)
    name6 = models.TextField(default = 0)
    qualification6 = models.TextField(default = 0)
    name7 = models.TextField(default = 0)
    qualification7 = models.TextField(default = 0)
    name8 = models.TextField(default = 0)
    qualification8 = models.TextField(default = 0)
    name9 = models.TextField(default = 0)
    qualification9 = models.TextField(default = 0)
    name10 = models.TextField(default = 0)
    qualification10 = models.TextField(default = 0)
    rent = models.IntegerField()
    file=models.FileField()
    lastdate = models.DateField()

    def __str__(self):
        return self.address

class Vacanthouse(models.Model):
    username = models.TextField()
    address = models.TextField()
    state = models.TextField(choices = state_choice, default = 'Maharashtra')
    city = models.TextField(choices = city_choice, default = 'Mumbai')
    area = models.TextField(choices = area_choice, default = 'Kandivali(East)')
    rent = models.IntegerField()
    file=models.FileField()
    lastdate = models.DateField()

    def __str__(self):
        return self.address


class Sellroom(models.Model):
    username = models.TextField()
    address = models.TextField()
    state = models.TextField(choices = state_choice, default = 'Maharashtra')
    city = models.TextField(choices = city_choice, default = 'Mumbai')
    area = models.TextField(choices = area_choice, default = 'Kandivali(East)')
    sellprice = models.IntegerField()
    file=models.FileField()
    lastdate = models.DateField()

    def __str__(self):
        return self.address