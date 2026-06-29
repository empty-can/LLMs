

# StringListValidation
<a name="API_StringListValidation"></a>

Validation for STRINGLIST fields.

## Contents
<a name="API_StringListValidation_Contents"></a>

 ** allowedValues **   <a name="bedrockagentcorecontrol-Type-StringListValidation-allowedValues"></a>
Allowed values for items in this STRINGLIST field.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 10 items.  
Length Constraints: Minimum length of 1. Maximum length of 64.  
Pattern: `[a-zA-Z0-9\s._:/=+@-]*`   
Required: No

 ** maxItems **   <a name="bedrockagentcorecontrol-Type-StringListValidation-maxItems"></a>
Maximum number of items in the string list.  
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 5.  
Required: No

## See Also
<a name="API_StringListValidation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/StringListValidation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/StringListValidation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/StringListValidation) 