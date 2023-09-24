import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_project.settings')  # Replace 'your_project_name' with your actual project name
django.setup()

from crm_app.models import Lead, Label

def populate_leads_from_tsv(file_path):
    # Ensure the "warm" label exists
    label, _ = Label.objects.get_or_create(name="warm")

    with open(file_path, 'r') as file:
        for line in file:
            try:
            # Split the line into its components
                lead_date, source, lead_name, mobile, loc, occupation, notes = line.strip().split('\t')

            # Create the lead
            
                lead = Lead(
                    date=lead_date,
                    source=source,
                    name=lead_name,
                    mobile=mobile,
                    location=loc,
                    occupation=occupation,
                    notes=notes,
                    label=label
                )
                lead.save()
            except Exception as e:
                if("UNIQUE" not in str(e)):
                    print(e , line)

if __name__ == "__main__":
    file_path = input("Enter the path to the TSV file: ")
    populate_leads_from_tsv(file_path)
    print("Data populated successfully!")
