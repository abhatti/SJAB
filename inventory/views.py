from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from inventory.forms import ItemForm, ItemWarehouseForm
from inventory.models import ItemWarehouseMapping, Item, Warehouse, Voucher, VoucherItemMapping


def login(request):
    return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def index(request):
    items = Item.objects.filter()
    html_data = []
    warehouse = Warehouse.objects.filter().order_by('id')
    for data in items:
        item_stock = []
        for ware in warehouse:
            stock = ItemWarehouseMapping.objects.filter(item_id=data.id, warehouse_id=ware.id).order_by('warehouse_id')
            if not stock:
                stock = 0
            else:
                stock = stock[0].stock
            item_stock.append(stock)
        values = {'name': data.name, 'stock': item_stock}
        html_data.append(values)
    return render(request, 'inventory/index2.html', {'warehouse': warehouse, 'item': html_data})


@login_required(login_url='/accounts/login/')
def additem(request):
    if request.method == 'POST':
        # POST, generate bound form with data from the request
        form_item = ItemForm(request.POST)

        # check if it's valid:
        if form_item.is_valid():
            # Insert into DB
            form_item.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/accounts/profile')
    else:
        # GET, generate unbound (blank) form

        form_item = ItemForm()
    return render(request, 'inventory/add_item.html', {'form_item': form_item})


@login_required(login_url='/accounts/login/')
def voucherlist(request):
    voucher_names = Voucher.objects.filter().order_by('-date_issued')
    return render(request, 'inventory/vouchers.html', {'voucher_names': voucher_names})


@login_required(login_url='/accounts/login/')
def voucherinfo(request):
    pk = request.GET.get('pk')
    if pk:
        voucher = VoucherItemMapping.objects.filter(voucher_number_id=pk)
    else:
        voucher = []
    return render(request, 'inventory/voucher_info.html', {'voucher': voucher})
