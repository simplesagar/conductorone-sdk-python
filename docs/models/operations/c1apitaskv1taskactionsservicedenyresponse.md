# C1APITaskV1TaskActionsServiceDenyResponse


## Fields

| Field                                                                                                                     | Type                                                                                                                      | Required                                                                                                                  | Description                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                            | *str*                                                                                                                     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `status_code`                                                                                                             | *int*                                                                                                                     | :heavy_check_mark:                                                                                                        | N/A                                                                                                                       |
| `raw_response`                                                                                                            | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                     | :heavy_minus_sign:                                                                                                        | N/A                                                                                                                       |
| `task_actions_service_deny_response`                                                                                      | [Optional[shared.TaskActionsServiceDenyResponse]](../../models/shared/taskactionsservicedenyresponse.md)                  | :heavy_minus_sign:                                                                                                        | The TaskActionsServiceDenyResponse returns a task view with paths indicating the location of expanded items in the array. |