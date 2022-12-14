# Generated by Django 4.1.2 on 2022-12-05 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_subjecte_delete_lesson_alter_student_subject_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('video', models.FileField(upload_to='videos/%y/%m/%d')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teacher.subject')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='teacher.subject'),
        ),
        migrations.DeleteModel(
            name='Subjecte',
        ),
    ]
