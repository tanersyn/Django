#python manage.py runserver

from django.contrib import admin

from .models import Article

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin): # Admin panelini özelleştireceğimiz articleadmin classı 

    list_display = ["title","author","created_date"] # Yazı,yazar ve oluşturulma tarihi gözükecek
    list_display_links = ["title","created_date"] # Başlık ve oluşturulma saatine basıldığında yazının içeriğini görebileceğiz
    search_fields = ["title"] # Title bilgisine göre arama özelliği  
    list_filter = ["created_date"] # Makaleleri gün,zamana göre filtreleme özelliği 

    # ArticleAdmin ile yukarıdaki Article birleştirmemiz gerekiyor ;
    class Meta():
        model = Article