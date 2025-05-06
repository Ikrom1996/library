from django.db import models



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Authors(BaseModel):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.birth_date}'




class Books(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Authors, on_delete=models.PROTECT, related_name="Book_Author",blank=True, null=True)
    file = models.FileField(upload_to="books/")
    image = models.ImageField(upload_to = 'upload_image/')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-id',)


class FileUpload(models.Model):
    name = models.CharField(max_length = 100 )
    file = models.FileField(upload_to = 'test')
