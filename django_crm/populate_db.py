import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_project.settings')
django.setup()

from crm_app.models import Lead, Label, Activity, ActivityName

fake = Faker()

# Create some sample labels
labels = ['Hot', 'Cold', 'Warm', 'Interested', 'Not Interested']
for label_name in labels:
    Label.objects.get_or_create(name=label_name)

# Create some sample activity names
activity_names = ['Call', 'Email', 'Meeting', 'Follow-up', 'Demo']
for activity_name in activity_names:
    ActivityName.objects.get_or_create(name=activity_name)

# Get all created labels and activity names
all_labels = Label.objects.all()
all_activity_names = ActivityName.objects.all()

# Populate 10 random leads and associated activities
for _ in range(1000):
    lead = Lead(
        name=fake.name(),
        mobile=fake.phone_number(),
        email=fake.email(),
        source=fake.company(),
        notes=fake.text(),
        label=random.choice(all_labels)
    )
    lead.save()

    # For each lead, create 2-5 random activities
    for _ in range(random.randint(2, 5)):
        Activity(
            name=random.choice(all_activity_names),
            notes=fake.text(),
            lead=lead
        ).save()

print("Sample data populated!")
