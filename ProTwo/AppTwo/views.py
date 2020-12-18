from django.shortcuts import render
from AppTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request, "AppTwo/index.html")

def help(request):
    my_dict = {"insert_var": "Help Page"}
    return render(request, "AppTwo/help.html", context=my_dict)

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form Invalid")

    return render(request, 'AppTwo/users.html', {'form': form})
