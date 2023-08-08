# AppResourceServiceGetResponse

The app resource service get response contains the app resource view and array of expanded items indicated by the request's expand mask.


## Fields

| Field                                                                                                                                                                                               | Type                                                                                                                                                                                                | Required                                                                                                                                                                                            | Description                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `app_resource_view`                                                                                                                                                                                 | [Optional[AppResourceView]](../../models/shared/appresourceview.md)                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                  | The app resource view returns an app resource with paths for items in the expand mask filled in when this response is returned and a request expand mask has "*" or "app_id" or "resource_type_id". |
| `expanded`                                                                                                                                                                                          | list[dict[str, *Any*]]                                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                  | List of serialized related objects.                                                                                                                                                                 |