

# APISchema
<a name="API_agent-runtime_APISchema"></a>

 Contains details about the OpenAPI schema for the action group. For more information, see [Action group OpenAPI schemas](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html). You can either include the schema directly in the payload field or you can upload it to an S3 bucket and specify the S3 bucket location in the s3 field. 

## Contents
<a name="API_agent-runtime_APISchema_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** payload **   <a name="bedrock-Type-agent-runtime_APISchema-payload"></a>
 The JSON or YAML-formatted payload defining the OpenAPI schema for the action group.   
Type: String  
Required: No

 ** s3 **   <a name="bedrock-Type-agent-runtime_APISchema-s3"></a>
 Contains details about the S3 object containing the OpenAPI schema for the action group.   
Type: [S3Identifier](API_agent-runtime_S3Identifier.md) object  
Required: No

## See Also
<a name="API_agent-runtime_APISchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/APISchema) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/APISchema) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/APISchema) 