from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.db.utils import IntegrityError
from SDPapp.models import Department

@receiver(post_migrate)
def ensure_default_departments(sender, **kwargs):
    departments = {
        "Computer Science": "cs",
        "Information Systems": "is",
        "Information Technology": "it",
        "Business Administration": "ba"
    }

    for name, code in departments.items():
        try:
            dept, created = Department.objects.get_or_create(
                code=code,
                defaults={"name": name}
            )
            if created:
                print(f"✅ Created department: {name} ({code})")
            else:
                if dept.name != name:
                    dept.name = name
                    dept.save()
                    print(f"♻️ Updated department name for code '{code}' to '{name}'")
                else:
                    print(f"✔️ Department already exists: {name} ({code})")
        except IntegrityError:
            print(f"❌ Error creating or updating department: {name} ({code})")
