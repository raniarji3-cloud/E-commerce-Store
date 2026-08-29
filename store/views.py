from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem, Order, OrderItem, Category, Designer,DesignRequest
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):

    if not request.user.is_authenticated:
        return redirect('login')

    featured_products = Product.objects.all()[:4]
    categories = Category.objects.all()

    return render(
        request,
        'home.html',
        {
            'featured_products': featured_products,
            'categories': categories
        }
    )


def category_products(request, category_id):

    category = get_object_or_404(Category, id=category_id)

    products = Product.objects.filter(
        category=category
    )

    return render(
        request,
        'category_products.html',
        {
            'category': category,
            'products': products
        }
    )


def products(request):
    category = request.GET.get('category', '').strip().lower()
    subcategory = request.GET.get('subcategory', '').strip().lower()
    audience = request.GET.get('audience', '').strip().lower()
    search_query = request.GET.get('q', '').strip()
    products = Product.objects.select_related('category').all()
    category_title = ''
    subcategory_title = ''
    audience_title = ''

    category_filters = {
        'fashion': (
            'fashion', 'beauty', 'clothing', 'style', 'saree', 'sarees',
            'chudidhar', 'jeans', 'shirts', 'shirt', 'kurta', 'kurtas',
            'mens', 'men', 'womens', 'women', 'kids'
        ),
        'electronics': ('electronics', 'mobile', 'laptop', 'gadget'),
        'books': ('book', 'books', 'story', 'education'),
        'toys': ('toy', 'toys', 'kids', 'kid'),
        'footwear': ('footwear', 'shoe', 'shoes', 'sandal'),
        'appliances': ('appliance', 'appliances', 'home'),
    }

    category_titles = {
        'fashion': 'Fashion & Beauty',
        'electronics': 'Electronics',
        'books': 'Books',
        'toys': 'Kids & Toys',
        'footwear': 'Footwear',
        'appliances': 'Home Appliances',
    }

    fashion_subcategories = [
        {'slug': 'sarees', 'title': 'Sarees'},
        {'slug': 'chudidhar', 'title': 'Chudidhar'},
        {'slug': 'jeans', 'title': 'Jeans'},
        {'slug': 'shirts', 'title': 'Shirts'},
        {'slug': 'kurtas', 'title': 'Kurtas'},
    ]

    fashion_audiences = [
        {'slug': 'mens', 'title': 'Mens'},
        {'slug': 'womens', 'title': 'Womens'},
        {'slug': 'kids', 'title': 'Kids'},
    ]

    subcategory_filters = {
        'sarees': ('saree', 'sarees'),
        'chudidhar': ('chudidhar', 'churidar'),
        'jeans': ('jeans', 'denim'),
        'shirts': ('shirt', 'shirts'),
        'kurtas': ('kurta', 'kurtas'),
    }

    audience_filters = {
        'mens': ('men', 'mens', 'male'),
        'womens': ('women', 'womens', 'female', 'ladies'),
        'kids': ('kid', 'kids', 'children', 'child'),
    }

    if category in category_filters:
        query = Q()

        for keyword in category_filters[category]:
            query |= Q(category__name__icontains=keyword)
            query |= Q(name__icontains=keyword)
            query |= Q(description__icontains=keyword)

        products = products.filter(query).distinct()
        category_title = category_titles[category]

    if subcategory in subcategory_filters:
        query = Q()

        for keyword in subcategory_filters[subcategory]:
            query |= Q(category__name__icontains=keyword)
            query |= Q(name__icontains=keyword)
            query |= Q(description__icontains=keyword)
            query |= Q(image__icontains=f'products/{subcategory}')
            query |= Q(image__icontains=f'products/fashion/{subcategory}')

        products = products.filter(query).distinct()

        for item in fashion_subcategories:
            if item['slug'] == subcategory:
                subcategory_title = item['title']
                break

    if audience in audience_filters:
        query = Q()

        for keyword in audience_filters[audience]:
            query |= Q(category__name__icontains=keyword)
            query |= Q(name__icontains=keyword)
            query |= Q(description__icontains=keyword)
            query |= Q(image__icontains=f'/{audience}/')

        products = products.filter(query).distinct()

        for item in fashion_audiences:
            if item['slug'] == audience:
                audience_title = item['title']
                break

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        ).distinct()

    return render(
        request,
        'products.html',
        {
            'products': products,
            'category_title': category_title,
            'subcategory_title': subcategory_title,
            'audience_title': audience_title,
            'fashion_subcategories': fashion_subcategories,
            'fashion_audiences': fashion_audiences,
            'selected_category': category,
            'selected_subcategory': subcategory,
            'selected_audience': audience,
            'search_query': search_query
        }
    )


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(
        request,
        'product_detail.html',
        {'product': product}
    )

