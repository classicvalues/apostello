# Generated by Django 2.0.3 on 2018-08-22 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("apostello", "0024_recipient_never_contact")]

    operations = [
        migrations.AlterUniqueTogether(name="cloudmessageid", unique_together=set()),
        migrations.RemoveField(model_name="cloudmessageid", name="user"),
        migrations.DeleteModel(name="CloudMessageId"),
    ]