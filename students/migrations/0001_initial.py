from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admission_no', models.CharField(db_index=True, max_length=40, unique=True)),
                ('full_name', models.CharField(max_length=150)),
                ('course_code', models.CharField(max_length=30)),
                ('campus', models.CharField(max_length=80)),
                ('supervisor', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={'ordering': ['admission_no']},
        ),
    ]