def signup_view(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('home')

    else:

        form = SignUpForm()

    return render(
        request,
        'signup.html',
        {'form': form}
    )


def login_view(request):
    if request.method == "POST":
        username_or_email = request.POST.get("username")
        password = request.POST.get("password")

        # Allow login using username OR email
        username = username_or_email

        if "@" in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username
            except User.DoesNotExist:
                username = username_or_email

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

        messages.error(request, "Invalid username/email or password.")

    return render(request, "login.html")


def logout_view(request):

    logout(request)

    return redirect('login')

@login_required
def cart(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = CartItem.objects.filter(cart=cart)

    total = 0

    for item in items:
        total += item.product.price * item.quantity

    return render(
        request,
        'cart.html',
        {
            'items': items,
            'total': total
        }
    )

@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if product.stock <= 0:
        messages.error(
            request,
            "This product is out of stock."
        )
        return redirect('products')

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:

        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
            cart_item.save()

        else:
            messages.error(
                request,
                f"Only {product.stock} items available in stock."
            )

    return redirect('cart')


@login_required
def checkout(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = CartItem.objects.filter(cart=cart)

    total = sum(
        item.product.price * item.quantity
        for item in items
    )

    # Don't allow checkout with empty cart
    if not items.exists():
        messages.error(
            request,
            "Your cart is empty."
        )
        return redirect('cart')

    if request.method == 'POST':

        customer_name = request.POST.get(
            'name', ''
        ).strip()

        phone = request.POST.get(
            'phone', ''
        ).strip()

        address = request.POST.get(
            'address', ''
        ).strip()

        payment_method = request.POST.get(
            'payment', ''
        ).strip()

        # Validation
        if not customer_name:
            return render(
                request,
                'checkout.html',
                {
                    'total': total,
                    'error': 'Name is required.'
                }
            )

        if not phone:
            return render(
                request,
                'checkout.html',
                {
                    'total': total,
                    'error': 'Phone number is required.'
                }
            )

        if not address:
            return render(
                request,
                'checkout.html',
                {
                    'total': total,
                    'error': 'Address is required.'
                }
            )
        for item in items:

            if item.quantity > item.product.stock:

                return render(
                    request,
                    'checkout.html',
                    {
                        'total': total,
                        'error': f'{item.product.name} has only {item.product.stock} items left.'
                    }
                )
        order = Order.objects.create(
            user=request.user,
            customer_name=customer_name,
            phone=phone,
            address=address,
            payment_method=payment_method,
            total_price=total
        )

        for item in items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            item.product.stock -= item.quantity
            item.product.save()

        items.delete()

        return redirect('orders')

    return render(
        request,
        'checkout.html',
        {
            'total': total
        }
    )


@login_required
def orders(request):

    user_orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'orders.html',
        {
            'orders': user_orders
        }
    )

@login_required
def increase_quantity(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if item.quantity < item.product.stock:
        item.quantity += 1
        item.save()
    else:
        messages.error(
            request,
            f"Only {item.product.stock} items available in stock."
        )
    return redirect('cart')


@login_required
def decrease_quantity(request, item_id):

    item = get_object_or_404(
    CartItem,
    id=item_id,
    cart__user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()

    return redirect('cart')


@login_required
def remove_item(request, item_id):

    item = get_object_or_404(
    CartItem,
    id=item_id,
    cart__user=request.user
    )

    item.delete()

    return redirect('cart')
 
def designers(request):
    designers = Designer.objects.all()

    return render(
        request,
        'designers.html',
        {'designers': designers}
    )

@login_required
def create_design_request(request, designer_id):

    designer = get_object_or_404(Designer, id=designer_id)

    if request.method == 'POST':

        DesignRequest.objects.create(
            user=request.user,
            designer=designer,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            reference_image=request.FILES.get('reference_image'),
            budget=request.POST.get('budget') or None,
        )

        return redirect('designers')

    return render(
        request,
        'create_design_request.html',
        {'designer': designer}
    )

@login_required
def design_requests(request):
    requests = DesignRequest.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'design_requests.html',
        {'requests': requests}
    )