## ✅ How to Find the Available Django Model Fields

- [Finding Django Model Fields - ChatGPT - Shared](https://chatgpt.com/share/6875e34d-27f4-8002-974f-3cccd87cae5d)

### 🔍 Option 1: **Official Django Documentation (Best Source)**

The most accurate and comprehensive list is in the official docs:

📚 [Django Model Field Reference](https://docs.djangoproject.com/en/stable/ref/models/fields/)

That page lists **all field types**, such as:

* `CharField`
* `TextField`
* `IntegerField`
* `BooleanField`
* `DateTimeField`
* `ForeignKey`
* `ManyToManyField`
* `OneToOneField`
* and many more…

---

### 🐍 Option 2: **Introspect a Model in Python Shell**

If you already have a model, you can explore its fields dynamically:

```bash
python manage.py shell
```

```python
from myapp.models import MyModel

for field in MyModel._meta.get_fields():
    print(field.name, type(field))
```

This shows the **field names** and **types**.

---

### ⚙️ Option 3: **List Field Classes Programmatically**

To see all the field classes available in Django, run:

```python
import django.db.models as models

fields = [attr for attr in dir(models) if attr.endswith('Field')]
for f in sorted(fields):
    print(f)
```

This will give you a list like:

```
AutoField
BigIntegerField
BinaryField
BooleanField
CharField
DateField
...
```

---

### 💡 Bonus: Use `help(models.CharField)` or `?` in IPython

You can dive deeper into any field like this:

```python
from django.db import models
help(models.CharField)
```

Or if you're using IPython:

```python
models.CharField?
```

---

Would you like a categorized cheat sheet next (e.g. string fields vs relationship fields), or a mini quiz to test your understanding as you learn?
