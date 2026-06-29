

# ApiSchemaConfiguration
<a name="API_ApiSchemaConfiguration"></a>

Configuration for API schema.

## Contents
<a name="API_ApiSchemaConfiguration_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** inlinePayload **   <a name="bedrockagentcorecontrol-Type-ApiSchemaConfiguration-inlinePayload"></a>
The inline payload containing the API schema definition.  
Type: String  
Required: No

 ** s3 **   <a name="bedrockagentcorecontrol-Type-ApiSchemaConfiguration-s3"></a>
The Amazon S3 configuration for a gateway. This structure defines how the gateway accesses files in Amazon S3.  
Type: [S3Configuration](API_S3Configuration.md) object  
Required: No

## See Also
<a name="API_ApiSchemaConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ApiSchemaConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ApiSchemaConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ApiSchemaConfiguration) 