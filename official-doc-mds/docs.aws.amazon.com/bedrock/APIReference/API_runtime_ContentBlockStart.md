

# ContentBlockStart
<a name="API_runtime_ContentBlockStart"></a>

Content block start information.

## Contents
<a name="API_runtime_ContentBlockStart_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** image **   <a name="bedrock-Type-runtime_ContentBlockStart-image"></a>
The initial event indicating the start of a streaming image block.  
Type: [ImageBlockStart](API_runtime_ImageBlockStart.md) object  
Required: No

 ** toolResult **   <a name="bedrock-Type-runtime_ContentBlockStart-toolResult"></a>
The   
Type: [ToolResultBlockStart](API_runtime_ToolResultBlockStart.md) object  
Required: No

 ** toolUse **   <a name="bedrock-Type-runtime_ContentBlockStart-toolUse"></a>
Information about a tool that the model is requesting to use.  
Type: [ToolUseBlockStart](API_runtime_ToolUseBlockStart.md) object  
Required: No

## See Also
<a name="API_runtime_ContentBlockStart_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ContentBlockStart) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ContentBlockStart) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ContentBlockStart) 