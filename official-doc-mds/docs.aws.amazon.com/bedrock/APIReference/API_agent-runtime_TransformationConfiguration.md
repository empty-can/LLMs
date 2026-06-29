

# TransformationConfiguration
<a name="API_agent-runtime_TransformationConfiguration"></a>

Contains configurations for transforming the natural language query into SQL.

## Contents
<a name="API_agent-runtime_TransformationConfiguration_Contents"></a>

 ** mode **   <a name="bedrock-Type-agent-runtime_TransformationConfiguration-mode"></a>
The mode of the transformation.  
Type: String  
Valid Values: `TEXT_TO_SQL`   
Required: Yes

 ** textToSqlConfiguration **   <a name="bedrock-Type-agent-runtime_TransformationConfiguration-textToSqlConfiguration"></a>
Specifies configurations for transforming text to SQL.  
Type: [TextToSqlConfiguration](API_agent-runtime_TextToSqlConfiguration.md) object  
Required: No

## See Also
<a name="API_agent-runtime_TransformationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/TransformationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/TransformationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/TransformationConfiguration) 