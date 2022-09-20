from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic as views

from product.forms import ProductForm
from product.models import Cart, CartItem, Product

USER = get_user_model()


# create course
class ProductCreateView(views.CreateView):
    template_name = "product/form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product:list")
    extra_context = {"action": "Create"}

    # def form_valid(self,form):
    #     form.instance.user=self.request.user
    #     return super().form_valid(form)

    def get(self, request):
        context = {"form": self.form_class()}
        context.update(self.extra_context)
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

    def form_invalid(self, form):
        context = {"form": form}
        context.update(self.extra_context)
        return render(self.request, self.template_name, context)


# list course
class ProductListView(views.ListView):
    template_name = "product/list.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        qs = Product.objects.filter(status=True)
        return qs


# detail course
class ProductDetailview(views.DetailView):
    template_name = "product/detail.html"
    model = Product
    context_object_name = "product"

    def get_queryset(self):
        qs = Product.objects.filter(status=True)
        return qs


# update course
class ProductUpdateView(views.UpdateView):
    template_name = "product/form.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("product:list")
    extra_context = {"action": "Update"}


# delete course
class ProductDeleteView(views.DeleteView):
    template_name = "product/form.html"
    model = Product
    success_url = reverse_lazy("product:list")
    extra_context = {"action": "Delete", "info": "Are you sure want to delete?"}

    def form_valid(self, form):
        self.object.status = False
        self.object.save()
        url = super().get_success_url()
        return redirect(url)


# class Cart(object):
#     def __init__(self, request):
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart

#     def add(self, product, quantity=1, update_quantity=False):
#         product_id = str(product.id)
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
#         if update_quantity:
#             self.cart[product_id]['quantity'] = quantity
#         else:
#             self.cart[product_id]['quantity'] += quantity
#         self.save()

#     def save(self):
#         self.session[settings.CART_SESSION_ID] = self.cart
#         self.session.modified = True

#     def remove(self, product):
#         product_id = str(product.id)
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()

#     def __iter__(self):
#         product_ids = self.cart.keys()
#         products = Product.objects.filter(id__in=product_ids)
#         for product in products:
#             self.cart[str(product.id)]['product'] = product

#         for item in self.cart.values():
#             item['price'] = Decimal(item['price'])
#             item['total_price'] = item['price'] * item['quantity']
#             yield item

#     def __len__(self):
#         return sum(item['quantity'] for item in self.cart.values())

#     def get_total_price(self):
#         return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

#     def clear(self):
#         del self.session[settings.CART_SESSION_ID]
#         self.session.modified = True


class AddToCart(LoginRequiredMixin, views.View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        quantity = request.POST.get("quantity")
        user = request.user

        product = Product.objects.filter(id=product_id).first()
        cart, created = Cart.objects.get_or_create(user=user, status=True)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity
            
        messages.success(request, "Added successfully!")
        return redirect(reverse_lazy("product:list"))
