# -*- coding: utf-8 -*- 
# ===============================================================================
# @Name:         urls.py
# @Description:  
# @Author:       springbocai
# @Date:         2019/9/27
# ===============================================================================
from django.urls import path , include
import blog.views

urlpatterns = [
    path ('hello_world',blog.views.hello_world),
    path('content',blog.views.article_content),
    path('index',blog.views.get_index_page),
   # path('detail',blog.views.get_detail_page)
    path('detail/<int:atricle_id>',blog.views.get_detail_page)
]
