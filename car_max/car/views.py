from django.shortcuts import render
from . import models
from . import forms
from django.views.generic import DetailView
# Create your views here.

class DetailClassView(DetailView):
    model= models.Car
    pk_url_kwarg = 'id'
    template_name="car_details.html"

    def post(self,request,*args,**kwargs):
        car= self.get_object()
        if self.request.method=="POST": 
            comment_form=forms.CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment=comment_form.save(commit=False)
                new_comment.car=car
                new_comment.save()
            return self.get(request, *args,**kwargs)  
    

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        car=self.object
        comments=car.comments.all()
        comment_form=forms.CommentForm()
        context['comments']=comments
        context['comment_form'] = comment_form
        return context
