

# S3Location
<a name="API_S3Location"></a>

The Amazon S3 location configuration of a resource.

## Contents
<a name="API_S3Location_Contents"></a>

 ** bucket **   <a name="BedrockAgentCore-Type-S3Location-bucket"></a>
The name of the Amazon S3 bucket where the resource is stored.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 63.  
Pattern: `[a-z0-9][a-z0-9.-]*[a-z0-9]`   
Required: Yes

 ** prefix **   <a name="BedrockAgentCore-Type-S3Location-prefix"></a>
The name of the Amazon S3 prefix/key where the resource is stored.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** versionId **   <a name="BedrockAgentCore-Type-S3Location-versionId"></a>
The name of the Amazon S3 version ID where the resource is stored (Optional).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/S3Location) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/S3Location) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/S3Location) 