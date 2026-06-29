

# AuthorizingClaimMatchValueType
<a name="API_AuthorizingClaimMatchValueType"></a>

Defines the value or values to match for and the relationship of the match.

## Contents
<a name="API_AuthorizingClaimMatchValueType_Contents"></a>

 ** claimMatchOperator **   <a name="bedrockagentcorecontrol-Type-AuthorizingClaimMatchValueType-claimMatchOperator"></a>
Defines the relationship between the claim field value and the value or values you're matching for.  
Type: String  
Valid Values: `EQUALS | CONTAINS | CONTAINS_ANY`   
Required: Yes

 ** claimMatchValue **   <a name="bedrockagentcorecontrol-Type-AuthorizingClaimMatchValueType-claimMatchValue"></a>
The value or values to match for.  
Type: [ClaimMatchValueType](API_ClaimMatchValueType.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

## See Also
<a name="API_AuthorizingClaimMatchValueType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/AuthorizingClaimMatchValueType) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/AuthorizingClaimMatchValueType) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/AuthorizingClaimMatchValueType) 