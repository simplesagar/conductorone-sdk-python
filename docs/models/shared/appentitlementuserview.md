# AppEntitlementUserView

The AppEntitlementUserView (aka grant view) describes the relationship between an app user and an entitlement. They have more recently been referred to as grants.


## Fields

| Field                                                                                                              | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `app_user_view`                                                                                                    | [Optional[AppUserView]](../../models/shared/appuserview.md)                                                        | :heavy_minus_sign:                                                                                                 | The AppUserView contains an app user as well as paths for apps, identity users, and last usage in expanded arrays. |
| `app_entitlement_user_binding_created_at`                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                               | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |
| `app_entitlement_user_binding_deprovision_at`                                                                      | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                               | :heavy_minus_sign:                                                                                                 | N/A                                                                                                                |