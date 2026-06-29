

# RFTConfig
<a name="API_RFTConfig"></a>

 Configuration settings for reinforcement fine-tuning (RFT), including grader configuration and training hyperparameters. 

## Contents
<a name="API_RFTConfig_Contents"></a>

 ** graderConfig **   <a name="bedrock-Type-RFTConfig-graderConfig"></a>
 Configuration for the grader that evaluates model responses and provides reward signals during RFT training.   
Type: [GraderConfig](API_GraderConfig.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: No

 ** hyperParameters **   <a name="bedrock-Type-RFTConfig-hyperParameters"></a>
 Hyperparameters that control the reinforcement fine-tuning training process, including learning rate, batch size, and epoch count.   
Type: [RFTHyperParameters](API_RFTHyperParameters.md) object  
Required: No

## See Also
<a name="API_RFTConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RFTConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RFTConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RFTConfig) 