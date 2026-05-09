from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from users.forms import CustomUserCreationForm
from django.views.generic.edit import CreateView


handler404 = 'core.views.page_not_found' 

urlpatterns = [
    path('auth/', include('django.contrib.auth.urls')),
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('birthday/', include('birthday.urls')),
    path(
        'auth/registration/', 
        CreateView.as_view(
            template_name='registration/registration_form.html', 
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('login'), 
        ),
        name='registration',
    ),
    # В конце добавляем к списку вызов функции static.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
