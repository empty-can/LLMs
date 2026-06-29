

# FoundationModelDetails
<a name="API_FoundationModelDetails"></a>

Information about a foundation model.

## Contents
<a name="API_FoundationModelDetails_Contents"></a>

 ** modelArn **   <a name="bedrock-Type-FoundationModelDetails-modelArn"></a>
The model Amazon Resource Name (ARN).  
Type: String  
Pattern: `arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}::foundation-model/[a-z0-9-]{1,63}[.]{1}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}`   
Required: Yes

 ** modelId **   <a name="bedrock-Type-FoundationModelDetails-modelId"></a>
The model identifier.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 140.  
Pattern: `[a-z0-9-]{1,63}[.]{1}[a-z0-9-]{1,63}([a-z0-9-]{1,63}[.]){0,2}[a-z0-9-]{1,63}([:][a-z0-9-]{1,63}){0,2}(/[a-z0-9]{12}|)`   
Required: Yes

 ** customizationsSupported **   <a name="bedrock-Type-FoundationModelDetails-customizationsSupported"></a>
The customization that the model supports.  
Type: Array of strings  
Valid Values: `FINE_TUNING | CONTINUED_PRE_TRAINING | DISTILLATION`   
Required: No

 ** inferenceTypesSupported **   <a name="bedrock-Type-FoundationModelDetails-inferenceTypesSupported"></a>
The inference types that the model supports.  
Type: Array of strings  
Valid Values: `ON_DEMAND | PROVISIONED`   
Required: No

 ** inputModalities **   <a name="bedrock-Type-FoundationModelDetails-inputModalities"></a>
The input modalities that the model supports.  
Type: Array of strings  
Valid Values: `TEXT | IMAGE | EMBEDDING`   
Required: No

 ** modelLifecycle **   <a name="bedrock-Type-FoundationModelDetails-modelLifecycle"></a>
Contains details about whether a model version is available or deprecated  
Type: [FoundationModelLifecycle](API_FoundationModelLifecycle.md) object  
Required: No

 ** modelName **   <a name="bedrock-Type-FoundationModelDetails-modelName"></a>
The model name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `.*`   
Required: No

 ** outputModalities **   <a name="bedrock-Type-FoundationModelDetails-outputModalities"></a>
The output modalities that the model supports.  
Type: Array of strings  
Valid Values: `TEXT | IMAGE | EMBEDDING`   
Required: No

 ** providerName **   <a name="bedrock-Type-FoundationModelDetails-providerName"></a>
The model's provider name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 20.  
Pattern: `.*`   
Required: No

 ** responseStreamingSupported **   <a name="bedrock-Type-FoundationModelDetails-responseStreamingSupported"></a>
Indicates whether the model supports streaming.  
Type: Boolean  
Required: No

## See Also
<a name="API_FoundationModelDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/FoundationModelDetails) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/FoundationModelDetails) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/FoundationModelDetails) 