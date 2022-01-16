
from django.urls import path
from app import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyChangePasswordForm
from django.conf.urls.static import static
urlpatterns = [
    # path('', views.home),
    path('',  views.Productview.as_view(), name='productview'),
    #path('product-detail/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-detail/', views.Productview.as_view(), name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:mdata>', views.mobile, name='mobiledata'),
    path('topwear/', views.Topwear, name='topwear'),
    path('topwear/<slug:data>', views.Topwear, name='topweardata'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomweardata'),
    path('laptop/', views.laptops, name='laptops'),
    path('laptop/<slug:ldata>', views.laptops, name='laptopdata'),

    # path('login/', views.login, name='login'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html', form_class=MyChangePasswordForm, success_url='/changepassworddone/'), name='changepassword'),
    path('changepassworddone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/changepassworddone.html'), name='changepassworddone'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('registration/', views.CustomerRegistrationview.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
