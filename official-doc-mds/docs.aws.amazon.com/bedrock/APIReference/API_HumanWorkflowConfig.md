

# HumanWorkflowConfig
<a name="API_HumanWorkflowConfig"></a>

Contains `SageMakerFlowDefinition` object. The object is used to specify the prompt dataset, task type, rating method and metric names.

## Contents
<a name="API_HumanWorkflowConfig_Contents"></a>

 ** flowDefinitionArn **   <a name="bedrock-Type-HumanWorkflowConfig-flowDefinitionArn"></a>
The Amazon Resource Number (ARN) for the flow definition  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 1024.  
Pattern: `arn:aws(-[^:]+)?:sagemaker:[a-z0-9-]{1,20}:[0-9]{12}:flow-definition/.*`   
Required: Yes

 ** instructions **   <a name="bedrock-Type-HumanWorkflowConfig-instructions"></a>
Instructions for the flow definition  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 5000.  
Pattern: `[\S\s]+`   
Required: No

## See Also
<a name="API_HumanWorkflowConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/HumanWorkflowConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/HumanWorkflowConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/HumanWorkflowConfig) 