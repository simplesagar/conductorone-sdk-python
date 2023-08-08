# CreatePolicyRequest

The CreatePolicyRequest message is used to create a new policy.


## Fields

| Field                                                                                                                                       | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `description`                                                                                                                               | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | The description of the new policy.                                                                                                          |
| `display_name`                                                                                                                              | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | The display name of the new policy.                                                                                                         |
| `policy_steps`                                                                                                                              | dict[str, [PolicySteps](../../models/shared/policysteps.md)]                                                                                | :heavy_minus_sign:                                                                                                                          | The map of policy type to policy steps. The key is the stringified version of the enum. See other policies for examples.                    |
| `policy_type`                                                                                                                               | [Optional[C1APIPolicyV1CreatePolicyRequestPolicyType]](../../models/shared/c1apipolicyv1createpolicyrequestpolicytype.md)                   | :heavy_minus_sign:                                                                                                                          | The enum of the policy type.                                                                                                                |
| `post_actions`                                                                                                                              | list[[PolicyPostActions](../../models/shared/policypostactions.md)]                                                                         | :heavy_minus_sign:                                                                                                                          | Actions to occur after a policy finishes. As of now this is only valid on a certify policy to remediate a denied certification immediately. |
| `reassign_tasks_to_delegates`                                                                                                               | *Optional[bool]*                                                                                                                            | :heavy_minus_sign:                                                                                                                          | Allows reassigning tasks to delegates.                                                                                                      |