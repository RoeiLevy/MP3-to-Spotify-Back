from django.db import models

class UserSession(models.Model):
    spotify_user_id=models.CharField(max_length=50)
    spotify_user_locale=models.CharField(max_length=50)
    playlist_id=models.CharField(max_length=50)
    uploaded_files_count=models.IntegerField()
    failed_files_count=models.IntegerField()
    succeeded_files_count=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)