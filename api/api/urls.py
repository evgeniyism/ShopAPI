from django.urls import path
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from django.contrib import admin
from backend.views import PartnerUpdate, RegisterAccount, LoginAccount, CategoryView, ShopView, ProductInfoView, \
    BasketView, AccountDetails, ContactView, OrderView, PartnerState, PartnerOrders, ConfirmAccount

app_name = 'backend'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'), # Загрузка прайса.  Реализовано и работает
    path('partner/state', PartnerState.as_view(), name='partner-state'), # Информация о магазине. Реализовано и работает
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('user/register', RegisterAccount.as_view(), name='user-register'), # Регистрация. Реализована и работает
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'), # Подтверждение. Реализовано и работает
    path('user/details', AccountDetails.as_view(), name='user-details'), # Прсомотре аккаунта/апдейт.  Реализовано и работает
    path('user/contact', ContactView.as_view(), name='user-contact'), # Просмотр контактов/апдейт контактов. Реализовано и работает
    path('user/login', LoginAccount.as_view(), name='user-login'), # Логин. Реализовано и работает
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('categories', CategoryView.as_view(), name='categories'), # Список категорий. Реализовано и работает
    path('shops', ShopView.as_view(), name='shops'),
    path('products', ProductInfoView.as_view(), name='shops'), #список товаров. Реализовано и работает
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
]