from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import request
from realestate.settings import EMAIL_HOST_USER

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if user made inquiry already
        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listings/'+listing_id )
            contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id) 
            contact.save()
            current_user = request.user
            # Email to realtor of that property
            send_mail(
                'Property Inquiry',
                'There has been a inquiry for the property'+listing+'. sign into admin for more info',
                EMAIL_HOST_USER,
                [realtor_email, 'hari'],
                fail_silently = False,
            )
            # Email to the logged-in user for confirming is inquiry
            recipient_list = [current_user.email, ]
            send_mail(
                'YOUR PROPERTY INQUIRY',
                'Your inquiry for the property '+listing+' has been made successfully our realtor will get back to you shortly',
                EMAIL_HOST_USER,
                recipient_list,
                fail_silently = False,
            ) 
            messages.success(request, 'Your request has been submitted,realtor will get back to you soon')
            return redirect('/listings/'+listing_id )
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'You are not logged-in please login to inquire about a property')
                return redirect('login')
            else:
                messages.error(request, 'You are not registered please register to inquire about a property')
                return redirect('register')
            



