

# ClaimMatchValueType
<a name="API_ClaimMatchValueType"></a>

The value or values to match for.
+ Include a `matchValueString` with the `EQUALS` operator to specify a string that matches the claim field value.
+ Include a `matchValueArray` to specify an array of string values. You can use the following operators:
  + Use `CONTAINS` to yield a match if the claim field value is in the array.
  + Use `CONTAINS_ANY` to yield a match if the claim field value contains any of the strings in the array.

## Contents
<a name="API_ClaimMatchValueType_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** matchValueString **   <a name="bedrockagentcorecontrol-Type-ClaimMatchValueType-matchValueString"></a>
The string value to match for.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-]+`   
Required: No

 ** matchValueStringList **   <a name="bedrockagentcorecontrol-Type-ClaimMatchValueType-matchValueStringList"></a>
An array of strings to check for a match.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-]+`   
Required: No

## See Also
<a name="API_ClaimMatchValueType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/ClaimMatchValueType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/ClaimMatchValueType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/ClaimMatchValueType) 