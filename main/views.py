from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.views.generic import *
from main.models import MediaDrivea
from main.forms import *
from django.http import HttpResponse


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	if request.user.is_authenticated:
		return redirect("homepage")
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
                
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
            
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form,"message":messages})




class ImageDriveaCreateView(CreateView):
	model = MediaDrivea
	form = MediaForm()
	template_name = "index.html"
	


class ImageView(View):
	def get(self, request, *args, **kwargs):
		form=MediaForm()
		Media=MediaDrivea.objects.filter(author=request.user)
		extension=list()
		
		for i in Media:
			string_media=str(i)
			new=os.path.splitext(string_media)[1]
			extension.append(new)
		print(extension)

		
		

		



		context={
			"form":form,
			"media":Media,
			"extension":extension,
		}



		return render(request,'index.html',context)


	def post(self,request,*args, **kwargs):
		if request.method == "POST":
			form = MediaForm(request.POST, request.FILES)
			if form.is_valid():
				new_img=form.save(commit=False)
				new_img.author=request.user

				new_img.save()
				messages.info(request, f"Successfully uploaded the image")
				return redirect('homepage')
		else:
			form = MediaForm()
		return render(request, 'index.html', {"form": form})




class VideoModelCreateView(CreateView):
	model = VideoModel
	template_name = "videos.html"
	success_url='/'
	fields=('video',)


class MediaDriveaDeleteView(DeleteView):
	model=MediaDrivea
	success_url = "/"
	template_name = "confirm_delete.html"



class MediaDriveaUpdateView(UpdateView):
	model = MediaDrivea
	success_url="/"
	template_name = "update_template.html"
	fields = ("image",)
	
def recent(request):
	rec = MediaDrivea.objects.order_by('-created_document_timestamp')
	return render(request,'videos.html',{"rec":rec})

