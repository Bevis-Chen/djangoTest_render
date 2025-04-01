from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)  # 文章標題
    content = models.TextField()  # 文章內容
    created_at = models.DateTimeField(auto_now_add=True)  # 自動記錄建立時間

    def __str__(self):
        return self.title