

# BlueprintFilter
<a name="API_data-automation_BlueprintFilter"></a>

A blueprint filter.

## Contents
<a name="API_data-automation_BlueprintFilter_Contents"></a>

 ** blueprintArn **   <a name="bedrock-Type-data-automation_BlueprintFilter-blueprintArn"></a>
Filter by blueprint ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`   
Required: Yes

 ** blueprintStage **   <a name="bedrock-Type-data-automation_BlueprintFilter-blueprintStage"></a>
Filter by blueprint stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

 ** blueprintVersion **   <a name="bedrock-Type-data-automation_BlueprintFilter-blueprintVersion"></a>
Filter by blueprint version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[0-9]*`   
Required: No

## See Also
<a name="API_data-automation_BlueprintFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/BlueprintFilter) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/BlueprintFilter) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/BlueprintFilter) 