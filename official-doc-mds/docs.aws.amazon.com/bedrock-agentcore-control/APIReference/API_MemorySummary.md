

# MemorySummary
<a name="API_MemorySummary"></a>

Contains summary information about a memory resource.

## Contents
<a name="API_MemorySummary_Contents"></a>

 ** createdAt **   <a name="bedrockagentcorecontrol-Type-MemorySummary-createdAt"></a>
The timestamp when the memory was created.  
Type: Timestamp  
Required: Yes

 ** updatedAt **   <a name="bedrockagentcorecontrol-Type-MemorySummary-updatedAt"></a>
The timestamp when the memory was last updated.  
Type: Timestamp  
Required: Yes

 ** arn **   <a name="bedrockagentcorecontrol-Type-MemorySummary-arn"></a>
The Amazon Resource Name (ARN) of the memory.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: No

 ** id **   <a name="bedrockagentcorecontrol-Type-MemorySummary-id"></a>
The unique identifier of the memory.  
Type: String  
Length Constraints: Minimum length of 12.  
Pattern: `[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: No

 ** managedByResourceArn **   <a name="bedrockagentcorecontrol-Type-MemorySummary-managedByResourceArn"></a>
ARN of the resource managing this memory (e.g. a harness). Null if not managed.  
Type: String  
Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`   
Required: No

 ** status **   <a name="bedrockagentcorecontrol-Type-MemorySummary-status"></a>
The current status of the memory.  
Type: String  
Valid Values: `CREATING | ACTIVE | FAILED | DELETING | UPDATING`   
Required: No

## See Also
<a name="API_MemorySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/MemorySummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/MemorySummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/MemorySummary) 