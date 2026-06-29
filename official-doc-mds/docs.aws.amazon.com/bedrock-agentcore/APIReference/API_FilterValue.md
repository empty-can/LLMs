

# FilterValue
<a name="API_FilterValue"></a>

A value used in filter comparisons, supporting different data types.

## Contents
<a name="API_FilterValue_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** booleanValue **   <a name="BedrockAgentCore-Type-FilterValue-booleanValue"></a>
A boolean value for true/false filtering conditions.  
Type: Boolean  
Required: No

 ** doubleValue **   <a name="BedrockAgentCore-Type-FilterValue-doubleValue"></a>
A numeric value for numerical filtering and comparisons.  
Type: Double  
Required: No

 ** stringValue **   <a name="BedrockAgentCore-Type-FilterValue-stringValue"></a>
A string value for text-based filtering.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Required: No

## See Also
<a name="API_FilterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-2024-02-28/FilterValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-2024-02-28/FilterValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-2024-02-28/FilterValue) 