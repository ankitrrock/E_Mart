from django.urls import path
from App.views import about,checkout,dresses,faq,mail,jeans,products,salwars,sandals,sarees,shirts,single,skirts,sweaters,index,short_codes,register


urlpatterns = [
   
    path("",index,name="index"),
    path("checkout",checkout,name="checkout"),
    path("dresses",dresses,name="dresses"),
    path("faq",faq,name="faq"),
    path("mail",mail,name="mail"),
    path("products",products,name="products"),
    path("salwars",salwars,name="salwars"),
    path("sandals",sandals,name="sandals"),
    path("sarees",sarees,name="sarees"),
    path("shirts",shirts,name="shirts"),
    path("single",single,name="single"),
    path("skirts",skirts,name="skirts"),
    path("sweaters",sweaters,name="sweaters"),
    path("jeans",jeans,name="jeans"),
    path("about",index,name="about"),
    path("short_codes",index,name="short_codes"),
    path("register",register,name="register"),
   
]
