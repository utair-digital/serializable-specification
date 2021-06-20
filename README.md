[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Serializable specification

---
**Source Code**: <a href="https://github.com/utair-digital/serializable-specification" target="_blank">https://github.com/utair-digital/serializable-specification</a>

---

<p align="center">
    <em>Serializable specification is an easy way to save your logical expressions to storage.</em>
</p>

## Installation

```console
$ pip install git+git://github.com/utair-digital/serializable-specification
```

## Example

For example you want to choose a specific motorbike (let's say it will be BMW or Harley, it's max speed is more than 80 km/h, it's gearbox type is one of ["dog_box", "sequential"] and the max speed of it's second gear is 1000). Then, our specification will be look like this.

```Python
from specification import (
    AndSpecification,
    AttributeSpecification,
    OrSpecification,
    NotSpecification
)

bmw_or_harley_transport_over_80_spec = AndSpecification(
    AttributeSpecification("speed", "gt", 80),
    OrSpecification(
        AttributeSpecification("model", "eq", "bmw"),
        AttributeSpecification("model", "eq", "harley"),
    ),
    AttributeSpecification("gearbox.type", "in", ["dog_box", "sequential"]),

    # Same as AttributeSpecification("gearbox.gears.second.max", "ne", 1000)
    NotSpecification(
        AttributeSpecification("gearbox.gears.second.max", "eq", 1000)
    ),
)
```

**for getting nested object you must use dot**

## Serialize specification to json

**It looks like this**

```python
bmw_or_harley_transport_over_80_spec_serialized = {
    "and": [
        {
            "key": "speed",
            "op": "gt",
            "value": 80,
            "aggregation": None,
            "discover_attribute": True
        },
        {
            "or": [
                {
                    "key": "model",
                    "op": "eq",
                    "value": "bmw",
                    "aggregation": None,
                    "discover_attribute": True
                },
                {
                    "key": "model",
                    "op": "eq",
                    "value": "harley",
                    "aggregation": None,
                    "discover_attribute": True
                }
            ]
        },
        {
            "key": "gearbox.type",
            "op": "in",
            "value": [
                "dog_box",
                "sequential"
            ],
            "aggregation": None,
            "discover_attribute": True
        },
        {
            "not": {
                "key": "gearbox.gears.second.max",
                "op": "eq",
                "value": 1000,
                "aggregation": None,
                "discover_attribute": True
            }
        }
    ]
}
```

## Deserialize specification into object

you can use the serialized specification from the previous example

```python
spec = AndSpecification.deserialize(bmw_or_harley_transport_over_80_spec_serialized)
filtered = list(filter(spec.is_satisfied_by, transports))
print(filtered)
```

## License

This project is licensed under the [Apache-2.0 License](LICENSE).