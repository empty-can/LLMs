

# InputConfiguration
<a name="API_data-automation_InputConfiguration"></a>

Input configuration for ingestion jobs.

Only one member of this object can be specified or returned. If both inlinePayload and s3Object are specified, the request will fail with an exception.

## Contents
<a name="API_data-automation_InputConfiguration_Contents"></a>

 ** inlinePayload **   <a name="bedrock-Type-data-automation_InputConfiguration-inlinePayload"></a>
Inline payload input.  
Type: [InlinePayload](API_data-automation_InlinePayload.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** s3Object **   <a name="bedrock-Type-data-automation_InputConfiguration-s3Object"></a>
S3 object input.  
Type: [S3Object](API_data-automation_S3Object.md) object  
Required: No

## See Also
<a name="API_data-automation_InputConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/InputConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/InputConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/InputConfiguration) 