

# DataAutomationProject
<a name="API_data-automation_DataAutomationProject"></a>

A data automation project.

## Contents
<a name="API_data-automation_DataAutomationProject_Contents"></a>

 ** creationTime **   <a name="bedrock-Type-data-automation_DataAutomationProject-creationTime"></a>
When the project was created.  
Type: Timestamp  
Required: Yes

 ** lastModifiedTime **   <a name="bedrock-Type-data-automation_DataAutomationProject-lastModifiedTime"></a>
When the project was last updated.  
Type: Timestamp  
Required: Yes

 ** projectArn **   <a name="bedrock-Type-data-automation_DataAutomationProject-projectArn"></a>
The project's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-]{12,36}`   
Required: Yes

 ** projectName **   <a name="bedrock-Type-data-automation_DataAutomationProject-projectName"></a>
The project's name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: Yes

 ** status **   <a name="bedrock-Type-data-automation_DataAutomationProject-status"></a>
The project's status.  
Type: String  
Valid Values: `COMPLETED | IN_PROGRESS | FAILED`   
Required: Yes

 ** customOutputConfiguration **   <a name="bedrock-Type-data-automation_DataAutomationProject-customOutputConfiguration"></a>
Blueprints that are enabled for the project.  
Type: [CustomOutputConfiguration](API_data-automation_CustomOutputConfiguration.md) object  
Required: No

 ** dataAutomationLibraryConfiguration **   <a name="bedrock-Type-data-automation_DataAutomationProject-dataAutomationLibraryConfiguration"></a>
Library configuration for the project.  
Type: [DataAutomationLibraryConfiguration](API_data-automation_DataAutomationLibraryConfiguration.md) object  
Required: No

 ** kmsEncryptionContext **   <a name="bedrock-Type-data-automation_DataAutomationProject-kmsEncryptionContext"></a>
The AWS KMS encryption context to use for encryption.  
Type: String to string map  
Map Entries: Maximum number of items.  
Key Length Constraints: Minimum length of 1. Maximum length of 2000.  
Key Pattern: `.*\S.*`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Value Pattern: `.*\S.*`   
Required: No

 ** kmsKeyId **   <a name="bedrock-Type-data-automation_DataAutomationProject-kmsKeyId"></a>
The AWS KMS key to use for encryption.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]+`   
Required: No

 ** overrideConfiguration **   <a name="bedrock-Type-data-automation_DataAutomationProject-overrideConfiguration"></a>
Additional settings for the project.  
Type: [OverrideConfiguration](API_data-automation_OverrideConfiguration.md) object  
Required: No

 ** projectDescription **   <a name="bedrock-Type-data-automation_DataAutomationProject-projectDescription"></a>
The project's description.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 300.  
Required: No

 ** projectStage **   <a name="bedrock-Type-data-automation_DataAutomationProject-projectStage"></a>
The project's stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

 ** projectType **   <a name="bedrock-Type-data-automation_DataAutomationProject-projectType"></a>
The type of bedrock data automation API that is compatible with this project.   
Type: String  
Valid Values: `ASYNC | SYNC`   
Required: No

 ** standardOutputConfiguration **   <a name="bedrock-Type-data-automation_DataAutomationProject-standardOutputConfiguration"></a>
The project's standard output configuration.  
Type: [StandardOutputConfiguration](API_data-automation_StandardOutputConfiguration.md) object  
Required: No

## See Also
<a name="API_data-automation_DataAutomationProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/DataAutomationProject) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/DataAutomationProject) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/DataAutomationProject) 