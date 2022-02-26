from ast import Import
from binascii import Incomplete
from dataclasses import field, fields
from msilib.schema import Class
from pyexpat import model
from tkinter import Widget
from turtle import title
from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):


    class Meta():
        fields= '__all__'
        model = Post
        field = ('author','title','text')

        Widget = {
            'title':forms.TextInput(attrs={'class': 'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):

    class Meta():
        fields= '__all__'
        model = Comment
        field = ('author','text')

        Widget = {
            'author':forms.TextInput(attrs={'Class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
        }
        
            
    
        
        
            


    
    
        




