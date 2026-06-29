

# Create and manage records
<a name="registry-create-manage-records"></a>

## Create a registry record
<a name="registry-create-record"></a>

### Console
<a name="registry-create-record-console"></a>

1. Open the registry detail page.

1. In the **Registry records** section, choose **Create record**.

1. Choose a source type:

   1.  **Synchronize from endpoint** — Provide an endpoint URL and optional credentials to invoke the endpoint, and the registry fetches metadata from the source. Available for MCP and Agent record types only. To update the record after the source changes, you must manually trigger synchronization. See [Synchronize records from external sources](registry-sync-records.md) for details.

   1.  **Manual** — Manually configure the record details and protocol configuration.

 **Synchronize from endpoint** 

1. Under **Record details**, select the record type: **MCP** or **Agent**.
**Note**  
Synchronization is only supported for MCP and Agent record types. Agent Skills and Custom record types do not support synchronization — use the Manual source type instead.

1. Enter the **Endpoint** URL. Must be a valid HTTPS URL.

1. Under **Credential type**, choose how the registry authorizes with the endpoint:

   1.  **IAM** — Provide a **Role ARN** for SigV4 signing and a **Service** name (e.g., `bedrock-agentcore`, `execute-api`, `lambda`). Optionally specify a **Region** for signing.

   1.  **OAuth** — Select or enter a **Credential provider** ARN from AgentCore Identity. Optionally configure **Scopes** and **Custom parameters** under Additional configuration.

   1.  **None** — No authorization (for public endpoints).

