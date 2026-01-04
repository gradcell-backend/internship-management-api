from django.core.exceptions import ValidationError


def validate_resume(value):
    allowed_extensions = (".pdf", ".doc", ".docx")
    max_size = 2 * 1024 * 1024  # 2MB

    if not value.name.lower().endswith(allowed_extensions):
        raise ValidationError("Only PDF or Word documents are allowed.")

    if value.size > max_size:
        raise ValidationError("Resume file must be under 2MB.")
