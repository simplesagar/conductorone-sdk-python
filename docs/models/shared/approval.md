# Approval

The Approval message.

This message contains a oneof named typ. Only a single field of the following list may be set at a time:
  - users
  - manager
  - appOwners
  - group
  - self
  - entitlementOwners



## Fields

| Field                                                                                                                                           | Type                                                                                                                                            | Required                                                                                                                                        | Description                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `app_group_approval`                                                                                                                            | [Optional[AppGroupApproval]](../../models/shared/appgroupapproval.md)                                                                           | :heavy_minus_sign:                                                                                                                              | The AppGroupApproval object provides the configuration for setting a group as the approvers of an approval policy step.                         |
| `app_owner_approval`                                                                                                                            | [Optional[AppOwnerApproval]](../../models/shared/appownerapproval.md)                                                                           | :heavy_minus_sign:                                                                                                                              | App owner approval provides the configuration for an approval step when the app owner is the target.                                            |
| `entitlement_owner_approval`                                                                                                                    | [Optional[EntitlementOwnerApproval]](../../models/shared/entitlementownerapproval.md)                                                           | :heavy_minus_sign:                                                                                                                              | The entitlement owner approval allows configuration of the approval step when the target approvers are the entitlement owners.                  |
| `manager_approval`                                                                                                                              | [Optional[ManagerApproval]](../../models/shared/managerapproval.md)                                                                             | :heavy_minus_sign:                                                                                                                              | The manager approval object provides configuration options for approval when the target of the approval is the manager of the user in the task. |
| `self_approval`                                                                                                                                 | [Optional[SelfApproval]](../../models/shared/selfapproval.md)                                                                                   | :heavy_minus_sign:                                                                                                                              | The self approval object describes the configuration of a policy step that needs to be approved by the target of the request.                   |
| `user_approval`                                                                                                                                 | [Optional[UserApproval]](../../models/shared/userapproval.md)                                                                                   | :heavy_minus_sign:                                                                                                                              | The user approval object describes the approval configuration of a policy step that needs to be approved by a specific list of users.           |
| `allow_reassignment`                                                                                                                            | *Optional[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to allow reassignment by reviewers during this step.                                                                              |
| `assigned`                                                                                                                                      | *Optional[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                              | A field indicating whether this step is assigned.                                                                                               |
| `require_approval_reason`                                                                                                                       | *Optional[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to require a reason when approving this step.                                                                                     |
| `require_reassignment_reason`                                                                                                                   | *Optional[bool]*                                                                                                                                | :heavy_minus_sign:                                                                                                                              | Configuration to require a reason when reassigning this step.                                                                                   |