1. Choose **Create record**.

   The record is created in CREATING status. The registry connects to the endpoint, extracts metadata, and populates the record’s descriptors. After synchronization completes, the record transitions to DRAFT. If synchronization fails, the record transitions to CREATE\_FAILED status with the error details available in the Status Reason field on the record detail page. For troubleshooting, see [Record synchronization errors](registry-troubleshooting.md#registry-troubleshooting-sync-errors). To update the record when the source changes, use the **Sync** button on the record detail page or select **Re-sync from endpoint** during editing.

For AWS CLI and SDK examples of creating records with synchronization, see [Synchronize records from external sources](registry-sync-records.md).

 **Manual** 

1. Under **Record details** , enter:

   1.  **Name** — Must start with a letter or digit. Valid characters are a-z, A-Z, 0-9, \_ (underscore), - (hyphen), . (dot), and / (forward slash). The name can have up to 255 characters.

   1.  **Description** (optional) — 1 to 4,096 characters.

   1.  **Record version** — Specify the version of this record (e.g., 1.0.0, v2.1).

1. Under **Record type** , select one of: **MCP** , **Agent** , **Agent Skills** , or **Custom**.

1. A type-specific editor appears. Enter your protocol configuration in JSON format.

   1. For **Agent** and **MCP** types, toggle **Show official schema** to display the reference schema side-by-side for guidance.

   1. The console validates your JSON against the official schema and shows inline errors (e.g., "Missing property 'name'") with a **Diagnose with Amazon Q** button.

1. Choose one of:

   1.  **Create as draft** — Creates the record in Draft status.

   1.  **Create and submit for approval** — Creates the record and immediately submits it for approval.

### AWS CLI
<a name="registry-create-record-cli"></a>

```
aws bedrock-agentcore-control create-registry-record \
  --registry-id <registryId> \
  --name "MyMCPServer" \
  --descriptor-type MCP \
  --descriptors '{"mcp": {"server": {"inlineContent": "{\"name\": \"my/mcp-server\", \"description\": \"My MCP server\", \"version\": \"1.0.0\"}"}}}' \
  --record-version "1.0" \
  --region us-east-1
```

### AWS SDK
<a name="registry-create-record-sdk"></a>

```
import boto3
import json

client = boto3.client('bedrock-agentcore-control')

server_content = json.dumps({
    "name": "my/mcp-server",
    "description": "My MCP server",
    "version": "1.0.0"
})

response = client.create_registry_record(
    registryId='<registryId>',
    name='MyMCPServer',
    descriptorType='MCP',
    descriptors={
        'mcp': {
            'server': {
                'inlineContent': server_content
            }
        }
    },
    recordVersion='1.0'
)
print(f"Record ARN: {response['recordArn']}")
print(f"Status: {response['status']}")  # CREATING
```

## List registry records
<a name="registry-list-records"></a>

### Console
<a name="registry-list-records-console"></a>

1. Open the registry detail page.

1. The **Registry records** section displays:

   1.  **Status summary counters** — Total submitted, Pending approval, Approved, Deprecated, Rejected.

   1.  **Records table** with columns: Name, Description, Status, Record type, Record ARN, Last updated.

1. Use the **Search records** bar to filter by name.

1. Use the **Update status** dropdown to perform bulk status changes on selected records.

### AWS CLI
<a name="registry-list-records-cli"></a>

```
aws bedrock-agentcore-control list-registry-records \
  --registry-id "<registryId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-list-records-sdk"></a>

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.list_registry_records(
    registryId='<registryId>'
)
for record in response['registryRecords']:
    print(f"{record['name']} - {record['status']} - {record['descriptorType']}")
```

## View record details
<a name="registry-view-record"></a>

### Console
<a name="registry-view-record-console"></a>

1. From the registry detail page, choose a record name from the records table.

1. The record detail page displays:

   1.  **Record details** section — Name, Description, Record ARN, Status (shown as a badge next to the record name), Version, Last updated date, Record type, Record ID, Created date.

   1.  **Synchronization configuration** section (if configured) — Synchronization type, Source URL, and credential provider details (IAM role ARN, service, region or OAuth provider ARN, grant type, scopes, custom parameters).

   1.  **Protocol configuration** section — The descriptor content displayed as formatted JSON (e.g., "Agent card" for A2A records, "Server" and "Tools" for MCP records).

1. Actions available:

   1.  **Sync** button (MCP and Agent records only) — Triggers a fresh synchronization from the configured endpoint. Opens a confirmation dialog before proceeding. The record transitions to UPDATING status during synchronization.

   1.  **Update status** dropdown — Submit for approval, Approve, Reject, or Deprecate.

   1.  **Three-dot menu (⋮)** — Edit or Delete.

### AWS CLI
<a name="registry-view-record-cli"></a>

```
aws bedrock-agentcore-control get-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-view-record-sdk"></a>

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.get_registry_record(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Name: {response['name']}")
print(f"Description: {response['description']}")
print(f"Status: {response['status']}")
print(f"Descriptor Type: {response['descriptorType']}")
print(f"Version: {response['recordVersion']}")
```

## Update a registry record
<a name="registry-update-record"></a>

### Console
<a name="registry-update-record-console"></a>

1. From the record detail page, choose the three-dot menu (⋮), then choose **Edit**.

1. On the **Edit record** page, update any of the following:

   1.  **Name** , **Description** , **Record version** under Record details.

   1.  **Record type** — Change the protocol type if needed.

1. (MCP and Agent records only) Under **Synchronize from endpoint**, optionally configure synchronization:

   You can update records via synchronization regardless of whether they were originally created with synchronization. When synchronization is triggered during an update, the record transitions to UPDATING status. If it succeeds, a new record version is created in DRAFT status. If it fails, the record transitions to UPDATE\_FAILED status with error details in the Status Reason field. The synchronized data overwrites the record’s name, description, version, tool definitions, and server definitions with the values found at the source, but does not modify fields that the source does not provide. An admin or curator must review and approve the new draft for it to become visible in search. Until then, the previous approved revision (if any) remains searchable. For more information on dual-revision behavior, see [Record lifecycle](registry-record-lifecycle.md).

   1. Enter an **Endpoint** URL to enable synchronization. Credential type fields appear when an endpoint is provided. If the record already has synchronization configured, the endpoint and credential provider fields are pre-populated with the existing configuration.

   1. Choose a **Credential type** (IAM, OAuth, or None) and fill in the required fields. If the record was previously configured with a credential provider, the existing values are pre-filled.

   1. Select **Re-sync from endpoint** to trigger a fresh synchronization when saving. The record transitions to UPDATING status during synchronization.

   1. To remove synchronization, choose the clear button next to the endpoint field. This resets the endpoint and all credential fields.

1. Under **Record configuration**, update the record’s definitions in the JSON editor.

   1. You can configure both the endpoint for synchronization and manually edit the record’s definitions. When synchronization is triggered, the registry fetches the latest metadata from the endpoint and updates the record’s name, description, version, tool definitions, and server definitions with the values found at the source, taking precedence over any manual edits to those fields. Fields that the source does not provide are not modified.

1. The console validates your JSON against the official schema and shows inline errors with a **Diagnose with Amazon Q** button.

1. Choose one of:

   1.  **Save changes** — Saves the record as a draft.

   1.  **Save and submit for approval** — Saves and submits in one step.

A success banner confirms: "[Name] is updated and submitted for approval successfully."

### AWS CLI
<a name="registry-update-record-cli"></a>

```
aws bedrock-agentcore-control update-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --description "Updated description" \
  --region us-east-1
```

### AWS SDK
<a name="registry-update-record-sdk"></a>

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.update_registry_record(
    registryId='<registryId>',
    recordId='<recordId>',
    description='Updated description'
)
print(f"Updated: {response['name']} - Status: {response['status']}")
```

## Submit a record for approval
<a name="registry-submit-record"></a>

### Console
<a name="registry-submit-record-console"></a>

From the record detail page -

1. Choose the **Update status** dropdown

1. Then, choose **Submit for approval**.

   1. Alternatively, use **Create and submit for approval** or **Save and submit for approval** during creation or editing.

**Note**  
If the Registry’s Auto-Approval configuration is set to TRUE, then submitting a record for approval automatically approves it. Otherwise, if the Auto-Approval configuration is set to FALSE, then the record moves to 'Pending Approval' status and waits for the Curator to either Approve it or Reject it. Additionally, an Amazon EventBridge notification is triggered indicating a new record has been requested for approval.

### AWS CLI
<a name="registry-submit-record-cli"></a>

```
aws bedrock-agentcore-control submit-registry-record-for-approval \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-submit-record-sdk"></a>

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.submit_registry_record_for_approval(
    registryId='<registryId>',
    recordId='<recordId>'
)
print(f"Status: {response['status']}")  # PENDING_APPROVAL or APPROVED
```

## Delete a registry record
<a name="registry-delete-record"></a>

### Console
<a name="registry-delete-record-console"></a>

1. From the record detail page, choose the three-dot menu (⋮), then choose **Delete**.

1. Confirm the deletion by typing in 'delete' when prompted

Deletion is permanent and cannot be undone.

### AWS CLI
<a name="registry-delete-record-cli"></a>

```
aws bedrock-agentcore-control delete-registry-record \
  --registry-id "<registryId>" \
  --record-id "<recordId>" \
  --region us-east-1
```

### AWS SDK
<a name="registry-delete-record-sdk"></a>

```
import boto3

client = boto3.client('bedrock-agentcore-control')

response = client.delete_registry_record(
    registryId='<registryId>',
    recordId='<recordId>'
)
print("Record deleted successfully")
```

## Schema validation
<a name="registry-schema-validation"></a>

When you create or edit a record, the console and API validate your protocol configuration against the official schema for the selected record type. More details on validations can be found in [Supported record types](registry-supported-record-types.md).