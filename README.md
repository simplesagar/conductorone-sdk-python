# openapi

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/ConductorOne/conductorone-sdk-python.git
```
<!-- End SDK Installation -->


```python
import sdk
from sdk.models import shared

s = sdk.SDKWithCredentials("CLIENT_ID", "CLIENT_SECRET")

req = shared.AppEntitlementSearchServiceSearchRequest(
    app_entitlement_expand_mask=shared.AppEntitlementExpandMask(
        paths=[
            'provident',
            'distinctio',
            'quibusdam',
        ],
    ),
    access_review_id='unde',
    alias='nulla',
    app_ids=[
        'illum',
        'vel',
        'error',
    ],
    app_user_ids=[
        'suscipit',
        'iure',
        'magnam',
    ],
    compliance_framework_ids=[
        'ipsa',
        'delectus',
        'tempora',
        'suscipit',
    ],
    exclude_app_ids=[
        'minus',
        'placeat',
    ],
    exclude_app_user_ids=[
        'iusto',
        'excepturi',
        'nisi',
    ],
    only_get_expiring=False,
    page_size=9255.97,
    page_token='temporibus',
    query='ab',
    resource_type_ids=[
        'veritatis',
        'deserunt',
    ],
    risk_level_ids=[
        'ipsam',
    ],
)

res = s.app_entitlement_search.search(req)

if res.app_entitlement_search_service_search_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [app_entitlement_search](docs/sdks/appentitlementsearch/README.md)

