# Generated by Django 3.0.4 on 2020-03-24 12:22

from django.db import migrations, models
import psqlextra.manager.manager
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('coronavirus_bg', '0001_Individuals_and_Totals_schema'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.CharField(blank=True, max_length=1000, null=True, verbose_name='twitter_api_user_id')),
                ('tweet_id', models.CharField(blank=True, max_length=1000, null=True, verbose_name='twitter_api_tweet_id')),
                ('datetime', models.DateTimeField(blank=True, null=True, verbose_name='twitter_api_datetime')),
                ('text', models.CharField(blank=True, max_length=1000, null=True, verbose_name='full_tweet_text')),
                ('url', models.CharField(blank=True, max_length=1000, null=True, verbose_name='full_tweet_url')),
                ('total_cases_bg', models.IntegerField(blank=True, null=True, verbose_name='total_cases_infected_bulgaria')),
            ],
            options={
                'db_table': 'tweets',
                'unique_together': {('tweet_id', 'datetime')},
            },
            managers=[
                ('objects', psqlextra.manager.manager.PostgresManager()),
            ],
        ),
    ]
