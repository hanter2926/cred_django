TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # ✅ सिर्फ एक बार
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


from django.contrib import admin
from django.urls import path, include

# 👇 image show करने के लिए
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('your_app_name.urls')),   # 👈 app connect
]

# 👇 media files (images) show करने के लिए
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('bolloapp.urls')),   # 👈 app connect
]

# 👇 media (image) show करने के लिए
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)