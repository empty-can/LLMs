

# CustomClaimValidationType
<a name="API_CustomClaimValidationType"></a>

Defines the name of a custom claim field and rules for finding matches to authenticate its value.

## Contents
<a name="API_CustomClaimValidationType_Contents"></a>

 ** authorizingClaimMatchValue **   <a name="bedrockagentcorecontrol-Type-CustomClaimValidationType-authorizingClaimMatchValue"></a>
Defines the value or values to match for and the relationship of the match.  
Type: [AuthorizingClaimMatchValueType](API_AuthorizingClaimMatchValueType.md) object  
Required: Yes

 ** inboundTokenClaimName **   <a name="bedrockagentcorecontrol-Type-CustomClaimValidationType-inboundTokenClaimName"></a>
The name of the custom claim field to check.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 255.  
Pattern: `[A-Za-z0-9_.-:]+`   
Required: Yes

 ** inboundTokenClaimValueType **   <a name="bedrockagentcorecontrol-Type-CustomClaimValidationType-inboundTokenClaimValueType"></a>
The data type of the claim value to check for.  
+ Use `STRING` if you want to find an exact match to a string you define.
+ Use `STRING_ARRAY` if you want to fnd a match to at least one value in an array you define.
Type: String  
Valid Values: `STRING | STRING_ARRAY`   
Required: Yes

## See Also
<a name="API_CustomClaimValidationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CustomClaimValidationType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CustomClaimValidationType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CustomClaimValidationType) 