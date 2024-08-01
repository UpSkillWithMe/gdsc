from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("login/", views.login, name="Login"),
    path("handlelogin/", views.handlelogin, name="handlelogin"),
    path("handlelogout/", views.handlelogout, name="handlelogout"),
    path("signup/", views.signup, name="SignUp"),
    path("handlesignup/", views.handlesignup, name="handlesignup"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("feedback/", views.feedback, name="feedback"),
    path("filter/", views.filter, name="filter"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),

# json
    path('get-sample/', views.get_sample, name='get_sample'),
    path('post-data/', views.post_data, name='post_data'),
]
