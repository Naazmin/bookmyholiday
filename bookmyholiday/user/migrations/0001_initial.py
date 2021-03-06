# Generated by Django 3.2 on 2021-05-30 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='hotels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotelname', models.CharField(max_length=60)),
                ('loaction', models.CharField(max_length=60)),
                ('ratings', models.IntegerField()),
                ('price', models.IntegerField()),
                ('himg', models.ImageField(blank=True, null=True, upload_to='hotelimg/')),
            ],
        ),
        migrations.CreateModel(
            name='vehicletype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vname', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('vtype', models.CharField(max_length=50)),
                ('seats', models.IntegerField()),
                ('vprice', models.IntegerField()),
                ('vimg', models.ImageField(blank=True, null=True, upload_to='vehicleimg/')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.destinations')),
                ('mtype', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.vehicletype')),
            ],
        ),
        migrations.CreateModel(
            name='userlogindata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=60)),
                ('pdesc', models.CharField(max_length=255)),
                ('paccomudation', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('pimg', models.ImageField(blank=True, null=True, upload_to='pkgimg/')),
                ('ratings', models.IntegerField(default=0)),
                ('pdestination', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.destinations')),
            ],
        ),
        migrations.CreateModel(
            name='mybookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('members', models.IntegerField()),
                ('source', models.CharField(max_length=60)),
                ('fromdate', models.DateField()),
                ('todate', models.DateField()),
                ('mhotle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.hotels')),
                ('mvehicle', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.vehicle')),
                ('pakage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.userlogindata')),
            ],
        ),
        migrations.CreateModel(
            name='Enquery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquerys', models.CharField(max_length=255)),
                ('reply', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
                ('startdate', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.userlogindata')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coment', models.CharField(max_length=255)),
                ('cratings', models.IntegerField()),
                ('pakage', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.package')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.userlogindata')),
            ],
        ),
    ]
