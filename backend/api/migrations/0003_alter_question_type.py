

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_customeranswer_custom_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.TextField(choices=[('selected', 'Selected'), ('range', 'Range'), ('textarea', 'Textarea'), ('message', 'Message'), ('datapicker', 'Datapicker'), ('switch', 'Switch'), ('checkbox', 'Checkbox')]),
        ),
    ]
