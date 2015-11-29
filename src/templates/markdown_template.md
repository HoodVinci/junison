***

# {{class_.name()}}

***

## Description
> **{{class_.description()}}**

***

## Heritage

{% for super in class_.get_inheritance_tree() %}
{{super}}  /  {% endfor %}

***

## Champs de {{class_.name()}}

Classe |Type | Nom | Description
--|---|---|---
{% for field in class_.fields %}
{{field.class_name()}}|{{field.type()}}|{{field.name()}}|{{field.description()}}
{% endfor %}




## Enums Utilisés
{% for enum in class_.enums%}
### {{enum.name()}}
#### Valeurs possibles
{% for item in enum.items()  %}* __{{item}}__
{% endfor %}  


{% endfor %}

## Exemple

```json
{{class_.get_exemple_data()}}
```

## Java
```java
{{class_.java_code}}
```

## Php
```php
{{class_.php_code}}
```