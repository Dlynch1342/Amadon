from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Product

def index(request):
	products = Product.objects.all()
	context = {
		'all_products': products,
	}
	return render(request, 'products/index.html', context )

def add_product(request):
	print(request.POST)
	Product.objects.create(name=request.POST['name'], price = request.POST['price'])
	return redirect('/')

def buy(request):
	product = Product.objects.get(id = request.POST['product_id'])

	if 'current_price' in request.session:
		request.session['current_price'] = float(product.price) * float(request.POST['quantity'])
	else:
		request.session['current_price'] = float(product.price) * float(request.POST['quantity'])

	if 'total_items' in request.session:
		request.session['total_items'] += int(request.POST) 
	else:
		request.session['total_items'] += int(request.POST) 

	if 'total_items' in request.session:
		request.session['total_spent'] += float(request.session['session_price']) 
	else:
		request.session['total_spent'] += float(request.session['session_price']) 
	
	return redirect('/amadon/checkout')

	def checkout(request):
		print(request.session)['current_price']
		print(request.session)['total_items']
		print(request.session)['total_spent']
		return redirect('/products/checkout.html')

