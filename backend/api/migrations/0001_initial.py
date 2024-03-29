# Generated by Django 3.2.3 on 2021-06-12 18:37

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswersOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(verbose_name='Значение варианта ответа в виде текста')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(blank=True, default='name', max_length=765)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone', models.CharField(max_length=16)),
                ('full_name', models.CharField(max_length=255)),
                ('home_country', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('tag', models.CharField(default='имя', max_length=100, primary_key=True, serialize=False, verbose_name='Тег (Суть)')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('type', models.TextField(choices=[('selected', 'Selected'), ('range', 'Range'), ('textarea', 'Textarea'), ('message', 'Message'), ('datapicker', 'Datapicker'), ('switch', 'Switch')])),
            ],
        ),
        migrations.CreateModel(
            name='Stack',
            fields=[
                ('name', models.CharField(default='Django', max_length=150, primary_key=True, serialize=False, verbose_name='Название технологии')),
                ('avg_price', models.FloatField(blank=True, null=True)),
                ('avg_days', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.customuser')),
                ('business_name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('api.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='test project', max_length=150, null=True, verbose_name='Название Проекта')),
                ('is_active', models.BooleanField(default=True)),
                ('predicted_price', models.IntegerField(blank=True, null=True)),
                ('real_price', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('predict_end_date', models.DateField(blank=True, null=True)),
                ('real_end_date', models.DateField(blank=True, null=True)),
                ('stack', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='api.stack')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('custom_answer', models.ManyToManyField(related_name='selected_answers_option', to='api.AnswersOption')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_answers', to='api.project')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api.question')),
            ],
        ),
        migrations.AddField(
            model_name='answersoption',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers_option', to='api.question'),
        ),
    ]
