from django.contrib import admin
from .models import(
    Category,
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem,
    Designer,
    DesignRequest,
)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)   

@admin.register(Designer)
class DesignerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'specialization',
        'location',
        'experience',
        'price_range',
    )


@admin.register(DesignRequest)
class DesignRequestAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'designer',
        'status',
        'created_at',
    )

    list_filter = ('status',)