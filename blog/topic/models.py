from django.db import models



DEFAULT_STATUS='draft'
STATUS = {
    ('draft', 'Taslak'),
    ('published', 'Yayinlandi'),
    ('deleted', 'Silindi'),
}


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, default="")
    about = models.TextField(max_length=1000)
    cover_image = models.ImageField(
        upload_to='topic',
        null=True,
        blank=True
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CategoryItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    about=models.CharField(max_length=1000)
    slug = models.CharField(max_length=200)
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to='topic',
        null=True,
        blank=True,)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
