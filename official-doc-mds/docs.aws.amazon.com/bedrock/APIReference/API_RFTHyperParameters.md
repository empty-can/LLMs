

# RFTHyperParameters
<a name="API_RFTHyperParameters"></a>

 Hyperparameters for controlling the reinforcement fine-tuning training process, including learning settings and evaluation intervals. 

## Contents
<a name="API_RFTHyperParameters_Contents"></a>

 ** batchSize **   <a name="bedrock-Type-RFTHyperParameters-batchSize"></a>
 Number of training samples processed in each batch during reinforcement fine-tuning (RFT) training. Larger batches may improve training stability.   
Type: Integer  
Valid Range: Minimum value of 16. Maximum value of 512.  
Required: No

 ** epochCount **   <a name="bedrock-Type-RFTHyperParameters-epochCount"></a>
 Number of training epochs to run during reinforcement fine-tuning. Higher values may improve performance but increase training time.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 50.  
Required: No

 ** evalInterval **   <a name="bedrock-Type-RFTHyperParameters-evalInterval"></a>
 Interval between evaluation runs during RFT training, measured in training steps. More frequent evaluation provides better monitoring.   
Type: Integer  
Valid Range: Minimum value of 1. Maximum value of 100.  
Required: No

 ** inferenceMaxTokens **   <a name="bedrock-Type-RFTHyperParameters-inferenceMaxTokens"></a>
 Maximum number of tokens the model can generate in response to each prompt during RFT training.   
Type: Integer  
Required: No

 ** learningRate **   <a name="bedrock-Type-RFTHyperParameters-learningRate"></a>
 Learning rate for the reinforcement fine-tuning. Controls how quickly the model adapts to reward signals.   
Type: Float  
Valid Range: Minimum value of 1.0e-07. Maximum value of 0.001.  
Required: No

 ** maxPromptLength **   <a name="bedrock-Type-RFTHyperParameters-maxPromptLength"></a>
 Maximum length of input prompts during RFT training, measured in tokens. Longer prompts allow more context but increase memory usage and training-time.   
Type: Integer  
Required: No

 ** reasoningEffort **   <a name="bedrock-Type-RFTHyperParameters-reasoningEffort"></a>
 Level of reasoning effort applied during RFT training. Higher values may improve response quality but increase training time.   
Type: String  
Valid Values: `low | medium | high`   
Required: No

 ** trainingSamplePerPrompt **   <a name="bedrock-Type-RFTHyperParameters-trainingSamplePerPrompt"></a>
 Number of response samples generated per prompt during RFT training. More samples provide better reward signal estimation.   
Type: Integer  
Valid Range: Minimum value of 2. Maximum value of 16.  
Required: No

## See Also
<a name="API_RFTHyperParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/RFTHyperParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/RFTHyperParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/RFTHyperParameters) 