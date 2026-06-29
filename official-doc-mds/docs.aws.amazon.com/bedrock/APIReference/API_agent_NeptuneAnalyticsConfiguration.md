

# NeptuneAnalyticsConfiguration
<a name="API_agent_NeptuneAnalyticsConfiguration"></a>

Contains details about the storage configuration of the knowledge base in Amazon Neptune Analytics. For more information, see [Create a vector index in Amazon Neptune Analytics](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-neptune.html).

## Contents
<a name="API_agent_NeptuneAnalyticsConfiguration_Contents"></a>

 ** fieldMapping **   <a name="bedrock-Type-agent_NeptuneAnalyticsConfiguration-fieldMapping"></a>
Contains the names of the fields to which to map information about the vector store.  
Type: [NeptuneAnalyticsFieldMapping](API_agent_NeptuneAnalyticsFieldMapping.md) object  
Required: Yes

 ** graphArn **   <a name="bedrock-Type-agent_NeptuneAnalyticsConfiguration-graphArn"></a>
The Amazon Resource Name (ARN) of the Neptune Analytics vector store.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `arn:aws(|-cn|-us-gov):neptune-graph:[a-zA-Z0-9-]*:[0-9]{12}:graph/g-[a-zA-Z0-9]{10}`   
Required: Yes

## See Also
<a name="API_agent_NeptuneAnalyticsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/NeptuneAnalyticsConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/NeptuneAnalyticsConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/NeptuneAnalyticsConfiguration) 