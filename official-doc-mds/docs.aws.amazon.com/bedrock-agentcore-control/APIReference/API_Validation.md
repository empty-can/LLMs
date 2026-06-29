

# Validation
<a name="API_Validation"></a>

Validation rules for extracted metadata values. Only one type can be specified, matching the field's data type.

## Contents
<a name="API_Validation_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** numberValidation **   <a name="bedrockagentcorecontrol-Type-Validation-numberValidation"></a>
Validation for NUMBER fields.  
Type: [NumberValidation](API_NumberValidation.md) object  
Required: No

 ** stringListValidation **   <a name="bedrockagentcorecontrol-Type-Validation-stringListValidation"></a>
Validation for STRINGLIST fields.  
Type: [StringListValidation](API_StringListValidation.md) object  
Required: No

 ** stringValidation **   <a name="bedrockagentcorecontrol-Type-Validation-stringValidation"></a>
Validation for STRING fields.  
Type: [StringValidation](API_StringValidation.md) object  
Required: No

## See Also
<a name="API_Validation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/Validation) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/Validation) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/Validation) 