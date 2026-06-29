

# Event
<a name="API_Event"></a>

Contains information about an event in an AgentCore Memory resource.

## Contents
<a name="API_Event_Contents"></a>

 ** actorId **   <a name="BedrockAgentCore-Type-Event-actorId"></a>
The identifier of the actor associated with the event.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_/]*(?::[a-zA-Z0-9-_/]+)*[a-zA-Z0-9-_/]*`   
Required: Yes

 ** eventId **   <a name="BedrockAgentCore-Type-Event-eventId"></a>
The unique identifier of the event.  
Type: String  
Pattern: `[0-9]+#[a-fA-F0-9]+`   
Required: Yes

 ** eventTimestamp **   <a name="BedrockAgentCore-Type-Event-eventTimestamp"></a>
The timestamp when the event occurred.  
Type: Timestamp  
Required: Yes

 ** memoryId **   <a name="BedrockAgentCore-Type-Event-memoryId"></a>
The identifier of the AgentCore Memory resource containing the event.  
Type: String  
Length Constraints: Minimum length of 12.  
Pattern: `(arn:(aws|aws-cn|aws-us-gov):bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory/)?[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** payload **   <a name="BedrockAgentCore-Type-Event-payload"></a>
The content payload of the event.  
Type: Array of [PayloadType](API_PayloadType.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 100 items.  
Required: Yes

 ** sessionId **   <a name="BedrockAgentCore-Type-Event-sessionId"></a>
The identifier of the session containing the event.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-_]*`   
Required: Yes

 ** branch **   <a name="BedrockAgentCore-Type-Event-branch"></a>
The branch information for the event.  
Type: [Branch](API_Branch.md) object  
Required: No

 ** metadata **   <a name="BedrockAgentCore-Type-Event-metadata"></a>
Metadata associated with an event.  
Type: String to [MetadataValue](API_MetadataValue.md) object map  
Map Entries: Minimum number of 0 items. Maximum number of 15 items.  
Key Length Constraints: Minimum length of 1. Maximum length of 128.  
Key Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

## See Also
<a name="API_Event_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/Event) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/Event) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/Event) 