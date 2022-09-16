from keyword import kwlist
import os
import shutil
from django.db import models
import pyrebase
from decouple import config
from instituto_ls_project.settings import APIKEY, APPID, AUTHDOMAIN, GMAIL, GMAIL_PWD, MESSAGINGSENDERID, PROJECTID, STORAGEBUCKET

# Method to save files on Firebase
def firebase_save(super, file_field, file_folder, file_name, *args, **kwargs):
        """overrides the instance.save method, uploading media file to Firebase and retreaving it's URL"""

        firebase_config = {
            'apiKey': APIKEY,
            'authDomain': AUTHDOMAIN,
            'projectId': PROJECTID,
            'storageBucket': STORAGEBUCKET,
            'messagingSenderId': MESSAGINGSENDERID,
            'appId': APPID,
            'databaseURL': "",
        }

        firebase = pyrebase.initialize_app(firebase_config)
        storage = firebase.storage()
        auth = firebase.auth()
        user = auth.sign_in_with_email_and_password(email=GMAIL, password=GMAIL_PWD)

        # update the database saving file to temp media folder on WebServer (will be deleted soon...)
        super.save(*args, **kwargs)
        
        # upload the file from media folder to Firebase on child(/media/hero/<hero_name>)
        # try/except to ignore errors in case of saving the model without uploading new image
        try:
            child = f'{file_folder}/{file_name}'
            storage.child(child).put(file_field.path, user['idToken'])
        except FileNotFoundError:
            pass
        
        # turn self.cover into string containing the URL file from Firebase
        file_field = storage.child(child).get_url(None)
        
        # update the database saving the files's URL
        # super.save(*args, **kwargs)

        # delete temp media folder on WebServer
        # try/except to ignore errors in case of saving the model without uploading new image
        try:    
            shutil.rmtree('media')
        except FileNotFoundError:
            pass

        return file_field

class Product(models.Model):
    cover = models.ImageField(verbose_name='Imagem', upload_to='products')
    title = models.CharField(verbose_name='Título', max_length=60)
    description = models.CharField(verbose_name='Descrição', max_length=95)
    know_more = models.TextField(verbose_name='Saiba mais', max_length=2000)
    index = models.IntegerField()

    class Meta:
        ordering = ['-index']
        verbose_name_plural = "Produtos"

    def save(self):
        self.cover = firebase_save(super=super(), file_field=self.cover, file_folder='media/products', file_name=self.title)
        super().save()

    def __str__(self) -> str:
        return self.description


class Hero(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=80)
    cover = models.ImageField(verbose_name="Foto com fundo transparente", upload_to='hero')
    bio = models.TextField(verbose_name='Biografia suscinta', max_length=150)

    class Meta:
        verbose_name_plural = 'Herois'
    
    def save(self):
        self.cover = firebase_save(super=super(), file_field=self.cover, file_folder='media/hero', file_name=self.name)
        super().save()
    


    #     """overrides the save method, uploading media file to Firebase and retreaving it's URL"""

    #     firebase_config = {
    #         'apiKey': APIKEY,
    #         'authDomain': AUTHDOMAIN,
    #         'projectId': PROJECTID,
    #         'storageBucket': STORAGEBUCKET,
    #         'messagingSenderId': MESSAGINGSENDERID,
    #         'appId': APPID,
    #         'databaseURL': "",
    #     }

    #     firebase = pyrebase.initialize_app(firebase_config)
    #     storage = firebase.storage()
    #     auth = firebase.auth()
    #     user = auth.sign_in_with_email_and_password(email=GMAIL, password=GMAIL_PWD)

    #     # update the database saving file to temp media folder on WebServer (will be deleted soon...)
    #     super().save(*args, **kwargs)
        
    #     # upload the file from media folder to Firebase on child(/media/hero/<hero_name>)
    #     # try/except to ignore errors in case of saving the model without uploading new image
    #     try:
    #         child = f'media/hero/{self.name}'
    #         storage.child(child).put(self.cover.path, user['idToken'])
    #     except FileNotFoundError:
    #         pass
        
    #     # turn self.cover into string containing the URL file from Firebase
    #     self.cover = storage.child(child).get_url(None)
        
    #     # update the database saving the files's URL
    #     super().save(*args, **kwargs)

    #     # delete temp media folder on WebServer
    #     # try/except to ignore errors in case of saving the model without uploading new image
    #     try:    
    #         shutil.rmtree('media/hero/')
    #     except FileNotFoundError:
    #         pass
    
    def __str__(self) -> str:
        return self.name


class Feedback(models.Model):
    video_iframe = models.TextField(verbose_name='iFrame de Video', blank=True, null=True)
    image_iframe = models.TextField(verbose_name='iFrame de Imagem', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return 'iFrames para Feedbacks'


