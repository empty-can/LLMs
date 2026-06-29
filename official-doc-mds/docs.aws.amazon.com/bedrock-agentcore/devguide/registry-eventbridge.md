

# Notifications (Amazon EventBridge)
<a name="registry-eventbridge"></a>

## Supported events
<a name="registry-eventbridge-supported-events"></a>

Events are sent to the default Amazon EventBridge bus. Source: `aws.bedrock-agentcore`.


| Event | Detail type | Trigger | 
| --- | --- | --- | 
| Record submitted for approval |  `Registry Record State changed to Pending Approval`  | SubmitRegistryRecordForApproval called | 
| Registry moves from Creating to Ready State |  `Registry State transitions from Creating to Ready`  | After Create Registry, once a Registry completes provisioning | 

See [Notifications for pending approvals](registry-notifications-approvals.md) for full event schema and setup instructions.