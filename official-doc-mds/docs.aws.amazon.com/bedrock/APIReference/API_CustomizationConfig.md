

# CustomizationConfig
<a name="API_CustomizationConfig"></a>

A model customization configuration

## Contents
<a name="API_CustomizationConfig_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** distillationConfig **   <a name="bedrock-Type-CustomizationConfig-distillationConfig"></a>
The Distillation configuration for the custom model.  
Type: [DistillationConfig](API_DistillationConfig.md) object  
Required: No

 ** rftConfig **   <a name="bedrock-Type-CustomizationConfig-rftConfig"></a>
 Configuration settings for reinforcement fine-tuning (RFT) model customization, including grader configuration and hyperparameters.   
Type: [RFTConfig](API_RFTConfig.md) object  
Required: No

## See Also
<a name="API_CustomizationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CustomizationConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CustomizationConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CustomizationConfig) 