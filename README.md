# Django Model Inspector

> Python scripts to explore and understand Django model attributes.

## Features

- List all field names and their types
- Display related objects (ForeignKey, OneToOne, etc.)
- Works with Pipenv for easy setup

## Setup

```bash
pipenv install
pipenv shell
````

## Usage

```bash
python inspect_fields.py
python list_related_objects.py
```

## Notes

* You must set up Django settings to point to your model project.
* Designed for exploration and learning.
