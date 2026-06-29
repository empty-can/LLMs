

# Blueprint
<a name="API_data-automation-runtime_Blueprint"></a>

Details about a data automation blueprint.

## Contents
<a name="API_data-automation-runtime_Blueprint_Contents"></a>

 ** blueprintArn **   <a name="bedrock-Type-data-automation-runtime_Blueprint-blueprintArn"></a>
The blueprint's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-insights-public-[a-zA-Z0-9-_]{1,30}|bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`   
Required: Yes

 ** stage **   <a name="bedrock-Type-data-automation-runtime_Blueprint-stage"></a>
The blueprint's stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

 ** version **   <a name="bedrock-Type-data-automation-runtime_Blueprint-version"></a>
The blueprint's version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[0-9]*`   
Required: No

## See Also
<a name="API_data-automation-runtime_Blueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/Blueprint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/Blueprint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/Blueprint) 