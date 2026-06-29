

# FilterAttribute
<a name="API_agent-runtime_FilterAttribute"></a>

Specifies the name that the metadata attribute must match and the value to which to compare the value of the metadata attribute. For more information, see [Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html).

This data type is used in the following API operations:
+  [RetrieveAndGenerate request](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html#API_agent-runtime_RetrieveAndGenerate_RequestSyntax) 

## Contents
<a name="API_agent-runtime_FilterAttribute_Contents"></a>

 ** key **   <a name="bedrock-Type-agent-runtime_FilterAttribute-key"></a>
The name that the metadata attribute must match.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: Yes

 ** value **   <a name="bedrock-Type-agent-runtime_FilterAttribute-value"></a>
The value to which to compare the value of the metadata attribute.  
Type: JSON value  
Required: Yes

## See Also
<a name="API_agent-runtime_FilterAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/FilterAttribute) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/FilterAttribute) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/FilterAttribute) 