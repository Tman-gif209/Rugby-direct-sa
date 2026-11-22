from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm as UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def post(request):

    products = [

        {
            "name": "Agility Ladder",
            "price": 299,
            "category": "Training",
            "description": "Improve speed and footwork drills.",
            "image": "images/agilityladder.jpeg"
        },

        {
            "name": "Training Cones",
            "price": 60,
            "category": "Training",
            "description": "Perfect for agility and fitness exercises.",
            "image": "images/cones.jpg"
        },

        {
            "name": "Gilbert Rugby Ball",
            "price": 200,
            "category": "Balls",
            "description": "Professional match-quality rugby ball.",
            "image": "images/gilbertball.jpg"
        },

        {
            "name": "Rugby Goal Posts",
            "price": 10000,
            "category": "Training",
            "description": "Heavy-duty rugby goal posts.",
            "image": "images/poles.jpg"
        },

        {
            "name": "Puma Rugby Boots",
            "price": 1900,
            "category": "Boots",
            "description": "Designed for maximum grip and comfort.",
            "image": "images/pumaboot.jpg"
        },

        {
            "name": "Springbok Rugby Jersey",
            "price": 500,
            "category": "Apparel",
            "description": "Official supporter-style rugby jersey.",
            "image": "images/SAshirt.jpg"
        },

        {
            "name": "Mouth Guard",
            "price": 120,
            "category": "Accessories",
            "description": "Essential protection during matches.",
            "image": "images/mouthguard.jpeg"
        },

        {
            "name": "Rugby Kit Bag",
            "price": 850,
            "category": "Accessories",
            "description": "Large storage bag for rugby gear.",
            "image": "images/rugbybag.jpeg"
        },

        {
            "name": "Tackle Bag",
            "price": 1999,
            "category": "Training",
            "description": "Professional tackle training equipment.",
            "image": "images/tacklebag.jpeg"
        },

        {
            "name": "Sports Water Bottle",
            "price": 80,
            "category": "Accessories",
            "description": "Stay hydrated during training.",
            "image": "images/waterbottle.jpg"
        },

        {
            "name": "Bluetooth Earphones",
            "price": 1500,
            "category": "Accessories",
            "description": "Wireless sports earphones.",
            "image": "images/bluetoothearphones.jpg"
        },

        {
            "name": "VOL Headphones",
            "price": 1800,
            "category": "Accessories",
            "description": "Premium sound quality headphones.",
            "image": "images/volheadphones.jpg"
        },

        {
            "name": "White Rugby Boots",
            "price": 2300,
            "category": "Boots",
            "description": "Premium lightweight rugby boots.",
            "image": "images/whiterugby.jpg"
        },

        {
            "name": "Rhino URC Rugby Ball",
            "price": 350,
            "category": "Balls",
            "description": "Official URC style rugby ball.",
            "image": "images/URCball.jpg"
        },

        {
            "name": "Sports T-Shirt",
            "price": 250,
            "category": "Apparel",
            "description": "Comfortable performance sports shirt.",
            "image": "images/sportstee.jpg"
        },

        {
            "name": "Referee Whistle",
            "price": 99,
            "category": "Accessories",
            "description": "Professional referee whistle.",
            "image": "images/refereewhistle.jpeg"
        },

        {
            "name": "Pro Rugby Boots",
            "price": 2600,
            "category": "Boots",
            "description": "High-performance adidas rugby boots.",
            "image": "images/adidasboots.webp"
        },

        {
            "name": "Agility Hurdles",
            "price": 650,
            "category": "Training",
            "description": "Training hurdles for speed drills.",
            "image": "images/hurdles.webp"
        }

    ]

    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()

    if query:
        products = [
            product
            for product in products
            if query.lower() in product["name"].lower()
        ]

    if category:
        products = [
            product
            for product in products
            if product["category"] == category
        ]

    cart_items = request.session.get("cart", [])

    return render(
        request,
        "post.html",
        {
            "products": products,
            "query": query,
            "category": category,
            "cart_count": len(cart_items)
        }
    )

@login_required
def blogpost(request):

    cart_items = request.session.get("cart", [])

    return render(
        request,
        "blogpost.html",
        {
            "cart_count": len(cart_items)
        }
    )


@login_required
def payment(request):

    cart_items = request.session.get("cart", [])

    return render(
        request,
        "paymentsite.html",
        {
            "cart_count": len(cart_items)
        }
    )



def member(request):
    return render(
        request,
        "membership.html"
    )


