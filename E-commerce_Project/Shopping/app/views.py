from django.shortcuts import render
from django.views import View
from .models import Product
from .forms import CustomerRegistrationForm
from django.contrib import messages
# def home(request):
#  return render(request, 'app/home.html')

class Productview(View):
 def get(self,request):
   topwear =Product.objects.filter(category='TW')
   bottomwear=Product.objects.filter(category='BW')
   mobile=Product.objects.filter(category='M')
   laptop=Product.objects.filter(category='L')
   # import pdb;
   # pdb.set_trace()
   return render(request, 'app/home.html', {'topwears':topwear, 'bottomwears':bottomwear,'mobiles':mobile, 'laptop':laptop})


class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(id=pk)
        print(product)
        # import pdb;
        # pdb.set_trace()

        return render (request, 'app/productdetail.html' , {'product':product})



# def product_detail(request):
#  return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, mdata=None):
    if mdata == None:
        mobile = Product.objects.filter(category='M')
        print(mobile)
    elif mdata == 'micromax' or mdata == 'nokia':
        mobile = Product.objects.filter(category='M').filter(brand=mdata)

    elif mdata == 'below':
        mobile=Product.objects.filter(category='M').filter(discounted_price__lt=10000)

    elif mdata == 'above':
        mobile=Product.objects.filter(category='M').filter(discounted_price__gt=10000)

    return render(request, 'app/mobile.html', {'mobiles':mobile})

# def login(request):
#  return render(request, 'app/login.html')


def Topwear(request, data=None):
    if data == None:
     topwear=Product.objects.filter(category='TW')
    elif data == 'Lee' or data == 'pepe':
        topwear = Product.objects.filter(category='TW').filter(brand=data)
    return render(request, 'app/topwear.html', {'topwear':topwear})



def bottomwear(request, data=None):
    if data == None:
        btmwear=Product.objects.filter(category='BW')
    elif data == 'suzy' or data == 'pepe':
        btmwear=Product.objects.filter(category='BW').filter(brand=data)
    return render(request, 'app/bottomwear.html', {'btmwear':btmwear})



def laptops(request, ldata=None):
    if ldata == None:
        laptop =Product.objects.filter(category='L')
    elif ldata == 'samsung' or ldata == 'acer':
        laptop =Product.objects.filter(category='L').filter(brand=ldata)
    elif ldata == 'below':
        laptop=Product.objects.filter(category='L').filter(discounted_price__lt=10000)
    elif ldata == 'above':
        laptop=Product.objects.filter(category='L').filter(discounted_price__gt=10000)
    return render(request, 'app/laptop.html', {'laptop':laptop})



# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')


# Customer Registration

class CustomerRegistrationview(View):

    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'cst_form':form})

    def post(self, request):
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Successfully Registered')
            form.save()

        return render(request, 'app/customerregistration.html', {'cst_form':form})

def checkout(request):
 return render(request, 'app/checkout.html')
