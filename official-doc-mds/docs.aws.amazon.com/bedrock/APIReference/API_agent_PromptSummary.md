

# PromptSummary
<a name="API_agent_PromptSummary"></a>

Contains information about a prompt in your Prompt management tool.

This data type is used in the following API operations:
+  [ListPrompts response](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_ListPrompts.html#API_agent_ListPrompts_ResponseSyntax) 

## Contents
<a name="API_agent_PromptSummary_Contents"></a>

 ** arn **   <a name="bedrock-Type-agent_PromptSummary-arn"></a>
The Amazon Resource Name (ARN) of the prompt or the prompt version (if you specified a version in the request).  
Type: String  
Pattern: `(arn:aws:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:prompt/[0-9a-zA-Z]{10}(?::[0-9]{1,5})?)`   
Required: Yes

 ** createdAt **   <a name="bedrock-Type-agent_PromptSummary-createdAt"></a>
The time at which the prompt was created.  
Type: Timestamp  
Required: Yes

 ** id **   <a name="bedrock-Type-agent_PromptSummary-id"></a>
The unique identifier of the prompt.  
Type: String  
Pattern: `[0-9a-zA-Z]{10}`   
Required: Yes

 ** name **   <a name="bedrock-Type-agent_PromptSummary-name"></a>
The name of the prompt.  
Type: String  
Pattern: `([0-9a-zA-Z][_-]?){1,100}`   
Required: Yes

 ** updatedAt **   <a name="bedrock-Type-agent_PromptSummary-updatedAt"></a>
The time at which the prompt was last updated.  
Type: Timestamp  
Required: Yes

 ** version **   <a name="bedrock-Type-agent_PromptSummary-version"></a>
The version of the prompt that this summary applies to.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5.  
Pattern: `(DRAFT|[0-9]{0,4}[1-9][0-9]{0,4})`   
Required: Yes

 ** description **   <a name="bedrock-Type-agent_PromptSummary-description"></a>
The description of the prompt.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Required: No

## See Also
<a name="API_agent_PromptSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptSummary) 