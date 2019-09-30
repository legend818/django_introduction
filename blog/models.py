from django.db import models

# Create your models here.
class Article(models.Model):
    # 文章的唯一ID
    atricle_id = models.AutoField(primary_key = True)   # 这里犯了一个错误atricle_id 写错了，导致后面都按错误的写了
    # 文章的标题
    title = models.TextField()
    # 文章的摘要
    brief_content = models.TextField()
    # 文章的主要内容
    content = models.TextField()
    # 文章的发布日期
    publish_data = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title