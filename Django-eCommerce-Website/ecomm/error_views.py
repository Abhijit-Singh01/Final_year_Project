from django.shortcuts import render


def custom_404(request, exception):
    # exception arg is required by Django for handler404
    return render(request, "404.html", status=404)


def custom_500(request):
    return render(request, "500.html", status=500)


# Preview endpoints (useful when DEBUG=True, since Django shows technical pages)
def preview_404(request):
    return render(request, "404.html", status=404)


def preview_500(request):
    return render(request, "500.html", status=500)

