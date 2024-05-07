
In [4]: models.Note.objects.all()

Out[4]: <QuerySet [<Note: Записка 1>, <Note: Записка 2>]>

In [6]: models.Product.objects.all()
Out[6]: <QuerySet [<Product: Мяука>, <Product: Хлеб>, <Product: Золото>]>

In [9]: models.Task.objects.filter(priority='High')
Out[9]: <QuerySet [<Task: Сделать лабы>]>

In [10]: models.Product.objects.filter(price__gt=100)
Out[10]: <QuerySet [<Product: Мяука>, <Product: Золото>]>

In [11]: models.Task.objects.filter(completed=True)
Out[11]: <QuerySet [<Task: Сделать лабы>]>

In [13]: models.Note.objects.filter(created_at__month=5, created_at__year=2024)
Out[13]: <QuerySet [<Note: Записка 1>, <Note: Записка 2>]>

In [17]: from datetime import datetime, timedelta
    ...: next_month = datetime.now() + timedelta(days=30)
    ...: models.Task.objects.filter(due_date__month=next_month.month, due_date__year=next_month.year)
Out[17]: <QuerySet []>

In [18]: models.Product.objects.order_by('-price')
Out[18]: <QuerySet [<Product: Мяука>, <Product: Золото>, <Product: Хлеб>]>

In [19]: models.Note.objects.all()[:1]
Out[19]: <QuerySet [<Note: Записка 1>]>

In [21]: models.Product.objects.filter(description__icontains='мяукает')
Out[21]: <QuerySet [<Product: Мяука>]>

In [29]: models.Product.objects.filter(quantity__gt=2)
Out[29]: <QuerySet [<Product: Золото>]>

In [30]: models.Note.objects.filter(title__icontains='1')
Out[30]: <QuerySet [<Note: Записка 1>]>

In [32]: models.Task.objects.filter(priority__in=['Medium', 'High'])
Out[32]: <QuerySet [<Task: Помыть полы>, <Task: Приготовить поесть>, <Task: Сделать лабы>]>

In [33]: models.Product.objects.filter(price__range=(1000, 3000))
Out[33]: <QuerySet [<Product: Золото>]>

In [35]: models.Product.objects.exclude(quantity=0)
Out[35]: <QuerySet [<Product: Мяука>, <Product: Хлеб>, <Product: Золото>]>

In [36]: models.Product.objects.order_by('price')
Out[36]: <QuerySet [<Product: Хлеб>, <Product: Золото>, <Product: Мяука>]>

In [42]: models.Product.objects.filter(description__icontains='скидка')
Out[42]: <QuerySet [<Product: Дом>]>

