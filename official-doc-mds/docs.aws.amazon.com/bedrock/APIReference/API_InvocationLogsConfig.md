

# InvocationLogsConfig
<a name="API_InvocationLogsConfig"></a>

Settings for using invocation logs to customize a model.

## Contents
<a name="API_InvocationLogsConfig_Contents"></a>

 ** invocationLogSource **   <a name="bedrock-Type-InvocationLogsConfig-invocationLogSource"></a>
The source of the invocation logs.  
Type: [InvocationLogSource](API_InvocationLogSource.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** requestMetadataFilters **   <a name="bedrock-Type-InvocationLogsConfig-requestMetadataFilters"></a>
Rules for filtering invocation logs based on request metadata.  
Type: [RequestMetadataFilters](API_RequestMetadataFilters.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** usePromptResponse **   <a name="bedrock-Type-InvocationLogsConfig-usePromptResponse"></a>
Whether to use the model's response for training, or just the prompt. The default value is `False`.  
Type: Boolean  
Required: No

## See Also
<a name="API_InvocationLogsConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/InvocationLogsConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/InvocationLogsConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/InvocationLogsConfig) 