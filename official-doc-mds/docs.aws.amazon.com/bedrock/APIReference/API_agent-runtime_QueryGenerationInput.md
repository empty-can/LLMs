

# QueryGenerationInput
<a name="API_agent-runtime_QueryGenerationInput"></a>

Contains information about a natural language query to transform into SQL.

## Contents
<a name="API_agent-runtime_QueryGenerationInput_Contents"></a>

 ** text **   <a name="bedrock-Type-agent-runtime_QueryGenerationInput-text"></a>
The text of the query.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20000.  
Pattern: `(?!\s*$).+.*`   
Required: Yes

 ** type **   <a name="bedrock-Type-agent-runtime_QueryGenerationInput-type"></a>
The type of the query.  
Type: String  
Valid Values: `TEXT`   
Required: Yes

## See Also
<a name="API_agent-runtime_QueryGenerationInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/QueryGenerationInput) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/QueryGenerationInput) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/QueryGenerationInput) 