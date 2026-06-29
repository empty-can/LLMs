

# Filter
<a name="API_Filter"></a>

 The filter that applies conditions to agent traces during online evaluation to determine which traces should be evaluated. 

## Contents
<a name="API_Filter_Contents"></a>

 ** key **   <a name="bedrockagentcorecontrol-Type-Filter-key"></a>
 The key or field name to filter on within the agent trace data.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9._-]+`   
Required: Yes

 ** operator **   <a name="bedrockagentcorecontrol-Type-Filter-operator"></a>
 The comparison operator to use for filtering.   
Type: String  
Valid Values: `Equals | NotEquals | GreaterThan | LessThan | GreaterThanOrEqual | LessThanOrEqual | Contains | NotContains`   
Required: Yes

 ** value **   <a name="bedrockagentcorecontrol-Type-Filter-value"></a>
 The value to compare against using the specified operator.   
Type: [FilterValue](API_FilterValue.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Filter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Filter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Filter) 