@login_required
def home(request):

    cart_items = request.session.get("cart", [])

    return render(
        request,
        "home.html",
        {
            "cart_count": len(cart_items)
        }
    )




def register(request):

    if request.method == "POST":

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Account created successfully. You can now log in."
            )

            return redirect("login")

    else:

        form = UserRegistrationForm()

    return render(
        request,
        "register.html",
        {
            "form": form
        }
    )

def logout_user(request):

    logout(request)

    return render(
        request,
        "logout.html"
    )

@login_required
def purchase_success(request):

    cart_items = request.session.get("cart", [])

    item_count = sum(cart_items.values())

    prices = {
        "Agility Ladder": 299,
        "Training Cones": 60,
        "Gilbert Rugby Ball": 200,
        "Rugby Goal Posts": 10000,
        "Puma Rugby Boots": 1900,
        "Springbok Rugby Jersey": 500,
        "Mouth Guard": 120,
        "Rugby Kit Bag": 850,
        "Tackle Bag": 1999,
        "Sports Water Bottle": 80,
        "Bluetooth Earphones": 1500,
        "VOL Headphones": 1800,
        "White Rugby Boots": 2300,
        "Rhino URC Rugby Ball": 350,
        "Sports T-Shirt": 250,
        "Referee Whistle": 99,
        "Pro Rugby Boots": 2600,
        "Agility Hurdles": 650,
    }

    total = 0

    for item_name, quantity in cart_items.items():

        total += prices.get(item_name, 0) * quantity

        request.session["cart"] = {}

    return render(
        request,
        "purchase_success.html",
        {
            "item_count": item_count,
            "total": total
        }
    )

@login_required
def cart(request):

    cart_items = request.session.get("cart", {})

    # Convert old list cart to new dictionary cart
    if isinstance(cart_items, list):

        new_cart = {}

        for item in cart_items:

            if item in new_cart:
                new_cart[item] += 1
            else:
                new_cart[item] = 1

        cart_items = new_cart

        request.session["cart"] = cart_items

    total = 0

    prices = {
        "Agility Ladder": 299,
        "Training Cones": 60,
        "Gilbert Rugby Ball": 200,
        "Rugby Goal Posts": 10000,
        "Puma Rugby Boots": 1900,
        "Springbok Rugby Jersey": 500,
        "Mouth Guard": 120,
        "Rugby Kit Bag": 850,
        "Tackle Bag": 1999,
        "Sports Water Bottle": 80,
        "Bluetooth Earphones": 1500,
        "VOL Headphones": 1800,
        "White Rugby Boots": 2300,
        "Rhino URC Rugby Ball": 350,
        "Sports T-Shirt": 250,
        "Referee Whistle": 99,
        "Pro Rugby Boots": 2600,
        "Agility Hurdles": 650,
    }

    total = 0

    cart_products = []

    for item_name, quantity in cart_items.items():

        price = prices.get(item_name, 0)

        subtotal = price * quantity

        total += subtotal

        cart_products.append(
            {
                "name": item_name,
                "price": price,
                "quantity": quantity,
                "subtotal": subtotal
            }
        )

    return render(
        request,
        "cart.html",
        {
            "cart_products": cart_products,
            "total": total,
            "cart_count": sum(cart_items.values())
        }
    )

def add_to_cart(request, product_name):

    cart = request.session.get("cart", {})

    if isinstance(cart, list):

        old_cart = {}

        for item in cart:
            if item in old_cart:
                old_cart[item] += 1
            else:
                old_cart[item] = 1

        cart = old_cart

    if product_name in cart:
        cart[product_name] += 1
    else:
        cart[product_name] = 1

    request.session["cart"] = cart

    return redirect("cart")

def update_quantity(request, product_name):

    cart = request.session.get("cart", {})

    quantity = int(request.POST.get("quantity", 1))

    if quantity < 1:
        quantity = 1

    if product_name in cart:
        cart[product_name] = quantity

    request.session["cart"] = cart

    return redirect("cart")

def remove_from_cart(request, product_name):

    cart = request.session.get("cart", {})

    if product_name in cart:
        del cart[product_name]

    request.session["cart"] = cart

    return redirect("cart")

def clear_cart(request):

    request.session["cart"] = {}

    return redirect('cart')

def update_quantity(request, product_name):

    cart = request.session.get("cart", {})

    quantity = int(
        request.POST.get(
            "quantity",
            1
        )
    )

    if quantity < 1:
        quantity = 1

    if product_name in cart:
        cart[product_name] = quantity

    request.session["cart"] = cart

    return redirect("cart")