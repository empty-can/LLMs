

# ImplicitFilterConfiguration
<a name="API_ImplicitFilterConfiguration"></a>

Configuration for implicit filtering in Knowledge Base vector searches. Implicit filtering allows you to automatically filter search results based on metadata attributes without requiring explicit filter expressions in each query.

## Contents
<a name="API_ImplicitFilterConfiguration_Contents"></a>

 ** metadataAttributes **   <a name="bedrock-Type-ImplicitFilterConfiguration-metadataAttributes"></a>
A list of metadata attribute schemas that define the structure and properties of metadata fields used for implicit filtering. Each attribute defines a key, type, and optional description.  
Type: Array of [MetadataAttributeSchema](API_MetadataAttributeSchema.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 25 items.  
Required: Yes

 ** modelArn **   <a name="bedrock-Type-ImplicitFilterConfiguration-modelArn"></a>
The Amazon Resource Name (ARN) of the foundation model used for implicit filtering. This model processes the query to extract relevant filtering criteria.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `(arn:aws(-[^:]+)?:(bedrock|sagemaker):[a-z0-9-]{1,20}:([0-9]{12})?:([a-z-]+/)?)?([a-zA-Z0-9.-]{1,63}){0,2}(([:][a-z0-9-]{1,63}){0,2})?(/[a-z0-9]{1,12})?`   
Required: Yes

## See Also
<a name="API_ImplicitFilterConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ImplicitFilterConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ImplicitFilterConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ImplicitFilterConfiguration) 