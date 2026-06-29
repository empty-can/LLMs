

# PromptMetadataEntry
<a name="API_agent_PromptMetadataEntry"></a>

Contains a key-value pair that defines a metadata tag and value to attach to a prompt variant. For more information, see [Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html).

## Contents
<a name="API_agent_PromptMetadataEntry_Contents"></a>

 ** key **   <a name="bedrock-Type-agent_PromptMetadataEntry-key"></a>
The key of a metadata tag for a prompt variant.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: Yes

 ** value **   <a name="bedrock-Type-agent_PromptMetadataEntry-value"></a>
The value of a metadata tag for a prompt variant.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: Yes

## See Also
<a name="API_agent_PromptMetadataEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agent-2023-06-05/PromptMetadataEntry) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agent-2023-06-05/PromptMetadataEntry) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agent-2023-06-05/PromptMetadataEntry) 