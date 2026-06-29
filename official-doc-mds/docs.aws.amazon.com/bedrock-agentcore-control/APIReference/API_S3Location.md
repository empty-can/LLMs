

# S3Location
<a name="API_S3Location"></a>

The Amazon S3 location for storing data. This structure defines where in Amazon S3 data is stored.

## Contents
<a name="API_S3Location_Contents"></a>

 ** bucket **   <a name="bedrockagentcorecontrol-Type-S3Location-bucket"></a>
The name of the Amazon S3 bucket. This bucket contains the stored data.  
Type: String  
Pattern: `[a-z0-9][a-z0-9.-]{1,61}[a-z0-9]`   
Required: Yes

 ** prefix **   <a name="bedrockagentcorecontrol-Type-S3Location-prefix"></a>
The prefix for objects in the Amazon S3 bucket. This prefix is added to the object keys to organize the data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: Yes

 ** versionId **   <a name="bedrockagentcorecontrol-Type-S3Location-versionId"></a>
The version ID of the Amazon Amazon S3 object. If not specified, the latest version of the object is used.  
Type: String  
Length Constraints: Minimum length of 3. Maximum length of 1024.  
Required: No

## See Also
<a name="API_S3Location_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/S3Location) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/S3Location) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/S3Location) 