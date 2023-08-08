# AppUser

Application User that represents an account in the application.


## Fields

| Field                                                                     | Type                                                                      | Required                                                                  | Description                                                               |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `app_user_status`                                                         | [Optional[AppUserStatus]](../../models/shared/appuserstatus.md)           | :heavy_minus_sign:                                                        | The satus of the applicaiton user.                                        |
| `app_id`                                                                  | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | The ID of the application.                                                |
| `app_user_type`                                                           | [Optional[AppUserAppUserType]](../../models/shared/appuserappusertype.md) | :heavy_minus_sign:                                                        | The appplication user type. Type can be user, system or service.          |
| `created_at`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)      | :heavy_minus_sign:                                                        | N/A                                                                       |
| `deleted_at`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)      | :heavy_minus_sign:                                                        | N/A                                                                       |
| `display_name`                                                            | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | The display name of the application user.                                 |
| `email`                                                                   | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | The email field of the application user.                                  |
| `id`                                                                      | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | A unique idenditfier of the application user.                             |
| `identity_user_id`                                                        | *Optional[str]*                                                           | :heavy_minus_sign:                                                        | The conductor one user ID of the account owner.                           |
| `profile`                                                                 | dict[str, *Any*]                                                          | :heavy_minus_sign:                                                        | N/A                                                                       |
| `updated_at`                                                              | [date](https://docs.python.org/3/library/datetime.html#date-objects)      | :heavy_minus_sign:                                                        | N/A                                                                       |