* [search](docs/sdks/appentitlementsearch/README.md#search) - Search

### [app_entitlement_user_binding](docs/sdks/appentitlementuserbinding/README.md)

* [list_app_users_for_identity_with_grant](docs/sdks/appentitlementuserbinding/README.md#list_app_users_for_identity_with_grant) - List App Users For Identity With Grant

### [app_entitlements](docs/sdks/appentitlements/README.md)

* [get](docs/sdks/appentitlements/README.md#get) - Get
* [list](docs/sdks/appentitlements/README.md#list) - List
* [list_for_app_resource](docs/sdks/appentitlements/README.md#list_for_app_resource) - List For App Resource
* [list_for_app_user](docs/sdks/appentitlements/README.md#list_for_app_user) - List For App User
* [list_groups](docs/sdks/appentitlements/README.md#list_groups) - List Groups
* [list_users](docs/sdks/appentitlements/README.md#list_users) - List Users
* [update](docs/sdks/appentitlements/README.md#update) - Update

### [app_owners](docs/sdks/appowners/README.md)

* [add](docs/sdks/appowners/README.md#add) - Add
* [list](docs/sdks/appowners/README.md#list) - List
* [remove](docs/sdks/appowners/README.md#remove) - Remove

### [app_report](docs/sdks/appreport/README.md)

* [list](docs/sdks/appreport/README.md#list) - List

### [app_report_action](docs/sdks/appreportaction/README.md)

* [generate_report](docs/sdks/appreportaction/README.md#generate_report) - Generate Report

### [app_resource](docs/sdks/appresource/README.md)

* [get](docs/sdks/appresource/README.md#get) - Get
* [list](docs/sdks/appresource/README.md#list) - List

### [app_resource_owners](docs/sdks/appresourceowners/README.md)

* [list](docs/sdks/appresourceowners/README.md#list) - List

### [app_resource_search](docs/sdks/appresourcesearch/README.md)

* [search_app_resource_types](docs/sdks/appresourcesearch/README.md#search_app_resource_types) - Search App Resource Types

### [app_resource_type](docs/sdks/appresourcetype/README.md)

* [get](docs/sdks/appresourcetype/README.md#get) - Get
* [list](docs/sdks/appresourcetype/README.md#list) - List

### [app_search](docs/sdks/appsearch/README.md)

* [search](docs/sdks/appsearch/README.md#search) - Search

### [app_usage_controls](docs/sdks/appusagecontrols/README.md)

* [get](docs/sdks/appusagecontrols/README.md#get) - Get
* [update](docs/sdks/appusagecontrols/README.md#update) - Update

### [apps](docs/sdks/apps/README.md)

* [create](docs/sdks/apps/README.md#create) - Create
* [delete](docs/sdks/apps/README.md#delete) - Delete
* [get](docs/sdks/apps/README.md#get) - Get
* [list](docs/sdks/apps/README.md#list) - List
* [update](docs/sdks/apps/README.md#update) - Update

### [auth](docs/sdks/auth/README.md)

* [introspect](docs/sdks/auth/README.md#introspect) - Introspect

### [connector](docs/sdks/connector/README.md)

* [create](docs/sdks/connector/README.md#create) - Create
* [create_delegated](docs/sdks/connector/README.md#create_delegated) - Create Delegated
* [delete](docs/sdks/connector/README.md#delete) - Delete
* [get](docs/sdks/connector/README.md#get) - Get
* [get_credentials](docs/sdks/connector/README.md#get_credentials) - Get Credentials
* [list](docs/sdks/connector/README.md#list) - List
* [revoke_credential](docs/sdks/connector/README.md#revoke_credential) - Revoke Credential
* [rotate_credential](docs/sdks/connector/README.md#rotate_credential) - Rotate Credential
* [update](docs/sdks/connector/README.md#update) - Update
* [update_delegated](docs/sdks/connector/README.md#update_delegated) - Update Delegated

### [directory](docs/sdks/directory/README.md)

* [create](docs/sdks/directory/README.md#create) - Create
* [delete](docs/sdks/directory/README.md#delete) - Delete
* [get](docs/sdks/directory/README.md#get) - Get
* [list](docs/sdks/directory/README.md#list) - List

### [personal_client](docs/sdks/personalclient/README.md)

* [create](docs/sdks/personalclient/README.md#create) - Create

### [policies](docs/sdks/policies/README.md)

* [create](docs/sdks/policies/README.md#create) - Create
* [delete](docs/sdks/policies/README.md#delete) - Delete
* [get](docs/sdks/policies/README.md#get) - Get
* [list](docs/sdks/policies/README.md#list) - List
* [update](docs/sdks/policies/README.md#update) - Update

### [policy_search](docs/sdks/policysearch/README.md)

* [search](docs/sdks/policysearch/README.md#search) - Search

### [request_catalog_management](docs/sdks/requestcatalogmanagement/README.md)

* [add_access_entitlements](docs/sdks/requestcatalogmanagement/README.md#add_access_entitlements) - Add Access Entitlements
* [add_app_entitlements](docs/sdks/requestcatalogmanagement/README.md#add_app_entitlements) - Add App Entitlements
* [create](docs/sdks/requestcatalogmanagement/README.md#create) - Create
* [delete](docs/sdks/requestcatalogmanagement/README.md#delete) - Delete
* [get](docs/sdks/requestcatalogmanagement/README.md#get) - Get
* [list_entitlements_for_access](docs/sdks/requestcatalogmanagement/README.md#list_entitlements_for_access) - List Entitlements For Access
* [list_entitlements_per_catalog](docs/sdks/requestcatalogmanagement/README.md#list_entitlements_per_catalog) - List Entitlements Per Catalog
* [remove_access_entitlements](docs/sdks/requestcatalogmanagement/README.md#remove_access_entitlements) - Remove Access Entitlements
* [remove_app_entitlements](docs/sdks/requestcatalogmanagement/README.md#remove_app_entitlements) - Remove App Entitlements
* [update](docs/sdks/requestcatalogmanagement/README.md#update) - Update

### [request_catalog_search](docs/sdks/requestcatalogsearch/README.md)

* [search_entitlements](docs/sdks/requestcatalogsearch/README.md#search_entitlements) - Search Entitlements

### [roles](docs/sdks/roles/README.md)

* [get](docs/sdks/roles/README.md#get) - Get
* [list](docs/sdks/roles/README.md#list) - List
* [update](docs/sdks/roles/README.md#update) - Update

### [task](docs/sdks/task/README.md)

* [create_grant_task](docs/sdks/task/README.md#create_grant_task) - Create Grant Task
* [create_revoke_task](docs/sdks/task/README.md#create_revoke_task) - Create Revoke Task
* [get](docs/sdks/task/README.md#get) - Get

### [task_actions](docs/sdks/taskactions/README.md)

* [approve](docs/sdks/taskactions/README.md#approve) - Approve
* [comment](docs/sdks/taskactions/README.md#comment) - Comment
* [deny](docs/sdks/taskactions/README.md#deny) - Deny
* [escalate_to_emergency_access](docs/sdks/taskactions/README.md#escalate_to_emergency_access) - Escalate To Emergency Access

### [task_search](docs/sdks/tasksearch/README.md)

* [search](docs/sdks/tasksearch/README.md#search) - Search

### [user](docs/sdks/user/README.md)

* [get](docs/sdks/user/README.md#get) - Get
* [list](docs/sdks/user/README.md#list) - List

### [user_search](docs/sdks/usersearch/README.md)

* [search](docs/sdks/usersearch/README.md#search) - Search
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)