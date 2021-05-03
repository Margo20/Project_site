from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import contactsForm, ChangePasswordForm, UserFormRegister, AccountLoginForm
from .models import FooterModel, contactsModel, DataModelUser, ExtendUser, DiscountModel, OrderCalculationModel, \
    KapRemModel, EuroRemModel, OurworkModel, RepairsModel
from cart.forms import CartAddProductForm


def product_detail(request, id, slug):
    ourwork = get_object_or_404(OurworkModel, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html', {'ourwork': ourwork, 'cart_product_form': cart_product_form})


def indexOur_work_bd(request, repair_slug=None):
    repair = None
    repairs = RepairsModel.objects.all()
    ourworks = OurworkModel.objects.all()
    if repair_slug:
        repair = get_object_or_404(RepairsModel, slug=repair_slug)
        ourworks = ourworks.filter(repair=repair)
    paginator = Paginator(ourworks, 4)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'repair': repair, 'repairs': repairs, 'page': page, 'ourworks': page.object_list}
    return render(request, 'pages/our_work_bd.html', context)

# def indexOur_work_bd(request):
#     repairs = RepairsModel.objects.all()
#     ourworks = OurworkModel.objects.all()
#     paginator = Paginator(ourworks, 1)
#     if 'page' in request.GET:
#         page_num = request.GET['page']
#     else:
#         page_num = 1
#     page = paginator.get_page(page_num)
#     context = {'repairs': repairs, 'page': page, 'ourworks': page.object_list}
#     return render(request, 'pages/our_work_bd.html', context)


def footer_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        record = FooterModel.objects.create(name=name, phone=phone, email=email)
        message ='Ваша заявка отправлена'
        return render(request, template_name='pages/main.html', context={'message': message})
    else:
        return render(request, template_name='pages/main.html')


def discount_form(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        record = DiscountModel.objects.create(phone=phone)
        message ='Благодарим за информацию'
        return render(request, template_name='pages/main.html', context={'message': message})
    else:
        return render(request, template_name='pages/main.html')


def index(request):
    data = request.POST
    return render(request, 'pages/main.html')


def indexOur_work_html(request):
    return render(request, 'pages/our_work.html')


def indexPrice(request):
    return render(request, 'pages/price.html')


def indexContacts(request):
    data = request.POST
    dataDBUser = contactsModel.objects.all()
    if request.POST:
        form = contactsForm(request.POST)
        phone = data['phone']
        if len(phone) < 9:
            return render(request, 'pages/base.html', {'error': 'Номер телефона должен содержать не менее 11 символов', 'color': 'red'})
        else:
            form.save()
            return render(request, 'pages/base.html', {'success': 'Благодарим за информацию!', 'color': 'green'})
        return redirect('rem:rem')
    else:
        form = contactsForm()
        context = {'form': form}
        return render(request, 'pages/contacts.html', context)

    return render(request, 'pages/contacts.html', {'dataDBUser': dataDBUser})


def indexReviews(request):
    return render(request, 'pages/about_us.html')


def indexServices(request):
    return render(request, 'pages/services.html')


def indexOrderCalculation(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        description = request.POST['description']
        record = OrderCalculationModel.objects.create(name=name, phone=phone, description=description)
        message ='Спасибо за информацию. Мы вам перезвоним'
        return render(request, template_name='pages/order_calculation.html', context={'message': message})
    else:
        return render(request, template_name='pages/order_calculation.html')


def indexKapRem(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        description = request.POST['description']
        record = KapRemModel.objects.create(name=name, phone=phone, description=description)
        message ='Спасибо за информацию. Мы вам перезвоним'
        return render(request, template_name='pages/kap_rem.html', context={'message': message})
    else:
        return render(request, template_name='pages/kap_rem.html')


def indexEuroRem(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        description = request.POST['description']
        record = EuroRemModel.objects.create(name=name, phone=phone, description=description)
        message ='Спасибо за информацию. Мы вам перезвоним'
        return render(request, template_name='pages/euro_rem.html', context={'message': message})
    else:
        return render(request, template_name='pages/euro_rem.html')


def saveuser_db(request):
    login = request.POST.get('login')
    password = request.POST.get('password')
    user = DataModelUser.objects.get(login=login)
    # userpass = DataModelUser.objects.filter()
    if check_password(password, user.password):
        print(password)
        return HttpResponse('Ты вошел')

    return render(request, 'pages/main.html')


class RegisterView(CreateView):
    model = ExtendUser
    template_name = 'user/user_register.html'
    form_class = UserFormRegister
    # success_url = reverse_lazy('rem:rem')
    success_url = reverse_lazy('rem:profile')

        # написать функцию для проверки


@login_required
def change_password(request):
    if request.method == 'POST':
        passwords = request.POST
        user = request.user
        old_password = passwords['old_password']
        new_password1 = passwords['new_password1']
        new_password2 = passwords['new_password2']
        print(old_password)
        if check_password(old_password, user.password):
            if new_password1 == new_password2:
                user.set_password(new_password1)
                user.save()
                message = 'Ваш пароль успешно изменен'
                return render(request, 'user/change_password.html', context={'message': message})
            else:
                error = 'Пароли не совпадают'
                return render(request, 'user/profile.html', context={'error': error})
    form = ChangePasswordForm()
    return render(request, 'user/change_password.html', context={'form': form})


class LogoutUserView(LoginRequiredMixin, LogoutView):
    template_name = 'pages/main.html'


@login_required
def profile_user(request):
    data = request.POST
    dataFooter = FooterModel.objects.all()
    dataDBUser = contactsModel.objects.all()
    dataDiscount = DiscountModel.objects.all()
    dataOrder = OrderCalculationModel.objects.all()
    dataKapRem = KapRemModel.objects.all()
    dataEuroRem = EuroRemModel.objects.all()

    return render(request, 'user/profile.html', {'dataDBUser': dataDBUser, 'dataFooter': dataFooter, 'dataDiscount': dataDiscount,
                                                 'dataOrder': dataOrder, 'dataKapRem': dataKapRem, 'dataEuroRem': dataEuroRem})


class LoginUserView(LoginView):
    template_name = 'user/login.html'
    redirect_field_name = 'profile.html'

# def user_login(request):
#     # error = ''
#     if request.method == 'POST':
#         form = AccountLoginForm(request.POST)
#         if form.is_valid():
#             cleaned_data = form.cleaned_data
#             user = ExtendUser.objects.filter(username=cleaned_data['login'])
#             if user:
#                 if check_password(cleaned_data['password'], user[0].password):
#                     user = user[0]
#                     login(request, user)
#                     return redirect('rem:profile')
#                 else:
#                     error = 'Неверный пароль'
#                     form = AccountLoginForm()
#                     context = {'error': error, 'form': form}
#                     return render(request, 'user/login.html', context=context)
#             else:
#                 error = 'Неверный логин'
#                 form = AccountLoginForm()
#                 context = {'error': error, 'form': form}
#                 return render(request, 'user/login.html', context=context)
#     form = AccountLoginForm()
#     context = {'form':form}
#     return render(request, 'user/login.html', context=context)