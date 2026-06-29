

# DataAutomationConfiguration
<a name="API_data-automation-runtime_DataAutomationConfiguration"></a>

Details about a data automation project.

## Contents
<a name="API_data-automation-runtime_DataAutomationConfiguration_Contents"></a>

 ** dataAutomationProjectArn **   <a name="bedrock-Type-data-automation-runtime_DataAutomationConfiguration-dataAutomationProjectArn"></a>
The ARN of the project you're using in your configuration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-_]+`   
Required: Yes

 ** stage **   <a name="bedrock-Type-data-automation-runtime_DataAutomationConfiguration-stage"></a>
The project's stage.  
Type: String  
Valid Values: `LIVE | DEVELOPMENT`   
Required: No

## See Also
<a name="API_data-automation-runtime_DataAutomationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/DataAutomationConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/DataAutomationConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/DataAutomationConfiguration) 