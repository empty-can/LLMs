

# ModelEnforcement
<a name="API_ModelEnforcement"></a>

Model-specific information for the enforced guardrail configuration.

## Contents
<a name="API_ModelEnforcement_Contents"></a>

 ** excludedModels **   <a name="bedrock-Type-ModelEnforcement-excludedModels"></a>
Models to exclude from enforcement of the guardrail.  
Type: Array of strings  
Array Members: Minimum number of 0 items.  
Pattern: `([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}){0,1}`   
Required: Yes

 ** includedModels **   <a name="bedrock-Type-ModelEnforcement-includedModels"></a>
Models to enforce the guardrail on.  
Type: Array of strings  
Array Members: Minimum number of 1 item.  
Pattern: `(ALL|([a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63})([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}){0,1})`   
Required: Yes

## See Also
<a name="API_ModelEnforcement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelEnforcement) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelEnforcement) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelEnforcement) 