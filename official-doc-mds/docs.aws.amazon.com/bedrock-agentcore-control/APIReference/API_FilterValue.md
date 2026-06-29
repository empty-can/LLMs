

# FilterValue
<a name="API_FilterValue"></a>

 The value used in filter comparisons, supporting different data types for flexible filtering criteria. 

## Contents
<a name="API_FilterValue_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** booleanValue **   <a name="bedrockagentcorecontrol-Type-FilterValue-booleanValue"></a>
 The boolean value for true/false filtering conditions.   
Type: Boolean  
Required: No

 ** doubleValue **   <a name="bedrockagentcorecontrol-Type-FilterValue-doubleValue"></a>
 The numeric value for numerical filtering and comparisons.   
Type: Double  
Required: No

 ** stringValue **   <a name="bedrockagentcorecontrol-Type-FilterValue-stringValue"></a>
 The string value for text-based filtering.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1024.  
Required: No

## See Also
<a name="API_FilterValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/FilterValue) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/FilterValue) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/FilterValue) 