# C1APIPolicyV1PoliciesUpdateResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |
| `update_policy_response`                                                              | [Optional[shared.UpdatePolicyResponse]](../../models/shared/updatepolicyresponse.md)  | :heavy_minus_sign:                                                                    | The UpdatePolicyResponse message contains the updated policy object.                  |