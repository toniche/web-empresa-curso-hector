# Generated by Django 2.2.7 on 2019-11-29 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_orden'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title'], 'verbose_name': 'página', 'verbose_name_plural': 'páginas'},
        ),
        migrations.RenameField(
            model_name='page',
            old_name='orden',
            new_name='order',
        ),
    ]
