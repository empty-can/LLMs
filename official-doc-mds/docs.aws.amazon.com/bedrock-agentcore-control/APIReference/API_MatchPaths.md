

# MatchPaths
<a name="API_MatchPaths"></a>

A condition that matches requests based on the request path.

## Contents
<a name="API_MatchPaths_Contents"></a>

 ** anyOf **   <a name="bedrockagentcorecontrol-Type-MatchPaths-anyOf"></a>
A list of path patterns. The condition is met if the request path matches any of the patterns.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 0. Maximum length of 512.  
Pattern: `/[\w\-.]+/\*`   
Required: Yes

## See Also
<a name="API_MatchPaths_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/MatchPaths) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/MatchPaths) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/MatchPaths) 