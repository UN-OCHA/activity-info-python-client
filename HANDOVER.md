# Handover

- OpenAPI and package version: 2.0.4. Client regenerated with openapi-python-client 0.29.0.
- Added GET /form/{form_id}/record/{record_id} (get_record), with sync/async client functions and FormRecord/FormRecordFields models. Required response fields: formId, recordId, lastEditTime (number), and fields (arbitrary field values); parentRecordId is optional.
- Get record documents 401, 403, 404, and 410 with description-only error responses because the endpoint documentation does not specify error bodies. Existing global bearer authentication is retained.
- Previous 2.0.3 schema preserved byte-for-byte as activityinfo_openapi_2.0.3.json.
- Form schema/schemaVersion are optional for deleted or inaccessible forms; both schemaVersion properties use integers, matching actual API responses.
- Permission filters and field code/relevanceCondition/requiredCondition/validationCondition allow null. Permission name corrected to manageImportConfigurations.
- Default values support strings, numbers, string arrays, and geopoints; defaultValueFormula remains optional. Previous spec preserved as activityinfo_openapi_2.0.2.json.
- Validation: all 3 existing tests passed. Additional mocked checks passed for get_record sync/async calls, mixed field-value round-tripping, and documented error responses. Schema JSON, local references, unique operation IDs, change scope, and git diff whitespace checks passed. Generation completed without warnings.
- Run tests: uv tool run --from openapi-python-client==0.29.0 python -m unittest discover -s tests -v.
