# FOLLOWING EXAMPLE SHOULD RUN AS IS WITH PYTHON 3.7+


from dto import Car, Moto

from specification import (
    AttributeSpecification,
    AndSpecification,
    OrSpecification,
    NotSpecification
)

gearbox = {
    "type": "sequential",
    "gears": [

    ]
}


transports = [
    Car("tesla", 300, gearbox),
    Car("zhiguli", 120, gearbox),
    Moto("jupiter", 90, gearbox),
    Moto("harley", 90, {
        "type": "dog_box",
        "gears": [
            {"first": {"min": 100, "max": 300}},
            {"second": {"min": 300, "max": 1000}},
        ]
    }),

    # Looking for:
    Moto("bmw", 190, gearbox),
    Moto("bmw", 210, gearbox),
    Car("bmw", 220, gearbox),
]


bmw_or_harley_transport_over_80_spec = AndSpecification(
    AttributeSpecification("speed", "gt", 80),
    OrSpecification(
        AttributeSpecification("model", "eq", "bmw"),
        AttributeSpecification("model", "eq", "harley"),
    ),
    AttributeSpecification("gearbox.type", "in", ["dog_box", "sequential"]),

    # Same as AttributeSpecification("gearbox.gears.second.max", "ne", 1000)
    NotSpecification(
        OrSpecification(
            AttributeSpecification("gearbox.gears.second.max", "eq", 1000)
        )
    ),
)

filtered = list(filter(bmw_or_harley_transport_over_80_spec.is_satisfied_by, transports))
print(filtered)

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

spec = AndSpecification.deserialize(bmw_or_harley_transport_over_80_spec_serialized)
filtered = list(filter(spec.is_satisfied_by, transports))
print(filtered)
