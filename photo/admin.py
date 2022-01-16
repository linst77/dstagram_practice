from django.contrib import admin
from .models import Photo
# Register your models here.


class PhotoAdmin (admin.ModelAdmin):
    list_display = ['id', 'author', 'created', 'updated']

    # 글울쓸때 아이디를 찾아 넣을수 있다
    raw_id_fields = ['author']

    # 화면옆에 날자별, 최신별 필드를 넣을수 있다.
    list_filter = ['created', 'updated', 'author']

    # serch를 넣을수 있다. (작성자는 text가 아닌 fornekey 라서 특수한 문자를 넣는다 author모델의 username을 string으로 반환)
    search_fields = ['text', 'created', 'author__username']

    # 소팅을 할수있는 옵션 (관리자 페이지에서만의 ordering)
    ordering = ['-updated', '-created']

admin.site.register( Photo,PhotoAdmin)
