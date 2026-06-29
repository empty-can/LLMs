

# Memory
<a name="API_Memory"></a>

Contains information about a memory resource.

## Contents
<a name="API_Memory_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-Memory-arn"></a>
The Amazon Resource Name (ARN) of the memory.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-Memory-createdAt"></a>
The timestamp when the memory was created.  
Type: Timestamp  
Required: Yes

 ** eventExpiryDuration **   <a name="bedrockagentcorecontrol-Type-Memory-eventExpiryDuration"></a>
The number of days after which memory events will expire.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 365.  
Required: Yes

 ** id **   <a name="bedrockagentcorecontrol-Type-Memory-id"></a>
The unique identifier of the memory.  
Type: String  
Length Constraints: Minimum length of 12.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: Yes

 ** name **   <a name="bedrockagentcorecontrol-Type-Memory-name"></a>
The name of the memory.  
Type: String  
Pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`   
Required: Yes

 ** status **   <a name="bedrockagentcorecontrol-Type-Memory-status"></a>
The current status of the memory.  
Type: String  
Valid Values: `CREATING | ACTIVE | FAILED | DELETING | UPDATING`   
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-Memory-updatedAt"></a>
The timestamp when the memory was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-Memory-description"></a>
The description of the memory.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

 ** encryptionKeyArn **   <a name="bedrockagentcorecontrol-Type-Memory-encryptionKeyArn"></a>
The ARN of the KMS key used to encrypt the memory.  
Type: String  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: No

 ** failureReason **   <a name="bedrockagentcorecontrol-Type-Memory-failureReason"></a>
The reason for failure if the memory is in a failed state.  
Type: String  
Required: No

 ** indexedKeys **   <a name="bedrockagentcorecontrol-Type-Memory-indexedKeys"></a>
The indexed metadata keys for this memory. Only indexed keys can be used in metadata filters.  
Type: Array of [IndexedKey](API_IndexedKey.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Required: No

 ** managedByResourceArn **   <a name="bedrockagentcorecontrol-Type-Memory-managedByResourceArn"></a>
ARN of the resource managing this memory (e.g. a harness). When set, strategy modifications and deletion are only allowed through the managing resource.  
Type: String  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: No

 ** memoryExecutionRoleArn **   <a name="bedrockagentcorecontrol-Type-Memory-memoryExecutionRoleArn"></a>
The ARN of the IAM role that provides permissions for the memory.  
Type: String  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: No

 ** strategies **   <a name="bedrockagentcorecontrol-Type-Memory-strategies"></a>
The list of memory strategies associated with this memory.  
Type: Array of [MemoryStrategy](API_MemoryStrategy.md) objects  
Required: No

 ** streamDeliveryResources **   <a name="bedrockagentcorecontrol-Type-Memory-streamDeliveryResources"></a>
Configuration for streaming memory record data to external resources.  
Type: [StreamDeliveryResources](API_StreamDeliveryResources.md) object  
Required: No

## See Also
<a name="API_Memory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Memory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Memory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Memory) 