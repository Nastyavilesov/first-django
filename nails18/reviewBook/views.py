from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

MENU = {"Главная" : "/", "О Блоге" : "/blog", "Отзывы" : "/reviews"}


def reviewsPage(request):
    reviews = Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    data = {"menu": MENU, "title": "Отзывы", "reviews": reviews, 'form': form}

    return render(request, 'reviews.html', data)