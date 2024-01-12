from django.db import models

# Create your models here.

#### Navigation Bar buttons ####
class NavBar(models.Model):
    name = models.CharField(max_length=15)
    link = models.CharField(max_length=10)
    order = models.IntegerField()
    class Meta:
        verbose_name_plural = "navbars"

    def __str__(self):
        return self.name
#### Navigation Bar toggles for buttons for Navbar ####
class NavBarToggle(models.Model):
    name = models.CharField(max_length=15)
    link = models.CharField(max_length=10)
    order = models.IntegerField()
    navbar = models.ForeignKey("NavBar",on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "navbartoggles"

    def __str__(self):
        return self.name
    
#### Testimonials ####
class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to="images/")
    order = models.IntegerField()
    class Meta:
        verbose_name_plural = "testimonials"
    def __str__(self):
        return self.name
        
    
    


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name



class Post(models.Model):
    title =  models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified =  models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category",related_name="posts")

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField( auto_now_add=True)
    post = models.ForeignKey("Post",on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.author} on '{self.post}'"


