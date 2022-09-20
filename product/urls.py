from django.urls import path

from product import views

app_name = "product"

urlpatterns = [
    # product paths
    path("create/", views.ProductCreateView.as_view(), name="create"),
    path("list/", views.ProductListView.as_view(), name="list"),
    path("<int:pk>/detail/", views.ProductDetailview.as_view(), name="detail"),
    path("<int:pk>/delete/", views.ProductDeleteView.as_view(), name="delete"),
    path("<int:pk>/update/", views.ProductUpdateView.as_view(), name="update"),
    path("cart/add/", views.AddToCart.as_view(), name="add_to_cart"),

    # cart
    # path("cart/create/", views.EnrollCreateView.as_view(), name="cart_create"),

]