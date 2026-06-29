

# DeletionProtectionConfiguration
<a name="API_agent_DeletionProtectionConfiguration"></a>

Configuration for deletion protection.

## Contents
<a name="API_agent_DeletionProtectionConfiguration_Contents"></a>

 ** deletionProtectionStatus **   <a name="bedrock-Type-agent_DeletionProtectionConfiguration-deletionProtectionStatus"></a>
Enable or disable deletion protection for the connector.  
Type: String  
Valid Values: `ENABLED | DISABLED`   
Required: Yes

 ** deletionProtectionThreshold **   <a name="bedrock-Type-agent_DeletionProtectionConfiguration-deletionProtectionThreshold"></a>
The threshold is the maximum percentage of documents that a sync job can delete from your index. If a sync would delete more than this percentage, the sync skips its delete phase, leaving your indexed documents in place. Not supported for the Custom connector.  
Type: Integer  
Valid Range: Minimum value of 0. Maximum value of 100.  
Required: No

## See Also
<a name="API_agent_DeletionProtectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/DeletionProtectionConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/DeletionProtectionConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/DeletionProtectionConfiguration) 