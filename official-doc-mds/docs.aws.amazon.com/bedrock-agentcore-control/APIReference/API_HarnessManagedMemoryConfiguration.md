

# HarnessManagedMemoryConfiguration
<a name="API_HarnessManagedMemoryConfiguration"></a>

Configuration for managed memory creation.

## Contents
<a name="API_HarnessManagedMemoryConfiguration_Contents"></a>

 ** arn **   <a name="bedrockagentcorecontrol-Type-HarnessManagedMemoryConfiguration-arn"></a>
The ARN of the managed AgentCore Memory resource. Read-only on Get, ignored on Create/Update input.  
Type: String  
Pattern: `arn:aws:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:memory\/[a-zA-Z][a-zA-Z0-9-_]{0,99}-[a-zA-Z0-9]{10}`   
Required: No

 ** encryptionKeyArn **   <a name="bedrockagentcorecontrol-Type-HarnessManagedMemoryConfiguration-encryptionKeyArn"></a>
Customer-managed KMS key. Defaults to AWS-owned key. Not updatable after creation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`   
Required: No

 ** eventExpiryDuration **   <a name="bedrockagentcorecontrol-Type-HarnessManagedMemoryConfiguration-eventExpiryDuration"></a>
Event retention in days. Defaults to 30.  
Type: Integer  
Valid Range: Minimum value of 3. Maximum value of 365.  
Required: No

 ** strategies **   <a name="bedrockagentcorecontrol-Type-HarnessManagedMemoryConfiguration-strategies"></a>
Strategy types to enable. Defaults to [SEMANTIC, SUMMARIZATION].  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 4 items.  
Valid Values: `SEMANTIC | SUMMARIZATION | USER_PREFERENCE | EPISODIC`   
Required: No

## See Also
<a name="API_HarnessManagedMemoryConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/HarnessManagedMemoryConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/HarnessManagedMemoryConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/HarnessManagedMemoryConfiguration) 