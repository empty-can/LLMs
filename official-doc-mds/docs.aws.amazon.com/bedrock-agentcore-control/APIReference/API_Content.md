

# Content
<a name="API_Content"></a>

Represents content input for policy generation operations. This structure encapsulates the natural language descriptions or other content formats that are used as input for AI-powered policy generation.

## Contents
<a name="API_Content_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** rawText **   <a name="bedrockagentcorecontrol-Type-Content-rawText"></a>
The raw text content containing natural language descriptions of desired policy behavior. This text is processed by AI to generate corresponding Cedar policy statements that match the described intent.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2000.  
Required: No

## See Also
<a name="API_Content_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Content) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Content) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Content) 