

# ImplicitFilterConfiguration
<a name="API_agent-runtime_ImplicitFilterConfiguration"></a>

Settings for implicit filtering, where a model generates a metadata filter based on the prompt.

## Contents
<a name="API_agent-runtime_ImplicitFilterConfiguration_Contents"></a>

 ** metadataAttributes **   <a name="bedrock-Type-agent-runtime_ImplicitFilterConfiguration-metadataAttributes"></a>
Metadata that can be used in a filter.  
Type: Array of [MetadataAttributeSchema](API_agent-runtime_MetadataAttributeSchema.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Required: Yes

 ** modelArn **   <a name="bedrock-Type-agent-runtime_ImplicitFilterConfiguration-modelArn"></a>
The model that generates the filter.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

## See Also
<a name="API_agent-runtime_ImplicitFilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ImplicitFilterConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ImplicitFilterConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ImplicitFilterConfiguration) 