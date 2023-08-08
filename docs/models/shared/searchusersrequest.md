# SearchUsersRequest

Search for users based on some filters.


## Fields

| Field                                                                                                                                                                                                 | Type                                                                                                                                                                                                  | Required                                                                                                                                                                                              | Description                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user_expand_mask`                                                                                                                                                                                    | [Optional[UserExpandMask]](../../models/shared/userexpandmask.md)                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | The user expand mask is used to indicate which related objects should be expanded in the response.<br/> The supported paths are 'role_ids', 'manager_ids', 'delegated_user_id', 'directory_ids', and '*'. |
| `email`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Search for users based on their email (exact match).                                                                                                                                                  |
| `exclude_ids`                                                                                                                                                                                         | list[*str*]                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                    | An array of users IDs to exclude from the results.                                                                                                                                                    |
| `ids`                                                                                                                                                                                                 | list[*str*]                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                    | Deprecated. Use refs array instead.                                                                                                                                                                   |
| `page_size`                                                                                                                                                                                           | *Optional[float]*                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                    | The pageSize where 0 <= pageSize <= 100. Values < 10 will be set to 10. A value of 0 returns the default page size (currently 25)                                                                     |
| `page_token`                                                                                                                                                                                          | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | The pageToken field.                                                                                                                                                                                  |
| `query`                                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | Query the apps with a fuzzy search on display name and emails.                                                                                                                                        |
| `refs`                                                                                                                                                                                                | list[[UserRef](../../models/shared/userref.md)]                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                    | An array of user refs to restrict the return values to by ID.                                                                                                                                         |
| `role_ids`                                                                                                                                                                                            | list[*str*]                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                    | Search for users that have any of the role IDs on this list.                                                                                                                                          |
| `user_statuses`                                                                                                                                                                                       | list[[SearchUsersRequestUserStatuses](../../models/shared/searchusersrequestuserstatuses.md)]                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                    | Search for users that have any of the statuses on this list. This can only be ENABLED, DISABLED, and DELETED                                                                                          |