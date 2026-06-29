

# BlueprintSummary
<a name="API_data-automation_BlueprintSummary"></a>

A summary of a blueprint.

## Contents
<a name="API_data-automation_BlueprintSummary_Contents"></a>

 ** blueprintArn **   <a name="bedrock-Type-data-automation_BlueprintSummary-blueprintArn"></a>
The blueprint's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`   
Required: Yes

 ** creationTime **   <a name="bedrock-Type-data-automation_BlueprintSummary-creationTime"></a>
When the blueprint was created.  
Type: Timestamp  
Required: Yes

 ** blueprintName **   <a name="bedrock-Type-data-automation_BlueprintSummary-blueprintName"></a>
The blueprint's name.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: No

 ** blueprintStage **   <a name="bedrock-Type-data-automation_BlueprintSummary-blueprintStage"></a>
The blueprint's stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

 ** blueprintVersion **   <a name="bedrock-Type-data-automation_BlueprintSummary-blueprintVersion"></a>
The blueprint's version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[0-9]*`   
Required: No

 ** lastModifiedTime **   <a name="bedrock-Type-data-automation_BlueprintSummary-lastModifiedTime"></a>
When the blueprint was last updated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_data-automation_BlueprintSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/BlueprintSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/BlueprintSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/BlueprintSummary) 