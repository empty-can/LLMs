

# Blueprint
<a name="API_data-automation_Blueprint"></a>

A data processing blueprint.

## Contents
<a name="API_data-automation_Blueprint_Contents"></a>

 ** blueprintArn **   <a name="bedrock-Type-data-automation_Blueprint-blueprintArn"></a>
The blueprint's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`   
Required: Yes

 ** blueprintName **   <a name="bedrock-Type-data-automation_Blueprint-blueprintName"></a>
The blueprint's name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: Yes

 ** creationTime **   <a name="bedrock-Type-data-automation_Blueprint-creationTime"></a>
When the blueprint was created.  
Type: Timestamp  
Required: Yes

 ** lastModifiedTime **   <a name="bedrock-Type-data-automation_Blueprint-lastModifiedTime"></a>
When the blueprint was last updated.  
Type: Timestamp  
Required: Yes

 ** schema **   <a name="bedrock-Type-data-automation_Blueprint-schema"></a>
The blueprint's schema.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100000.  
Required: Yes

 ** type **   <a name="bedrock-Type-data-automation_Blueprint-type"></a>
The blueprint's type.  
Type: String  
Valid Values: `DOCUMENT | IMAGE | AUDIO`   
Required: Yes

 ** blueprintStage **   <a name="bedrock-Type-data-automation_Blueprint-blueprintStage"></a>
The blueprint's stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

 ** blueprintVersion **   <a name="bedrock-Type-data-automation_Blueprint-blueprintVersion"></a>
The blueprint's version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[0-9]*`   
Required: No

 ** kmsEncryptionContext **   <a name="bedrock-Type-data-automation_Blueprint-kmsEncryptionContext"></a>
The AWS KMS encryption context to use for encryption.  
Type: String to string map  
Map Entries: Maximum number of items.  
Key Length Constraints: Minimum length of 1. Maximum length of 2000.  
Key Pattern: `.*\S.*`   
Value Length Constraints: Minimum length of 1. Maximum length of 2000.  
Value Pattern: `.*\S.*`   
Required: No

 ** kmsKeyId **   <a name="bedrock-Type-data-automation_Blueprint-kmsKeyId"></a>
The AWS KMS key to use for encryption.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]+`   
Required: No

 ** optimizationSamples **   <a name="bedrock-Type-data-automation_Blueprint-optimizationSamples"></a>
Sample data used to optimize this blueprint.  
Type: Array of [BlueprintOptimizationSample](API_data-automation_BlueprintOptimizationSample.md) objects  
Required: No

 ** optimizationTime **   <a name="bedrock-Type-data-automation_Blueprint-optimizationTime"></a>
When the blueprint was last optimized.  
Type: Timestamp  
Required: No

## See Also
<a name="API_data-automation_Blueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/Blueprint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/Blueprint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/Blueprint) 