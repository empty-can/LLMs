

# ModelConfiguration
<a name="API_ModelConfiguration"></a>

Configuration for a model used in advanced prompt optimization.

## Contents
<a name="API_ModelConfiguration_Contents"></a>

 ** modelId **   <a name="bedrock-Type-ModelConfiguration-modelId"></a>
The model ID.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 140.  
Pattern: `[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`   
Required: Yes

 ** additionalModelRequestFields **   <a name="bedrock-Type-ModelConfiguration-additionalModelRequestFields"></a>
Additional model-specific request fields.  
Type: String to JSON value map  
Key Length Constraints: Minimum length of 1. Maximum length of 100.  
Required: No

 ** inferenceConfig **   <a name="bedrock-Type-ModelConfiguration-inferenceConfig"></a>
The inference configuration for the model.  
Type: [InferenceConfiguration](API_InferenceConfiguration.md) object  
Required: No

## See Also
<a name="API_ModelConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ModelConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ModelConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ModelConfiguration) 