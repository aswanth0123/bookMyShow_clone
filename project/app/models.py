from django.db import models

# Create your models here.
class movie(models.Model):
    name=models.TextField()
    ratting=models.FloatField()
    m_format=models.TextField()
    duration=models.TextField()
    genre=models.TextField()
    r_date=models.DateField()
    cover_image=models.FileField()
    cover_image1=models.FileField()
    main_image=models.FileField()
    about=models.TextField()
    def __str__(self):
        return self.name
class member(models.Model):
    type=models.TextField()
    name=models.TextField()
    role=models.TextField()
    photo=models.FileField()
    def __str__(self):
        return self.name
class language(models.Model):
    language=models.TextField()
    movie_name=models.ForeignKey(movie,on_delete=models.CASCADE)
class movie_members(models.Model):
    member_name=models.ForeignKey(member,on_delete=models.CASCADE)
    movie_name=models.ForeignKey(movie,on_delete=models.CASCADE)
    def __str__(self):
        return self.member_name.name


class Theater(models.Model):
    name=models.TextField()
    place=models.TextField()
    address=models.TextField()
    cancellable=models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Screen(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name='screens')
    screen_number = models.IntegerField()

    def __str__(self):
        return f"Screen {self.screen_number} - {self.theater.name}"

class Show(models.Model):
    movie = models.ForeignKey(movie, on_delete=models.CASCADE, related_name='shows')
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='shows')
    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie.name} at {self.show_time}"
    

class Seat(models.Model):
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(max_length=10)
    seat_type = models.CharField(max_length=20, choices=[('Regular', 'Regular'), ('Premium', 'Premium')])

    def __str__(self):
        return f"Seat {self.seat_number} - {self.seat_type} ({self.screen})"
