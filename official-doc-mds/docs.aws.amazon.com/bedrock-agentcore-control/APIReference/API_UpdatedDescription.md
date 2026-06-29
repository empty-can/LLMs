

# UpdatedDescription
<a name="API_UpdatedDescription"></a>

Wrapper for updating an optional Description field with PATCH semantics. When present in an update request, the description is replaced with optionalValue. When absent, the description is left unchanged. To unset the description, include the wrapper with optionalValue not specified.

## Contents
<a name="API_UpdatedDescription_Contents"></a>

 ** optionalValue **   <a name="bedrockagentcorecontrol-Type-UpdatedDescription-optionalValue"></a>
Represents an optional value that is used to update the human-readable description of the resource. If not specified, it will clear the current description of the resource.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 4096.  
Required: No

## See Also
<a name="API_UpdatedDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/UpdatedDescription) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/UpdatedDescription) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/UpdatedDescription) 