import unittest

import httpx

from activity_info_api_client import Client
from activity_info_api_client.api.default import get_form_schema, update_form_schema
from activity_info_api_client.models import FormSchema, FormSchemaElement, GeoPointDefaultValue
from activity_info_api_client.types import UNSET


class FormSchemaDefaultsTests(unittest.TestCase):
    def test_defaults_round_trip_through_get_and_update(self):
        cases = [
            ("FREE_TEXT", "Hello", None),
            ("FREE_TEXT", UNSET, 'LEFT("Hello", 2)'),
            ("NARRATIVE", "Hello", None),
            ("NARRATIVE", UNSET, 'LEFT("Hello", 2)'),
            ("quantity", 888, None),
            ("quantity", UNSET, 'VALUE("123")'),
            ("enumerated", "option1", None),
            ("enumerated", ["option1", "option2"], None),
            ("reference", "form:record", None),
            ("reference", "database@users:6027875378528256", None),
            ("date", "2026-11-16", None),
            ("geopoint", {"latitude": 23, "longitude": -23}, None),
            ("date", UNSET, "TODAY()"),
            ("epiweek", "2026W46", None),
            ("fortnight", "2026W45", None),
            ("month", "2025-10", None),
            ("quantity", 42.5, None),
        ]
        elements = []
        for i, (type_, value, formula) in enumerate(cases):
            field = {"id": f"field{i}", "label": f"Field {i}", "required": False,
                     "type": type_, "description": None}
            if value is not UNSET:
                field["defaultValue"] = value
            if formula is not None:
                field["defaultValueFormula"] = formula
            elements.append(field)
        payload = {"id": "form", "label": "Defaults", "databaseId": "database",
                   "schemaVersion": 4, "elements": elements}
        response = httpx.Response(200, json=payload)
        model = get_form_schema._parse_response(client=Client(base_url="https://example.org"), response=response)
        self.assertIsInstance(model, FormSchema)
        self.assertIsInstance(model.elements[11].default_value, GeoPointDefaultValue)
        self.assertEqual(model.elements[11].default_value.latitude, 23)
        output = update_form_schema._get_kwargs("form", body=model)["json"]
        for original, parsed, serialized in zip(elements, model.elements, output["elements"]):
            with self.subTest(type=original["type"], id=original["id"]):
                self.assertIsNone(parsed.description)
                self.assertIsNone(serialized["description"])
                for key in ("defaultValue", "defaultValueFormula"):
                    if key in original:
                        self.assertEqual(serialized[key], original[key])
                        self.assertIs(type(serialized[key]), type(original[key]))
                    else:
                        self.assertNotIn(key, serialized)

    def test_omitted_defaults_and_description_stay_omitted(self):
        model = FormSchemaElement.from_dict({"id": "field", "label": "Field", "required": False,
                                            "type": "FREE_TEXT"})
        for key in ("defaultValue", "defaultValueFormula", "description"):
            self.assertNotIn(key, model.to_dict())

    def test_literal_and_formula_can_coexist(self):
        model = FormSchemaElement.from_dict({"id": "field", "label": "Field", "required": False,
                                            "type": "quantity", "defaultValue": 888,
                                            "defaultValueFormula": 'VALUE("123")'})
        self.assertEqual(model.to_dict()["defaultValue"], 888)
        self.assertEqual(model.to_dict()["defaultValueFormula"], 'VALUE("123")')


if __name__ == "__main__":
    unittest.main()
