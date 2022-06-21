from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from board import views

# URLConf파일을 2개로 사용하기 위해 board.urls 를 인클루드 한다.
urlpatterns = [
    # 앱의 첫화면(원래는 로켓화면, 현재는 바로가기 링크로 수정)
    path('', views.index, name="index"),
    # 관리자 모드 
    path('admin/', admin.site.urls),
    # 게시판 경로 설정
    path('board/', include('board.urls')),
]
# 첨부파일 media파일로 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
