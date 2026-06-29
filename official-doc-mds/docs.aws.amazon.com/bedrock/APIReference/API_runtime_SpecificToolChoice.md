

# SpecificToolChoice
<a name="API_runtime_SpecificToolChoice"></a>

The model must request a specific tool. For example, `{"tool" : {"name" : "Your tool name"}}`. For more information, see [Call a tool with the Converse API](https://docs.aws.amazon.com/bedrock/latest/userguide/tool-use.html) in the Amazon Bedrock User Guide

**Note**  
This field is only supported by Anthropic Claude 3 models.

## Contents
<a name="API_runtime_SpecificToolChoice_Contents"></a>

 ** name **   <a name="bedrock-Type-runtime_SpecificToolChoice-name"></a>
The name of the tool that the model must request.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

## See Also
<a name="API_runtime_SpecificToolChoice_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/SpecificToolChoice) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/SpecificToolChoice) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/SpecificToolChoice) 