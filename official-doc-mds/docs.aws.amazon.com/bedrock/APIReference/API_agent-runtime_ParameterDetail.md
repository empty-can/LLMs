

# ParameterDetail
<a name="API_agent-runtime_ParameterDetail"></a>

 Contains details about a parameter in a function for an action group. 

## Contents
<a name="API_agent-runtime_ParameterDetail_Contents"></a>

 ** type **   <a name="bedrock-Type-agent-runtime_ParameterDetail-type"></a>
 The data type of the parameter.   
Type: String  
Valid Values: `string | number | integer | boolean | array`   
Required: Yes

 ** description **   <a name="bedrock-Type-agent-runtime_ParameterDetail-description"></a>
 A description of the parameter. Helps the foundation model determine how to elicit the parameters from the user.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 500.  
Required: No

 ** required **   <a name="bedrock-Type-agent-runtime_ParameterDetail-required"></a>
 Whether the parameter is required for the agent to complete the function for action group invocation.   
Type: Boolean  
Required: No

## See Also
<a name="API_agent-runtime_ParameterDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-runtime-2023-07-26/ParameterDetail) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-runtime-2023-07-26/ParameterDetail) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-runtime-2023-07-26/ParameterDetail) 