

# Condition
<a name="API_Condition"></a>

A condition that determines when a gateway rule applies. Conditions can match on principals or request paths.

## Contents
<a name="API_Condition_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** matchPaths **   <a name="bedrockagentcorecontrol-Type-Condition-matchPaths"></a>
A condition that matches on the request path.  
Type: [MatchPaths](API_MatchPaths.md) object  
Required: No

 ** matchPrincipals **   <a name="bedrockagentcorecontrol-Type-Condition-matchPrincipals"></a>
A condition that matches on the identity of the caller making the request.  
Type: [MatchPrincipals](API_MatchPrincipals.md) object  
Required: No

## See Also
<a name="API_Condition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Condition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Condition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Condition) 