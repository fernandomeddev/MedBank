from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from users.models import Status 
import random
from django.views.generic import ListView
from .models import MoneyTransfer

def randomGen():
    # cria um numero de conta randomico
    return int(random.uniform(100000, 999999))

def index(request):
    try:
        curr_user = Status.objects.get(user_name=request.user) # Busca os detlahes da conta logada
    except:
        # se não existir os detlhes do (new user), criar novos detalhes
        curr_user = Status()
        curr_user.account_number = randomGen() # conta randomica
        curr_user.balance = 0
        curr_user.user_name = request.user
        curr_user.save()
    return render(request, "users/profile.html", {"curr_user": curr_user})

def money_transfer(request):
    if request.method == "POST":
        form = forms.MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()
        
            curr_user = models.MoneyTransfer.objects.get(enter_your_user_name=request.user)
            dest_user_acc_num = curr_user.enter_the_destination_account_number

            temp = curr_user # deleta a instacia depois da tranferencia
            
            dest_user = models.Status.objects.get(account_number=dest_user_acc_num) # FIELD 1
            transfer_amount = curr_user.enter_the_amount_to_be_transferred_in_INR # FIELD 2
            curr_user = models.Status.objects.get(user_name=request.user) # FIELD 3

            # Transfere o dinheiro!
            curr_user.balance = curr_user.balance - transfer_amount
            dest_user.balance = dest_user.balance + transfer_amount

            # Save as mudanças antes do redirect!
            curr_user.save()
            dest_user.save()

            temp.delete() # NOTE: deleta a instâcia para transações futuras

        return redirect("users/profile.html")
    else:
        form = forms.MoneyTransferForm()
    return render(request, "users/money_transfer.html", {"form": form})


def help(request):
    return render(request, "users/help.html")

def edit_details(request):
    if request.method == "POST":
        # POST formulario de ''BasicDetailsForms''
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form = forms.BasicDetailsForm(request.POST, instance=curr_user)
            if form.is_valid():
                form.save()
        except:
            form = forms.BasicDetailsForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user_name = request.user
                form.save()  
        
        # POST formulario de Password change
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')

        return redirect("users/edit_details.html")
    
    else: # GET actions
        try:
            curr_user = models.BasicDetails.objects.get(user_name=request.user)
            form1 = forms.BasicDetailsForm(instance=curr_user) # basic details
        except:
            form1 = forms.BasicDetailsForm()
        

        # change password
        form3 = PasswordChangeForm(request.user)

        dici = {"form1": form1, "form3": form3}
        return render(request, "users/edit_details.html", dici)

def delete_account(request):
    return render(request, "users/delete_account.html")

class Historico(ListView):
    model = Status
    template_name = 'users/report.html'
    context_object_name = 'tags'

    def get_queryset(self):  # SELECT * ALL NA TABELA DO SINTER 4
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        print(qs)

        return qs
        
