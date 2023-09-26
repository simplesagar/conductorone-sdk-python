# C1APIRequestcatalogV1RequestCatalogManagementServiceListResponse


## Fields

| Field                                                                                                                              | Type                                                                                                                               | Required                                                                                                                           | Description                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                                     | *str*                                                                                                                              | :heavy_check_mark:                                                                                                                 | HTTP response content type for this operation                                                                                      |
| `request_catalog_management_service_list_response`                                                                                 | [Optional[shared.RequestCatalogManagementServiceListResponse]](../../models/shared/requestcatalogmanagementservicelistresponse.md) | :heavy_minus_sign:                                                                                                                 | Successful response                                                                                                                |
| `status_code`                                                                                                                      | *int*                                                                                                                              | :heavy_check_mark:                                                                                                                 | HTTP response status code for this operation                                                                                       |
| `raw_response`                                                                                                                     | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                              | :heavy_minus_sign:                                                                                                                 | Raw HTTP response; suitable for custom response parsing                                                                            |