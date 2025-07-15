#!/usr/bin/env python3
# get_dir_django_db_models.py

import django.db.models as models

# print("\nAttributes in django.db.models:")
# attrs = dir(models)
# for attr in sorted(attrs):
#     print(attr)


def print_attributes(module):
    print(f"\nAttributes in {module.__name__}:")
    attrs = dir(module)
    for attr in sorted(attrs):
        print(attr)


def save_attributes_to_file(module, filename):
    with open(filename, "w") as f:
        attrs = dir(module)
        for attr in sorted(attrs):
            f.write(f"{attr}\n")
    print(f"Attributes saved to {filename}")


def main():
    print_attributes(models)
    FILE_NAME = "django_db_models_attributes.txt"
    save_attributes_to_file(models, FILE_NAME)
    print("\nDjango DB Models module inspection complete.")
    print(f"Run 'cat {FILE_NAME}' to see the saved attributes.")


if __name__ == "__main__":
    main()
