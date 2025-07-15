#!/usr/bin/env python3
# get_django_model_fields.py

import django.db.models as models

fields = [attr for attr in dir(models) if attr.endswith("Field")]
for f in sorted(fields):
    print(f)
