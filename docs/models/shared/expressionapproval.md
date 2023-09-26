# ExpressionApproval

The ExpressionApproval message.


## Fields

| Field                                                                                                                            | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `allow_self_approval`                                                                                                            | *Optional[bool]*                                                                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to allow self approval of if the user is specified and also the target of the ticket.                              |
| `assigned_user_ids`                                                                                                              | list[*str*]                                                                                                                      | :heavy_minus_sign:                                                                                                               | The assignedUserIds field.                                                                                                       |
| `expressions`                                                                                                                    | list[*str*]                                                                                                                      | :heavy_minus_sign:                                                                                                               | Array of dynamic expressions to determine the approvers.  The first expression to return a non-empty list of users will be used. |
| `fallback`                                                                                                                       | *Optional[bool]*                                                                                                                 | :heavy_minus_sign:                                                                                                               | Configuration to allow a fallback if the expression does not return a valid list of users.                                       |
| `fallback_user_ids`                                                                                                              | list[*str*]                                                                                                                      | :heavy_minus_sign:                                                                                                               | Configuration to specific which users to fallback to if and the expression does not return a valid list of users.                |