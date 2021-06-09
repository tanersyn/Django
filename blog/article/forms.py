from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # Modelinle buradaki formu ilişkili hale getirmek için
    class Meta:
        model = Article
        fields = ["title","content"]# Böyle oluşturduktan sonra Django modelimiz içinde hangi alanlar varsa ona göre alanlar oluşturacak
                                    # Böylece author,title,content ve created_date gelecek ama biz sadece title ve contente görme form input oluşturulsun
                                    # author kısmıda giriş yapan kullanıcı alınacak
